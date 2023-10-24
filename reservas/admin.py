from django.contrib import admin

# Register your models here.
from reservas.models import Reservas

@admin.register(Reservas)
class ReservasAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'hora', 'cancha','user']