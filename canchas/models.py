from django.db import models
from deportes.models import Deporte
# Create your models here.

class Canchas(models.Model):
    name = models.CharField(max_length=20)
    deporte = models.ForeignKey(Deporte,on_delete=models.CASCADE, null=False)
    disponible = models.BooleanField(default=False)

