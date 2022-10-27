from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls), path("", lambda x: HttpResponse("OK"), name="home"),
    path("api/", include('app.urls', namespace="app")),
    path("api/", include('common.urls', namespace="common")),
    path("api/", include('authentication.urls', namespace="authentication")),
    path("api/settings/", include('settings.urls', namespace="settings")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns.insert(0, path('__debug__/', include('debug_toolbar.urls')))
