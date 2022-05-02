# from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from oneheritagefinance.users.models import Account
from oneheritagefinance.utils.emails import plain_email

from .models import AccountHistory, Debit

# from oneheritagefinance.utils.logger import LOGGER


User = get_user_model()


@receiver(post_save, sender=Debit)
def debit_post_save_signal(sender, created, instance, *args, **kwargs):
    to_email = instance.user.email
    balance = Account.objects.get(user=instance.user, acc_no=instance.acc_no).balance
    r_balance = Account.objects.get(acc_no=instance.recipients_acc_no).balance
    p_balance = r_balance + instance.amount
    m_balance = balance - instance.amount
    if created:
        if (
            instance.transfer_type == Debit.LOCAL
            and balance >= instance.amount
            and instance.verified == Debit.UNVERIFIED
            and instance.user.complete_transaction
        ):
            Account.objects.filter(acc_no=instance.recipients_acc_no).update(
                balance=p_balance
            )
            Account.objects.filter(
                user=instance.user, acc_no=instance.acc_no, balance__gte=instance.amount
            ).update(balance=m_balance)
            Debit.objects.filter(verified=Debit.UNVERIFIED).update(
                verified=Debit.VERIFIED
            )
            AccountHistory.objects.filter(
                user=instance.user,
                account__acc_no=instance.acc_no,
                amount=instance.amount,
                created=instance.created,
            ).update(status=AccountHistory.VERIFIED)
        elif (
            instance.transfer_type == Debit.INTERNATIONAL
            and balance >= instance.amount
            and instance.verified == Debit.UNVERIFIED
            and instance.user.complete_transaction
        ):
            Account.objects.filter(
                user=instance.user, acc_no=instance.acc_no, balance__gte=instance.amount
            ).update(balance=m_balance)
            Debit.objects.filter(verified=Debit.UNVERIFIED).update(
                verified=Debit.PENDING
            )
            AccountHistory.objects.filter(
                user=instance.user,
                account__acc_no=instance.acc_no,
                amount=instance.amount,
                created=instance.created,
            ).update(status=AccountHistory.PENDING)

    if (
        instance.transfer_type == Debit.INTERNATIONAL
        and instance.verified == Debit.VERIFIED
        and instance.user.complete_transaction
    ):
        AccountHistory.objects.filter(
            user=instance.user,
            account__acc_no=instance.acc_no,
            status=AccountHistory.PENDING,
            amount=instance.amount,
            created=instance.created,
        ).update(status=AccountHistory.VERIFIED)
    elif (
        instance.transfer_type == Debit.INTERNATIONAL
        and instance.verified == Debit.BLOCKED
        and instance.user.complete_transaction
    ):
        AccountHistory.objects.filter(
            user=instance.user,
            account__acc_no=instance.acc_no,
            status=AccountHistory.PENDING,
            amount=instance.amount,
            created=instance.created,
        ).update(status=AccountHistory.BLOCKED)
        User.objects.filter(username=instance.user.username).update(
            complete_transaction=False
        )
    elif (
        instance.transfer_type == Debit.LOCAL
        and instance.verified == Debit.BLOCKED
        and instance.user.complete_transaction
    ):
        AccountHistory.objects.filter(
            user=instance.user,
            account__acc_no=instance.acc_no,
            status=AccountHistory.VERIFIED,
            amount=instance.amount,
            created=instance.created,
        ).update(status=AccountHistory.BLOCKED)
        User.objects.filter(username=instance.user.username).update(
            complete_transaction=False
        )
    elif not instance.user.complete_transaction and (
        instance.transfer_type == Debit.LOCAL
        or instance.transfer_type == Debit.INTERNATIONAL
    ):
        subject = _("Account Suspended")
        content = f"""
        Dear {instance.user.username.title()},
        <br>
        <br>
        We regret to inform you that your account with us,
        <br>
        <br>
        ACCOUNT NO: {instance.acc_no}
        <br>
        <br>
        has been suspended.
        <br>
        This is due to a suspected attack/hack/fraud alert imposed on your previous transaction.
        <br>
        <br>
        Please verify your identity or get in touch with your account manager: ({instance.acc_manager})
        """
        body = get_template("mail/simple_mail.html").render(
            context={"subject": subject, "body": mark_safe(content)}
        )
        plain_email(to_email=to_email, subject=subject, body=body)
    # LOGGER.info("Debit request successfully done")
