from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
app_name = "orders"


urlpatterns = [
    path("cart/", views.CartListAPIView.as_view(), name= "cart-list" ),
    path("cart/<int:pk>/", views.CartRetrieveUpdateAPIView.as_view(), name= "cart-retrieve" ),
    path("cart-item/", views.CartItemDetailListAPIView.as_view(), name= "cart-items-list" ),
    path("cart-item/<int:pk>/", views.CartItemDetailUpdateAPIView.as_view(), name= "cart-items-retrieve" ),
    path("cart-item/<int:item_pk>/customize/", views.CustomizationListAPIView.as_view(), name= "customization-list"),
    path("cart-item/<int:item_pk>/customize/<int:pk>/",
          views.CustomizationRetrieveUpdateAPIView.as_view(), name= "customization-retrive"),
    path("order-item/", views.OrderItemDetailViewApi.as_view(), name= "order-items-list" ),
    path("order/", views.OrderViewApi.as_view(), name= "order-list" ),
]
