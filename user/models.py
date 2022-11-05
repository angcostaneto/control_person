import uuid

from django.db import models


# Create your models here.
class Person(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  first_name = models.CharField(max_length=255)
  middle_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  rg = models.CharField(max_length=255)
  cpf = models.CharField(max_length=255)
