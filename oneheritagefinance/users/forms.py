from allauth.account.forms import (  # AddEmailForm,; ChangePasswordForm,; ResetPasswordForm,; ResetPasswordKeyForm,
    LoginForm,
    SignupForm,
)
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
# from attr import attrs
from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """

    name = forms.CharField(
        max_length=255,
        label="Name",
        widget=forms.TextInput(
            attrs={"title": "Your Name", "placeholder": "Firstname Lastname"}
        ),
    )
    account_type = forms.ChoiceField(
        choices=User.ACCOUNT_TYPE,
        widget=forms.Select(
            attrs={
                "class": """form-control fbc-has-badge fbc-UID_1 appearance-none relative block w-full px-3 py-2 border
                border-gray-300 placeholder-gray-500 text-dark focus:outline-none focus:ring-primary focus:border-primary focus:z-10 sm:text-xl"""
            }
        ),
    )

    def save(self, request):
        user = super(UserSignupForm, self).save(request)
        user.name = self.cleaned_data["name"]
        user.account_type = self.cleaned_data["account_type"]
        user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        self.fields["email"].label = ""
        self.fields["name"].label = ""
        self.fields["account_type"].label = ""
        self.fields["password1"].label = ""
        self.fields["password2"].label = ""
        self.fields["username"].label = ""
        self.fields["email"].widget = forms.EmailInput(
            attrs={
                "placeholder": "Your Email",
                "hx-post": "/accounts/signup/check-email/",
                "hx-target": "#email-err",
                "hx-trigger": "keyup",
                "class": """textinput textInput form-control fbc-has-badge fbc-UID_1 appearance-none relative block w-full
                px-3 py-2 border border-gray-300 placeholder-gray-500 text-dark rounded-t-md focus:outline-none focus:ring-primary focus:border-primary focus:z-10 sm:text-xl""",
            }
        )
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": """form-control fbc-has-badge fbc-UID_1 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-
                500 text-dark focus:outline-none focus:ring-primary focus:border-primary focus:z-10 sm:text-xl""",
            }
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": """textinput textInput form-control fbc-has-badge appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500
                 text-dark rounded-b-md focus:outline-none focus:ring-primary focus:border-primary focus:z-10 sm:text-xl""",
            }
        )
        self.fields["username"].widget = forms.TextInput(
            attrs={
                "placeholder": "Your Username",
                "class": """form-control fbc-has-badge fbc-UID_1 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-dark
                focus:outline-none focus:ring-primary focus:border-primary focus:z-10 sm:text-xl""",
                "hx-pos""t": "/accounts/signup/check-username/",
                "hx-target": "#username-err",
                "hx-trigger": "keyup",
            }
        )
        self.fields["name"].widget = forms.TextInput(
            attrs={
                "placeholder": "Your Name",
                "class": """form-control fbc-has-badge fbc-UID_1 appearance-none relative block w-full px-3 py-2 border border-gray-300
                 placeholder-gray-500 text-dark focus:outline-none focus:ring-primary focus:border-primary focus:z-10 sm:text-xl""",
            }
        )


class UserLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields["email"].label = ""
        self.fields["password"].label = ""
        self.fields["login"].widget = forms.TextInput(
            attrs={
                "type": "email",
                "class": """textinput textInput form-control fbc-has-badge fbc-UID_1 appearance-none relative block w-full px-3
                py-2 border border-gray-300 placeholder-gray-500 text-dark rounded-t-md focus:outline-none focus:ring-primary focus:border-primary focus:z-10 sm:text-xl""",
            }
        )
        self.fields["password"].widget = forms.PasswordInput(
            attrs={
                "class": """textinput textInput form-control fbc-has-badge fbc-UID_1 appearance-none relative block w-full px-3
                 py-2 border border-gray-300 placeholder-gray-500 text-dark rounded-b-md focus:outline-none focus:ring-primary focus:border-primary focus:z-10 sm:text-xl"""
            }
        )


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """
