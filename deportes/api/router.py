from django.urls import path
from deportes.api.views import ListDeporteView, DeporteResgisterView, DeleteDeportes, UpdateDeportes

urlpatterns = [ 
    path('deportes/all', ListDeporteView.as_view()),
    path('deportes/register', DeporteResgisterView.as_view()),
    path('deportes/update',UpdateDeportes.as_view()),
    path('deportes/delete', DeleteDeportes.as_view())
]