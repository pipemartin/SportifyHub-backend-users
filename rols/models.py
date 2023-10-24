# Crear el nuevo modelo
from django.db import models

class Rol(models.Model):
    title = models.CharField(max_length=50, unique=True)
    state = models.BooleanField(default=False)

    def __str__(self):
        return self.title
