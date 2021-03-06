from decimal import Decimal

# from django.conf import settings
from django.contrib.auth import get_user_model
# from django.db.models import Max
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import get_template, render_to_string
from django.utils.safestring import mark_safe

from oneheritagefinance.utils.emails import plain_email
# from oneheritagefinance.utils.logger import LOGGER
from oneheritagefinance.utils.unique_otp import (
    unique_acc_no,
    unique_online_pin_generator,
)

from .models import Account, NextOfKin, Privacy, Profile, VerificationDocuments

User = get_user_model()


@receiver(post_save, sender=User)
def user_post_save_signal(sender, created, instance, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        NextOfKin.objects.create(user=instance)
        Privacy.objects.create(user=instance)

        if instance.account_type == (instance.CHECKING or instance.CORPORATE):
            Account.objects.create(
                user=instance, currency=Account.USD, balance=Decimal("0.00")
            )
            Account.objects.create(
                user=instance, currency=Account.GBP, balance=Decimal("0.00")
            )
            Account.objects.create(
                user=instance, currency=Account.EUR, balance=Decimal("0.00")
            )
            Account.objects.create(
                user=instance, currency=Account.NGN, balance=Decimal("0.00")
            )
        else:
            Account.objects.create(
                user=instance, currency=Account.NGN, balance=Decimal("0.00")
            )

        # LOGGER.info(f"{instance.username} Signal Created")


@receiver(post_save, sender=Account)
def account_post_save_signal(sender, created, instance, *args, **kwargs):
    if not instance.pin and not instance.acc_no:
        pin = unique_online_pin_generator(instance)
        # LOGGER.info("Created Random Transfer PIN")

        # largest = Account.objects.all().aggregate(Max('acc_no'))['acc_no__max']
        # #LOGGER.info(f"largest: {largest}")
        # if largest is not None:
        #     instance.acc_no = int(largest) + 1
        #     #LOGGER.info(f"Created Account Number +1: {instance.acc_no}")
        # else:
        instance.acc_no = unique_acc_no(instance)
        Account.objects.filter(user=instance.user, currency=instance.currency).update(
            acc_no=unique_acc_no(instance), pin=pin
        )

        body2 = f"""
        Hello {instance.user.username.title()},
        <br>
        <br>
        Your Transactional Pin For {instance.acc_no}:
        <br>
        <br>
        Acc No:  {instance.acc_no}.
        Acc Pin: {pin}.
        <br>
        <br>
        Ensure to keep this pin secure.
        <br>
        <br>
        Contact support on info@oneheritagefinance.com if in need to replace your pin.
        <br>
        <br>
        Account Management Department
        One Heritage Finance
        """

        # user_message = get_template('mail/simple_mail.html').render(context={"subject": "REFERRAL ID GENERATED", "body": mark_safe(body2)})
        plain_email(to_email=instance.user.email, subject="Transaction PIN", body=mark_safe(body2))

        # LOGGER.info(f"Created Account Number: {instance.acc_no}")


@receiver(post_save, sender=VerificationDocuments)
def verification_signal(sender, created, instance, *args, **kwargs):
    if (
        created
        and instance.user.verified == User.UNVERIFIED
        and instance.user.verified != User.BLOCKED
    ):
        User.objects.filter(username=instance.user.username).update(
            verified=User.PENDING
        )
        # LOGGER.info("User verification is pending")
