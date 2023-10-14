from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
app_name = "orders"

router = DefaultRouter()
router.register(r"cart",views.CartViewSetApi ,basename="cart" )
router.register(r"cart_item",views.CartItemDetailViewSetApi ,basename="cart_item" )
router.register(r"order",views.OrderViewSetApi ,basename="order" )
router.register(r"order_item",views.OrderItemDetailViewSetApi ,basename="order_item" )

urlpatterns = [
    path("", include(router.urls)),
]
