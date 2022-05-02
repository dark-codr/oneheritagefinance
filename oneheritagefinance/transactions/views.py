from decimal import Decimal

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DetailView, RedirectView, UpdateView

from oneheritagefinance.users.models import Account

from .models import SELECT_BANK, AccountHistory, Debit, Deposit, Withdraw

# from oneheritagefinance.utils.logger import LOGGER


User = get_user_model()


def debit_view(request, username):
    user = User.objects.get(username=username)
    amount = request.POST.get("amount")
    pin = request.POST.get("pin")
    transfer_type = request.POST.get("transfer_type")
    account = request.POST.get("account")
    name = request.POST.get("name")
    address = request.POST.get("address")
    res_account = request.POST.get("res_account")
    res_bank = request.POST.get("res_bank")
    route_no = request.POST.get("route_no")
    purpose = request.POST.get("purpose")

    amount = Decimal(int(amount))
    pin = int(pin)
    account = int(account)

    # LOGGER.info(f"{user.username} is attempting to debit {amount} from {account} to {res_account}")
    # LOGGER.info(f"{pin} is the pin used")
    # LOGGER.info(f"{transfer_type} is the transfer type initiated")

    user_account = Account.objects.get(user=user, acc_no=account, pin=pin)
    balance = user_account.balance - amount
    Account.objects.filter(user=user, acc_no=account, pin=pin).update(balance=balance)

    if transfer_type == "Local":
        if user_account.balance >= amount and user.complete_transaction:
            Debit.objects.create(
                user=user,
                transfer_type=transfer_type,
                local_bank=res_bank,
                acc_no=account,
                amount=amount,
                pin=pin,
                recipients_bank=res_bank,
                recipients_acc_no=res_account,
                recipients_route_no=route_no,
                purpose=purpose,
            )
            AccountHistory.objects.create(
                user=user,
                account=user_account,
                amount=amount,
                transfer_type=AccountHistory.TRANSFER,
                purpose=purpose,
                status=AccountHistory.VERIFIED,
            )
            message = f"You have successfully transferred {amount} from {account} to {res_account}. Your transaction will be complete after 3-5 mins."
            del request.session["account"]
            del request.session["transfer_type"]
            del request.session["pin"]
            del request.session["res_account"]
            return render(
                request,
                "users/complete.html",
                context={
                    "object": user,
                    "message": message,
                    "heading": "Transfer Successfull",
                },
            )
    elif transfer_type == "International":
        if user_account.balance >= amount and user.complete_transaction:
            Debit.objects.create(
                recipient_name=name,
                recipient_address=address,
                user=user,
                transfer_type=transfer_type,
                local_bank=account,
                acc_no=account,
                amount=amount,
                pin=pin,
                recipients_bank=res_bank,
                recipients_acc_no=res_account,
                recipients_route_no=route_no,
                purpose=purpose,
            )
            AccountHistory.objects.create(
                user=user,
                account=user_account,
                amount=amount,
                transfer_type=AccountHistory.TRANSFER,
                purpose=purpose,
                status=AccountHistory.PENDING,
            )
            message = f"You have successfully transferred {amount} from {account} to {res_account}. Your transaction will be complete after 3-5 working days."
            del request.session["account"]
            del request.session["transfer_type"]
            del request.session["pin"]
            del request.session["res_account"]
            return render(
                request,
                "users/complete.html",
                context={
                    "object": user,
                    "message": message,
                    "heading": "Transfer Successfull",
                },
            )
    message = f"There was an error transferring from {account} to {res_account}. Please try again."
    return render(
        request,
        "users/complete.html",
        context={"object": user, "message": message, "heading": "Transfer Failed"},
    )


def chk_tf_type(request):
    transfer_type = request.GET.get("transfer_type")
    request.session["transfer_type"] = transfer_type
    if transfer_type == "International":
        return render(request, "users/int.html")
    elif transfer_type == "Local":
        return render(
            request,
            "users/banks.html",
            context={"banks": SELECT_BANK, "accounts": Account.objects.all()},
        )


def chk_acc(request):
    user = request.user
    account = request.GET.get("account")
    request.session["account"] = account
    if Account.objects.filter(user=user, acc_no=account).exists():
        return render(request, "users/pin.html")


def check_pin(request):
    user = request.user
    pin = request.GET.get("pin")
    request.session["pin"] = pin
    account = request.session.get("account")
    if Account.objects.filter(user=user, pin=pin, acc_no=account).exists():
        return render(request, "users/submit.html", context={"object": user})
    else:
        return HttpResponse("Wrong Pin")


def check_res_acc(request):
    transfer_type = request.session.get("transfer_type")
    res_account = request.GET.get("res_account")
    res_account = int(res_account)
    # LOGGER.info(res_account)
    request.session["res_account"] = res_account
    user_account = Account.objects.filter(acc_no=res_account).exists()
    if (
        transfer_type == "Local"
        and res_account < 1000000000
        or res_account > 999999999999999999
    ):
        return HttpResponse("Invalid Account")
    elif transfer_type == "Local" and not user_account:
        return HttpResponse("Not OHF Account")
    elif user_account and transfer_type == "Local":
        # account = Account.objects.filter(acc_no=res_account).first()
        account = Account.objects.get(acc_no=res_account)
        # LOGGER.info(f"account to credit {account.user.username}")
        if account.user.name:
            return HttpResponse(account.user.name.title())
        else:
            return HttpResponse(account.user.username.title())
