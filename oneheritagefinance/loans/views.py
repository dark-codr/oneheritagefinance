# from django.contrib.auth import get_user_model
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.messages.views import SuccessMessageMixin
# from django.http import HttpResponseRedirect
# from django.shortcuts import redirect
# from django.urls import reverse
# from django.utils.translation import gettext_lazy as _
# from django.views.generic import DetailView, RedirectView, UpdateView

# from .models import Deposit, Withdraw

# User = get_user_model()

# class DepositView(LoginRequiredMixin, CreateView):
#     model = Deposit
#     fields = ['amount', 'acc_no', 'pin']
#     template_name = "transaction/deposit.html"

#     def form_valid(self, form):
#         form = form.save(commit=False)
#         if self.request.user.account_set.filter(acc_no=form.acc_no, pin=form.pin):
#             form.user = self.request.user
#             form.save()
#             Account.objects.filter(acc_no=form.acc_no).update(balance+=form.amount)
#             messages.success(self.request, _(f"You have successfully deposited {form.amount} to {form.acc_no}"))
#             return redirect('/')
#         elif self.request.user.account_set.filter(pin!=form.pin):
#             messages.error(self.request, _(f"Wrong transaction pin"))
#             return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
#         else:
#             messages.error(self.request, _("Wrong Account Number"))
#             return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

# deposit_view = DepositView.as_view()

# class WithdrawView(LoginRequiredMixin, CreateView):
#     model = Withdraw
#     fields = ['amount', 'acc_no', 'pin']
#     template_name = "transaction/withdraw.html"

#     def form_valid(self, form):
#         form = form.save(commit=False)
#         if self.request.user.account_set.filter(acc_no=form.acc_no, pin=form.pin, balance__gte=form.amount):
#             form.user = self.request.user
#             form.save()
#             Account.objects.filter(acc_no=form.acc_no, balance__gte=form.amount).update(balance-=form.amount)
#             messages.success(self.request, _(f"You have successfully withdrawn {form.amount} from {form.acc_no}"))
#             return redirect('dashboard')
#         elif self.request.user.account_set.filter(balance__lt=form.amount):
#             messages.error(self.request, _(f"Insufficient balance"))
#             return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
#         elif self.request.user.account_set.filter(pin!=form.pin):
#             messages.error(self.request, _(f"Wrong transaction pin"))
#             return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
#         elif not self.request.user.complete_transaction:
#             messages.error(self.request, _(f"This account has been suspended. Refer to your email for more information."))
#             return redirect('blocked')
#         else:
#             messages.error(self.request, _("Wrong Account Number"))
#             return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

# withdraw_view = WithdrawView.as_view()

# class DebitView(LoginRequiredMixin, CreateView):
#     model = Debit
#     fields = [
#         "transfer_type",
#         "local_bank",
#         "acc_no",
#         "amount",
#         "recipients_bank",
#         "recipients_bank_swift",
#         "recipients_name",
#         "recipients_address",
#         "recipients_acc_no",
#         "recipients_route_no",
#         "pin"
#     ]
#     template_name = "transaction/debit.html"

#     if form_valid(self, form):
#         form = form.save(commit=False)
#         if self.request.user.account_set.filter(acc_no=form.acc_no, pin=form.pin, balance__gte=form.amount) and self.request.user.complete_transaction:
#             form.user = self.request.user
#             form.save()
#             messages.success(self.request, _(f"You have successfully transferred {form.amount} from {form.acc_no} to {form.recipients_acc_no}. Your transaction will be complete after 3-5 working days."))
#             return redirect('dashboard')
#         elif self.request.user.account_set.filter(balance__lt=form.amount):
#             messages.error(self.request, _(f"Insufficient balance"))
#             return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
#         elif self.request.user.account_set.filter(pin!=form.pin):
#             messages.error(self.request, _(f"Wrong transaction pin"))
#             return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
#         elif not self.request.user.complete_transaction:
#             messages.error(self.request, _(f"This account has been suspended. Refer to your email for more information."))
#             return redirect('blocked')
#         else:
#             messages.error(self.request, _("Wrong Account Number"))
#             return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

# debit_view = DebitView.as_view()
