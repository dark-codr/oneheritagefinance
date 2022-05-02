from django.conf import settings

from oneheritagefinance.users.models import Account


def context_data(request):
    """Expose some settings from django-allauth in templates."""
    if request.user.is_authenticated:
        accounts = Account.objects.filter(user=request.user)
    else:
        accounts = None
    return {
        "ACCOUNT_ALLOW_REGISTRATION": settings.ACCOUNT_ALLOW_REGISTRATION,
        "DEBUG": settings.DEBUG,
        "ACCOUNTS": accounts
    }
