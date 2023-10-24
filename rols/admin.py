# 4 añadir el modelo
from django.contrib import admin
from rols.models import Rol


@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ['title', 'state']