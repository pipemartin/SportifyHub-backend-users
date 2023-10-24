from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from reservas.api.serializers import ReservasSerializers
from reservas.models import Reservas

class ReservaResgisterView(APIView):
    def post(self, request):
        #validando data del request que llegue bien
        serializer = ReservasSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListReservaView(generics.ListAPIView):
    #valida si tiene token en el head
    def get(self, request):
        qs = Reservas.objects.all()
        serializer = ReservasSerializers(qs,many=True)
        return Response(serializer.data)
    
class DeleteReserva(APIView):
    #valida si tiene token en el head
    def post(self, request):
        try:
            #falta validar si es admin
            reserva_id = request.data.get('id')
            reserva = Reservas.objects.get(id=reserva_id)
            reserva.delete()
            return Response({'message': 'La reserva ha sido eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)
        except Reservas.DoesNotExist:
            return Response({'message': 'La reserva no existe.'}, status=status.HTTP_404_NOT_FOUND)
        
class UpdateReserva(APIView):
    def put(self, request):
        try:
            reserva_id = request.data.get('id')
            reserva = Reservas.objects.get(id=reserva_id)
        except Reservas.DoesNotExist:
            return Response({'message': 'La reserva no existe.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReservasSerializers(reserva, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)