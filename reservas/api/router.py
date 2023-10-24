from django.urls import path
from reservas.api.views import ListReservaView, ReservaResgisterView, DeleteReserva, UpdateReserva

urlpatterns = [
    path('reservas/all', ListReservaView.as_view()),
    path('reservas/register', ReservaResgisterView.as_view()),
    path('reservas/update', UpdateReserva.as_view()),
    path('reservas/delete', DeleteReserva.as_view()),
]