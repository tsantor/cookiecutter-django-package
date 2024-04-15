# {{ cookiecutter.project_name }}

![Coverage](https://img.shields.io/badge/coverage-97%25-brightgreen)

<!-- ![Code Style](https://img.shields.io/badge/code_style-ruff-black) -->

## Overview

{{ cookiecutter.project_short_description }}

## Quickstart

Install {{ cookiecutter.project_name }}:

```bash
python3 -m pip install {{cookiecutter.package_name}}
```

### Settings

To enable `{{cookiecutter.project_slug}}` in your project you need to add it to `INSTALLED_APPS` in your projects `settings.py` file:

```python
INSTALLED_APPS = (
    ...
    '{{cookiecutter.project_slug}}',
    ...
)
```

Add {{cookiecutter.package_name}}'s URL patterns:

```python
from {{cookiecutter.project_slug}} import urls as {{cookiecutter.project_slug}}_urls


urlpatterns = [
    ...
    path(r"", include({{cookiecutter.project_slug}}_urls, namespace='{{cookiecutter.package_name}}')),
    ...
]
```

## Local Development

```bash
make env
make pip_install
make migrations
make migrate
make superuser
make serve
```

or simply `make from_scratch`

- Visit `http://127.0.0.1:8000/admin/` for the Django Admin

### Testing

```bash
make pytest
make coverage
make open_coverage
```

## Issues

If you experience any issues, please create an [issue](https://github.org/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}/issues) on Github.
