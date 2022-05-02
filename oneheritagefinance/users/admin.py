from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from oneheritagefinance.users.forms import UserAdminChangeForm, UserAdminCreationForm

from .models import Account, NextOfKin, Privacy, Profile, VerificationDocuments

User = get_user_model()

admin.site.register(Account)
admin.site.register(NextOfKin)
admin.site.register(Privacy)
admin.site.register(Profile)
admin.site.register(VerificationDocuments)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "complete_transaction",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "name", "complete_transaction", "is_superuser"]
    list_editable = ["name", "complete_transaction", "is_superuser"]
    search_fields = ["name"]
