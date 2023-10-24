from django.db import models
from establecimiento.models import Establecimiento

# Create your models here.
class Deporte(models.Model):
    name = models.CharField(max_length=20, unique=True)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE, null=True)

    