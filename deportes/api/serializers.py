from rest_framework import serializers
from deportes.models import Deporte

class DeporteSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Deporte
        fields = ['id','name','establecimiento']