from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rols.api.permissions import IsAdmin
from establecimiento.api.serializers import EstablecimientoSerializers
from establecimiento.models import Establecimiento
from users.models import User

class ResgisterView(APIView):
    permission_classes = [IsAdmin]
    def post(self, request):
        #validando data del request que llegue bien
        serializer = EstablecimientoSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
class ListEstablecimientoView(generics.ListAPIView):
    #valida si tiene token en el head
    def get(self, request):
        qs = Establecimiento.objects.all()
        serializer = EstablecimientoSerializers(qs,many=True)
        return Response(serializer.data)
    
class DeleteEstablecimiento(APIView):
    permission_classes = [IsAdmin]
    #valida si tiene token en el head
    def post(self, request):
        try:
            #falta validar si es admin
            establecimiento_id = request.data.get('id')
            establecimiento = Establecimiento.objects.get(id=establecimiento_id)
            establecimiento.delete()
            return Response({'message': 'El establecimiento ha sido eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)
        except Establecimiento.DoesNotExist:
            return Response({'message': 'El establecimiento no existe.'}, status=status.HTTP_404_NOT_FOUND)
        
class UpdateEstablecimiento(APIView):
    permission_classes = [IsAdmin]
    def put(self, request):
        try:
            establecimiento_id = request.data.get('id')
            establecimiento = Establecimiento.objects.get(id=establecimiento_id)
        except Establecimiento.DoesNotExist:
            return Response({'message': 'El establecimiento no existe.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EstablecimientoSerializers(establecimiento, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
