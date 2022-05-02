from django.urls import path

from oneheritagefinance.users.views import (
    account_view,
    debit_complete,
    kyc_view,
    nok_view,
    photo_view,
    pin_view,
    privacy_view,
    user_blocked_view,
    user_detail_view,
    user_login_home,
    user_redirect_view,
    user_update_view,
    users,
)

app_name = "users"
urlpatterns = [
    path("", view=users, name="users"),
    path("transfer/complete/", view=debit_complete, name="debit_complete"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("~edit-photo/", view=photo_view, name="photo"),

    path("~login/", view=user_login_home, name="login"),

    path('~account/<int:acc_no>/', view=account_view, name="account"),
    path("~account/<int:acc_no>/~update-pin/", view=pin_view, name="pin"),

    path("~verify/", view=kyc_view, name="kyc"),
    path("~next-of-kin/", view=nok_view, name="nok"),
    path("~privacy-settings/", view=privacy_view, name="privacy"),

    path("<str:username>/", view=user_detail_view, name="detail"),
    path("<str:username>/account/blocked/", view=user_blocked_view, name="account_blocked"),

]
