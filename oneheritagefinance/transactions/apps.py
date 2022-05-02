from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TransactionsConfig(AppConfig):
    name = "oneheritagefinance.transactions"
    verbose_name = _("Transactions")

    def ready(self):
        try:
            import oneheritagefinance.transactions.signals  # noqa F401
        except ImportError:
            pass
