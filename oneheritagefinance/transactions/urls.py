from django.urls import path

from .views import (  # deposit_view,; withdraw_view,
    check_pin,
    check_res_acc,
    chk_acc,
    chk_tf_type,
    debit_view,
)

app_name = "transactions"
urlpatterns = [
    path("check-tf/", view=chk_tf_type, name="check_tf"),
    path("check-acc/", view=chk_acc, name="check_acc"),
    path("check-pin/", view=check_pin, name="check_pin"),
    path("check-racc/", view=check_res_acc, name="check_racc"),
    path("<username>/debit/", view=debit_view, name="debit"),
]
