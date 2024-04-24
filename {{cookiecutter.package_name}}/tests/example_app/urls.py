from django.contrib import admin
from django.urls import include  # noqa: F401
from django.urls import path

admin.site.enable_nav_sidebar = False

urlpatterns = [
    path("admin/", admin.site.urls),
    # Uncomment the next line to enable the admin and app urls
    # path("{{cookiecutter.package_name}}/", include("{{cookiecutter.package_dir}}.urls", namespace="{{cookiecutter.package_name}}")),
]
