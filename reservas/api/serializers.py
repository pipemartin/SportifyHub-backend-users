from rest_framework import serializers
from reservas.models import Reservas

class ReservasSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Reservas
        fields = ['fecha', 'hora', 'cancha','user']