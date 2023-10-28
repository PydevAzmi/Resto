from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
    path("", views.ReservationListCreateAPIView.as_view(), name = "Reservation-list-create"),    
    path("branch/", views.BranchListCreateAPIView.as_view(), name = "Branch-list-create"),    
]
