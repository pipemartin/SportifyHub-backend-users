from django.urls import path

from establecimiento.api.views import ResgisterView, ListEstablecimientoView, DeleteEstablecimiento, UpdateEstablecimiento

urlpatterns = [ 
    path('establecimiento/register', ResgisterView.as_view()),
    path('establecimiento/all', ListEstablecimientoView.as_view()),
    path('establecimiento/delete', DeleteEstablecimiento.as_view()),
    path('establecimiento/update', UpdateEstablecimiento.as_view())
]