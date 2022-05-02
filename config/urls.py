from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views as flatpage_views
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.utils.translation import gettext_lazy as _
from django.views import defaults as default_views
from django.views.generic import TemplateView
from filebrowser.sites import site as filebrowser

from config.sitemaps import StaticViewSitemap
from oneheritagefinance.core.views import switch_language

# from django.views.i18n import JavaScriptCatalog


sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = i18n_patterns(
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        _("about/"),
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(_("admin/"), include("admin_honeypot.urls", namespace="admin_honeypot")),
    path(settings.ADMIN_URL, admin.site.urls),
    path(settings.ADMIN_DOC_URL, include("django.contrib.admindocs.urls")),
    # User management
    path("rosetta/", include("rosetta.urls")),
    # path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path(_("users/"), include("oneheritagefinance.users.urls", namespace="users")),
    path(
        _("transactions/"),
        include("oneheritagefinance.transactions.urls", namespace="transactions"),
    ),
    path(_("accounts/"), include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path("tinymce/", include("tinymce.urls")),
    path(settings.ADMIN_FILEBROWSER_URL, filebrowser.urls),
    path("__reload__/", include("django_browser_reload.urls")),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# flatpages
if flatpage_views:
    urlpatterns += i18n_patterns(
        path(_("terms/"), flatpage_views.flatpage, {"url": "/terms/"}, name="terms"),
        path(
            _("cookies/"), flatpage_views.flatpage, {"url": "/cookies/"}, name="cookies"
        ),
        path(
            _("privacy/"), flatpage_views.flatpage, {"url": "/privacy/"}, name="privacy"
        ),
    )

urlpatterns += i18n_patterns(
    path("i18n/", include("django.conf.urls.i18n")),
    path(_("sitemap.xml/"), sitemap, kwargs={"sitemaps": sitemaps}, name="sitemap"),
    path(
        _("robots.txt/"),
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
        name="robots",
    ),
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += i18n_patterns(
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    )

    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = (
            i18n_patterns(path("__debug__/", include(debug_toolbar.urls))) + urlpatterns
        )

urlpatterns += [
    path("<str:language>/<str:url>/", view=switch_language, name="language"),
]

admin.site.site_header = _("Dashboard - One Heritage Finance")
admin.site.site_title = _("One Heritage Finance Dashboard")
admin.site.index_title = _("One Heritage Finance Dashboard")
