from django.db import models
from canchas.models import Canchas
from users.models import User
# Create your models here.

class Reservas(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    cancha = models.ForeignKey(Canchas, on_delete=models.CASCADE,null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
