from django.urls import path, include
from . import views
app_name = "orders"

urlpatterns = [
    path("cart-item/", views.CartItemDetailListAPIView.as_view(), name= "cart-items-list" ),
    path("cart/", views.CartListAPIView.as_view(), name= "cart-list" ),
    path("cart/<int:pk>", views.CartRetrieveUpdateAPIView.as_view(), name= "cart-retrieve" ),

    path("order-item/", views.OrderItemDetailViewApi.as_view(), name= "order-items-list" ),
    path("order/", views.OrderViewApi.as_view(), name= "order-list" ),
    path("custom/", views.CustomizationViewApi.as_view(), name= "customization-list" ),
]
