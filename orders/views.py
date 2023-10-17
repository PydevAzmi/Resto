from rest_framework import generics
from .serializers import CartItemDetailSerailizer, CartSerailizer, OrderItemDetailSerailizer, OrderSerailizer, CustomizationSerializer
from .models import Cart, CartItemDetail, Order, OrderItemDetail, Customization
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

class CustomizationViewApi(generics.ListAPIView):
    queryset = Customization.objects.all()
    serializer_class= CustomizationSerializer
