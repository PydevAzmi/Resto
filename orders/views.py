from rest_framework import viewsets
from .serializers import CartItemDetailSerailizer, CartSerailizer, OrderItemDetailSerailizer, OrderSerailizer
from .models import Cart, CartItemDetail, Order, OrderItemDetail
# Create your views here.


class CartItemDetailViewSetApi(viewsets.ModelViewSet):
    queryset = CartItemDetail.objects.all()
    serializer_class= CartItemDetailSerailizer
    

class CartViewSetApi(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class= CartSerailizer


class OrderItemDetailViewSetApi(viewsets.ModelViewSet):
    queryset = OrderItemDetail.objects.all()
    serializer_class= OrderItemDetailSerailizer


class OrderViewSetApi(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class= OrderSerailizer


"""
cart_item_detail_view_set_api = CartItemDetailViewSetApi.as_view({'get': 'list'})
cart_view_set_api = CartViewSetApi.as_view({'get': 'list'})
order_item_detail_view_set_api = OrderItemDetailViewSetApi.as_view({'get': 'list'})
order_view_set_api = OrderViewSetApi.as_view({'get': 'list'})
"""
