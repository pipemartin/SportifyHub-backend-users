from django.db import models
from django.db.models import SET_NULL
from users.models import User

# Create your models here.
class Establecimiento(models.Model):
    #Cambiar el username por el email user para logearse
    name = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    # referencia a la tabla rol
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, to_field='id',  related_name='user_id')
    