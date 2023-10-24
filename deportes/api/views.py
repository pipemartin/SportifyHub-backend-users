from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
from deportes.api.serializers import DeporteSerializers 
from establecimiento.models import Establecimiento
from deportes.models import Deporte
from rols.api.permissions import IsAdmin
#from rest_framework.decorators import  permission_classes

class DeporteResgisterView(APIView):
    permission_classes = [IsAdmin]
    def post(self, request):
        #validando data del request que llegue bien
        serializer = DeporteSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListDeporteView(generics.ListAPIView):    
    def get(self, request):
        qs = Deporte.objects.all()
        serializer = DeporteSerializers(qs,many=True)
        return Response(serializer.data)
    
class DeleteDeportes(APIView):
    permission_classes = [IsAdmin]
    #valida si tiene token en el head
    def post(self, request):
        try:
            #falta validar si es admin
            deporte_id = request.data.get('id')
            deporte = Deporte.objects.get(id=deporte_id)
            deporte.delete()
            return Response({'message': 'El deporte ha sido eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)
        except Deporte.DoesNotExist:
            return Response({'message': 'El deporte no existe.'}, status=status.HTTP_404_NOT_FOUND)
        
class UpdateDeportes(APIView):
    permission_classes = [IsAdmin]
    def put(self, request):
        try:
            deporte_id = request.data.get('id')
            deporte = Deporte.objects.get(id=deporte_id)
        except Deporte.DoesNotExist:
            return Response({'message': 'El establecimiento no existe.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DeporteSerializers(deporte, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)