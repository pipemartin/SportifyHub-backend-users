from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
from canchas.api.serializers import CanchasSerializers 
from canchas.models import Canchas
from rols.api.permissions import IsAdmin



class CanchasResgisterView(APIView):
    permission_classes = [IsAdmin]
    def post(self, request):
        #validando data del request que llegue bien
        serializer = CanchasSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListCanchasView(generics.ListAPIView):
    #valida si tiene token en el head
    def get(self, request):
        qs = Canchas.objects.all()
        serializer = CanchasSerializers(qs,many=True)
        return Response(serializer.data)
    
class ListCanchasDisponibleView(generics.ListAPIView):
    #valida si tiene token en el head
    def get(self, request):
        qs = Canchas.objects.filter(disponible=False)
        serializer = CanchasSerializers(qs,many=True)
        return Response(serializer.data)
    
class TotalCanchasDisponibleView(generics.ListAPIView):
    #valida si tiene token en el head
    def post(self, request):
        try: 
            #estan disponible la variable se identifica como false
            deporte_id = request.data.get('deporte_id')
            qs = Canchas.objects.filter(disponible=False, deporte = deporte_id)
            cantidad_canchas_disponibles = qs.count()
            return Response({'totalDisponible': cantidad_canchas_disponibles})
        except Canchas.DoesNotExist:
            return Response({'message':'No hay canchas para ese deporte'},
                            status=status.HTTP_404_NOT_FOUND)

class CanchasDisponibleDeporteView(generics.ListAPIView):
    #valida si tiene token en el head
    def post(self, request):
        try: 
            #estan disponible la variable se identifica como false
            deporte_id = request.data.get('deporte_id')
            qs = Canchas.objects.filter(disponible=False, deporte = deporte_id)
            serializer = CanchasSerializers(qs,many=True)
            return Response(serializer.data)
        except Canchas.DoesNotExist:
            return Response({'message':'No hay canchas para ese deporte'},
                            status=status.HTTP_404_NOT_FOUND)

class ListCanchasOcupadasView(generics.ListAPIView):
    #valida si tiene token en el head
    def get(self, request):
        qs = Canchas.objects.filter(disponible=True)
        serializer = CanchasSerializers(qs,many=True)
        return Response(serializer.data)


class DeleteCanchas(APIView):
    permission_classes = [IsAdmin]
    #valida si tiene token en el head
    def post(self, request):
        try:
            #falta validar si es admin
            cancha_id = request.data.get('id')
            cancha = Canchas.objects.get(id=cancha_id)
            cancha.delete()
            return Response({'message': 'La cancha ha sido eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)
        except Canchas.DoesNotExist:
            return Response({'message': 'La cancha no existe.'}, status=status.HTTP_404_NOT_FOUND)
        
class UpdateCancha(APIView):
    permission_classes = [IsAdmin]
    def put(self, request):
        try:
            cancha_id = request.data.get('id')
            cancha = Canchas.objects.get(id=cancha_id)
        except Canchas.DoesNotExist:
            return Response({'message': 'La cancha no existe.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CanchasSerializers(cancha, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
