# from django.db.models import BooleanField, CharField, DecimalField
# from django.utils.translation import gettext_lazy as _
# from model_utils.models import TimeStampedModel
# from tinymce import HTMLField


# class Currency(TimeStampedModel):
#     NGN = "NGN"
#     USD = "USD"
#     EUR = "EUR"
#     GBP = "GBP"
#     CNY = "CNY"
#     JPY = "JPY"
#     AUD = "AUD"
#     CAD = "CAD"
#     CHF = "CHF"
#     DKK = "DKK"
#     SEK = "SEK"
#     ZAR = "ZAR"
#     AED = "AED"
#     CODE = (
#         (NGN, "Nigerian Naira"),
#         (USD, "United States Dollar"),
#         (EUR, "Euro"),
#         (GBP, "British Pound"),
#         (CNY, "Chinese Yuan"),
#         (JPY, "Japanese Yen"),
#         (AUD, "Australian Dollar"),
#         (CAD, "Canadian Dollar"),
#         (CHF, "Swiss Franc"),
#         (DKK, "Danish Krone"),
#         (SEK, "Swedish Krona"),
#         (ZAR, "South African Rand"),
#         (AED, "United Arab Emirates Dirham"),
#     )
#     code = CharField(max_length=3, choices=CODE, default=USD, blank=False, null=False, unique=True)
#     symbol = CharField(max_length=10, blank=False, null=False, unique=True)
#     price = DecimalField(max_digits=20, decimal_places=2, blank=False, default=0.00, null=False)

#     def __str__(self):
#         return self.code

#     class Meta:
#         verbose_name = _("Currency")
#         verbose_name_plural = _("Currencies")
#         ordering = ["code"]
