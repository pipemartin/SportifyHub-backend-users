from rest_framework import serializers
from users.models import User
from rols.api.serializers import RolsSerializer

class UserRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'password']

    #encriptar pass
    def create(self, validate_data):
        password = validate_data.pop('password', None)
        instance = self.Meta.model(**validate_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

#Obteniendo los datos del usuario logeado:
class UserSerializer(serializers.ModelSerializer):
    rol = RolsSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'rol']

#Actualizando datos del usuario
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','phone']