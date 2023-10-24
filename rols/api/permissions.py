from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        # Verificar si el usuario está autenticado
        if request.user.is_authenticated:
            # Verificar si el usuario tiene el rol de "Administrador"
            user = request.user
            if user and user.rol.title == "Administrador":
                return True
        return False
