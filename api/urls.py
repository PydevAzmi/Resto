from django.urls import path, include

app_name = "api"

urlpatterns = [
    path("menu/", include("menus.urls", namespace="menus")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("reservations/", include("reservations.urls", namespace="reservations")),
]
