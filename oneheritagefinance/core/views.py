# import datetime
# from decimal import Decimal

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.messages.views import SuccessMessageMixin
# from django.db.models import Sum
# from django.http import Http404, HttpResponseRedirect
# from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
# from django.template.loader import get_template, render_to_string
from django.urls import reverse
from django.utils import translation
# from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

User = get_user_model()

# from django.views.generic import CreateView, DetailView, RedirectView, UpdateView

# from oneheritagefinance.utils.logger import LOGGER


def home(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = authenticate(request, email=email, password=password)
    if user is not None:
        # #LOGGER.info(f"user info: {user.username} - {email}")
        login(request, user)
        messages.info(request, "You have successfully logged in")
        username = request.user.username
        return redirect("users:detail", username=username)
    return render(request, "pages/home.html", context={"user": user, "email": email})


def switch_language(request, **kwargs):
    language = kwargs.get("language")
    redirect_url_name = request.GET.get("url")  # e.g. '/about/'

    # make sure language is available
    valid = False
    for l in settings.LANGUAGES:
        if l[0] == language:
            valid = True
    if not valid:
        raise Http404(_("The selected language is unavailable!"))

    # Make language the setting for the session
    translation.activate(str(language))
    # response = redirect(reverse(redirect_url_name)) # Changing this to use reverse works

    # response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    # return response
    return redirect(
        reverse(language, kwargs={"url": redirect_url_name})
    )  # Changing this to use reverse works
