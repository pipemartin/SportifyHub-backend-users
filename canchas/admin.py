from django.contrib import admin

# Register your models here.
from canchas.models import Canchas

@admin.register(Canchas)
class CanchasAdmin(admin.ModelAdmin):
    list_display = ['name','deporte', 'disponible']