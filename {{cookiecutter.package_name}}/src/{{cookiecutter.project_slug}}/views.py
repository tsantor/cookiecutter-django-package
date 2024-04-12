from django.views.generic import TemplateView


class MyView(TemplateView):
    template_name = '{{cookiecutter.project_slug}}/my_template.html'
