from rest_framework import serializers
from canchas.models import Canchas

class CanchasSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Canchas
        fields = ['id', 'name','deporte', 'disponible']