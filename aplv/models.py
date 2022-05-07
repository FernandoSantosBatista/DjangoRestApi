from django.db import models
from uuid import uuid4

# Create your models here.

class Aplv(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)