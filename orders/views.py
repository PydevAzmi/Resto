from rest_framework import generics
from .serializers import CartItemDetailSerailizer, CartSerailizer, OrderItemDetailSerailizer, OrderSerailizer
from .models import Cart, CartItemDetail, Order, OrderItemDetail
# Create your views here.


class CartItemDetailViewApi(generics.ListAPIView):
    queryset = CartItemDetail.objects.all()
    serializer_class= CartItemDetailSerailizer
    

class CartViewApi(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class= CartSerailizer


class OrderItemDetailViewApi(generics.ListAPIView):
    queryset = OrderItemDetail.objects.all()
    serializer_class= OrderItemDetailSerailizer


class OrderViewApi(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class= OrderSerailizer


"""
cart_item_detail_view_set_api = CartItemDetailViewSetApi.as_view({'get': 'list'})
cart_view_set_api = CartViewSetApi.as_view({'get': 'list'})
order_item_detail_view_set_api = OrderItemDetailViewSetApi.as_view({'get': 'list'})
order_view_set_api = OrderViewSetApi.as_view({'get': 'list'})
"""
