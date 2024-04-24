# {{ cookiecutter.project_name }}

![Coverage](https://img.shields.io/badge/coverage-97%25-brightgreen)

## Overview

{{ cookiecutter.description }}

## Quickstart

Install {{ cookiecutter.project_name }}:

```bash
# From pypi
python3 -m pip install {{cookiecutter.package_name}}

# From source
python3 -m pip install git+https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}.git
```

### Settings

To enable `{{cookiecutter.package_dir}}` in your project you need to add it to `INSTALLED_APPS` in your projects `settings.py` file:

```python
INSTALLED_APPS = (
    ...
    '{{cookiecutter.package_dir}}',
    ...
)
```

Add {{cookiecutter.package_name}}'s URL patterns:

```python
from {{cookiecutter.package_dir}} import urls as {{cookiecutter.package_dir}}_urls


urlpatterns = [
    ...
    path(r"", include({{cookiecutter.package_dir}}_urls, namespace='{{cookiecutter.package_name}}')),
    ...
]
```

## Development

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

## Deploying

```bash
# Publish to PyPI Test before the live PyPi
make release_test
make release
```

## Issues

If you experience any issues, please create an [issue](https://github.org/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}/issues) on Github.
