from django.contrib import admin

# Register your models here.
from deportes.models import Deporte

@admin.register(Deporte)
class DeporteAdmin(admin.ModelAdmin):
    list_display = ['name', 'establecimiento']