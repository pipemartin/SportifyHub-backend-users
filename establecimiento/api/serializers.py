from rest_framework import serializers, generics
from establecimiento.models import Establecimiento
from users.api.serializers import UserSerializer

class EstablecimientoSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    direccion = serializers.CharField(max_length=200, required=True)
    phone = serializers.CharField(max_length=15, required=True)

    class Meta:
        model = Establecimiento
        fields = ['id','name', 'direccion', 'phone', 'user']



