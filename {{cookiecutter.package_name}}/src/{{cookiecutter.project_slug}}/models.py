from django.db import models
import uuid

from {{cookiecutter.project_slug}}.mixins import TimeStampedMixin


# class MyModel(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name
