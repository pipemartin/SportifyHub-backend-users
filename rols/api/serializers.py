from rest_framework import serializers
from rols.models import Rol

class RolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'title', 'state']