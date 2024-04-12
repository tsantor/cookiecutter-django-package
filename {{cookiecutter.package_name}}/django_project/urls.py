from django.contrib import admin
from django.urls import include, path

admin.site.enable_nav_sidebar = False

urlpatterns = [
    path("admin/", admin.site.urls),
    path("{{cookiecutter.package_name}}/", include("{{cookiecutter.project_slug}}.urls", namespace="{{cookiecutter.package_name}}")),
]
