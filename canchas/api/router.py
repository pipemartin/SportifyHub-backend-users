from django.urls import path
from canchas.api.views import CanchasResgisterView, ListCanchasView, ListCanchasDisponibleView, ListCanchasOcupadasView, TotalCanchasDisponibleView, DeleteCanchas, UpdateCancha, CanchasDisponibleDeporteView

urlpatterns = [
    path('canchas/all', ListCanchasView.as_view()),
    path('canchas/register', CanchasResgisterView.as_view()),
    path('canchas/disponibles', ListCanchasDisponibleView.as_view()),
    path('canchas/ocupadas', ListCanchasOcupadasView.as_view()),
    path('canchas/totalDisponiblesDeporte',TotalCanchasDisponibleView.as_view()),
    path('canchas/disponiblesDeporte',CanchasDisponibleDeporteView.as_view()),
    path('canchas/delete',DeleteCanchas.as_view()),
    path('canchas/update', UpdateCancha.as_view())
]