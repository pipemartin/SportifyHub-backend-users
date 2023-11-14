from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.api.serializers import UserRegisterSerializers, UserSerializer, UserUpdateSerializer
from users.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 28 Obtener datos usuarios

class UserView(APIView):
    # añadir permisos
    #permission_classes = [IsAuthenticated]

    #Obtener usuarios
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    # 29. Actualizando datos del usuario
    def put(self, request):
        #request.user.id
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, User):
        token = super().get_token(User)

        rol = User.rol

        token['username'] = User.username
        token['user_id'] = User.id
        token['first_name'] = User.first_name
        token['rol_title'] = rol.title
        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer