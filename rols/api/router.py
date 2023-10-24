from rest_framework.routers import DefaultRouter
from rols.api.views import RolApiViewSet

router_rols = DefaultRouter()

router_rols.register(prefix='rols', basename='rols', viewset=RolApiViewSet)