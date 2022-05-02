from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DetailView, RedirectView, UpdateView

from oneheritagefinance.transactions.models import SELECT_BANK

from .models import Account, NextOfKin, Privacy, Profile, VerificationDocuments

# from oneheritagefinance.utils.logger import LOGGER


User = get_user_model()


def user_login_home(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = authenticate(request, email=email, password=password)
    if user is not None:
        # LOGGER.info(f"user info: {request.user.username} - {email}")
        login(request, user)
        messages.info(request, "You have successfully logged in")
        username = request.user.username
        return redirect("users:detail", username=username)
    else:
        messages.error(request, "Invalid credentials")
        return redirect("users:login")


class UsersDetailView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


users = UsersDetailView.as_view()


class UserDebitCompleteView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


debit_complete = UserDebitCompleteView.as_view()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            del self.request.session["account"]
            del self.request.session["transfer_type"]
            del self.request.session["pin"]
            del self.request.session["res_account"]
        except KeyError:
            pass
        context["banks"] = SELECT_BANK
        return context


user_detail_view = UserDetailView.as_view()


class UserBlockedDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "users/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        try:
            del self.request.session["account"]
            del self.request.session["transfer_type"]
            del self.request.session["pin"]
            del self.request.session["res_account"]
        except:
            pass
        context["banks"] = SELECT_BANK
        return context


user_blocked_view = UserBlockedDetailView.as_view()


class UserNOKUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = NextOfKin
    fields = [
        "name",
        "image",
        "gender",
        "dob",
        "phone",
        "country",
        "address",
        "postal_code",
    ]
    success_message = _("Kin Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.kin


nok_view = UserNOKUpdateView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Profile
    fields = ["gender", "dob", "phone", "country", "address", "postal_code"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        assert self.request.user.is_authenticated
        return self.request.user.profile


user_update_view = UserUpdateView.as_view()


class UserPhotoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Profile
    fields = [
        "image",
    ]
    success_message = _("Profile Photo successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        assert self.request.user.is_authenticated
        return self.request.user.profile


photo_view = UserPhotoUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


class AccountView(LoginRequiredMixin, DetailView):

    model = Account

    def get_object(self, queryset=None):
        return Account.objects.get(acc_no=self.kwargs.get("acc_no"))


account_view = AccountView.as_view()


class ChangePin(LoginRequiredMixin, UpdateView):

    model = Account
    fields = ["pin"]

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return Account.objects.get(acc_no=self.kwargs.get("acc_no"))


pin_view = ChangePin.as_view()


class KYCVerification(LoginRequiredMixin, CreateView):

    model = VerificationDocuments
    fields = ["file", "address_file", "company_certificate"]

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def form_valid(self, form):
        assert self.request.user.is_authenticated
        form = form.save(commit=False)
        if (
            self.request.user.verified == User.UNVERIFIED
            and self.request.user.verified != User.BLOCKED
            and self.request.user.verified != User.PENDING
        ):
            form.user = self.request.user
            form.save()
            messages.success(
                self.request,
                f"You have successfully deposited {form.amount} to {form.acc_no}",
            )
            return redirect(self.get_success_url())
        else:
            messages.error(self.request, "Wrong Account Number")
            return HttpResponseRedirect(self.request.META.get("HTTP_REFERER", "/"))


kyc_view = KYCVerification.as_view()


class UserPrivacyUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Privacy
    fields = [
        "cookies_and_tracking",
        "google_ads",
        "social_account_integration",
        "personal_information",
        "commercial_information",
        "identifiers",
        "internet_or_other_electronic_network_activity_information",
    ]
    success_message = _("Privacy Settings Successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        assert self.request.user.is_authenticated
        return self.request.user.privacy


privacy_view = UserPrivacyUpdateView.as_view()
