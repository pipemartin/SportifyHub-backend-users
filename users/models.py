from django.db import models
from django.db.models import SET_NULL
from django.contrib.auth.models import AbstractUser
from rols.models import Rol

class User(AbstractUser):
    #Cambiar el username por el email user para logearse
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    username = models.CharField(max_length=15, unique=True)
    # referencia a la tabla rol
    rol = models.ForeignKey(Rol, on_delete=SET_NULL, null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []