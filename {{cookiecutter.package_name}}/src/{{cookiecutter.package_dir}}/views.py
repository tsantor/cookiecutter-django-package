from django.views.generic import TemplateView


class MyView(TemplateView):
    template_name = '{{cookiecutter.package_dir}}/my_template.html'
