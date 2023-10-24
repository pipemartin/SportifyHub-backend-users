from rest_framework.viewsets import ModelViewSet
from rols.models import Rol
from rols.api.serializers import RolsSerializer
from rols.api.permissions import IsAdmin

class RolApiViewSet(ModelViewSet):
    # permisos
    permission_classes = [IsAdmin]
    serializer_class = RolsSerializer
    queryset = Rol.objects.filter()