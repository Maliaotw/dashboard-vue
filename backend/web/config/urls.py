from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# from django.views import defaults as default_views
# from django.views.generic import TemplateView
from django.http import HttpResponse
from django.urls import include, path

urlpatterns = [
                  # path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
                  # path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
                  # # Django Admin, use {% url 'admin:index' %}
                  path(settings.ADMIN_URL, admin.site.urls),
                  # # Your stuff: custom urls includes go here
                  path("", lambda x: HttpResponse("OK"), name="home"),
                  path("api/", include('app.urls', namespace="app")),
                  path("api/", include('common.urls', namespace="common")),
                  path("api/", include('authentication.urls', namespace="authentication")),
                  path("api/settings/", include('settings.urls', namespace="settings")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
