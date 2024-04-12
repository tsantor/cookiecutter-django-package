from django.urls import path

from .views import MyView

app_name = "{{cookiecutter.package_name}}"

urlpatterns = [
    path("", MyView.as_view(), name="my-view"),
]
