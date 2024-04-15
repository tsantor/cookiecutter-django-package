from django.apps import AppConfig


class {{cookiecutter.project_name.replace(" ", "")}}Config(AppConfig):
    name = "{{cookiecutter.package_dir}}"
    verbose_name = "{{cookiecutter.project_name}}"
    default_auto_field = "django.db.models.AutoField"
