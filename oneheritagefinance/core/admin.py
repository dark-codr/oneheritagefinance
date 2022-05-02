# from django.contrib import admin
# from django.utils.translation import gettext_lazy as _
# from parler.admin import TranslatableAdmin

# from oneheritagefinance.utils.export_as_csv import ExportCsvMixin

# from .models import Currency


# class CurrencyAdmin(admin.ModelAdmin, ExportCsvMixin):
#     list_display = ('code', 'symbol', 'price', 'created', 'modified')
#     list_filter = ('created', 'modified')
#     search_fields = ('code', 'symbol', 'price')

#     actions = [
#         "export_as_csv",
#     ]

#     # def save_model(self, request, obj, form, change):
#     #     user = request.user
#     #     if change and form.is_valid():
#     #         obj.admin = user
#     #         obj.save()
#     #     super().save_model(request, obj, form, change)


# admin.site.register(Currency, TranslatableAdmin)
