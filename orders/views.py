from rest_framework import generics
from .serializers import (CartItemDetailSerailizer, CartSubmitSerailizer,
                          CartSerailizer, OrderItemDetailSerailizer, 
                          OrderSerailizer, CustomizationSerializer)

from .models import Cart, CartItemDetail, Order, OrderItemDetail, Customization
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CartItemDetailListAPIView(generics.ListAPIView):
    queryset = CartItemDetail.objects.all()
    serializer_class= CartItemDetailSerailizer
    

class CartListAPIView(generics.ListAPIView):
    serializer_class= CartSerailizer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = Cart.objects.filter(user = self.request.user, status ="In_Progress")
        return queryset
    
class CartRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class= CartSubmitSerailizer
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = 'pk'
    def get_queryset(self):
        queryset = Cart.objects.filter(user = self.request.user, status ="In_Progress")
        return queryset

class OrderItemDetailViewApi(generics.ListAPIView):
    queryset = OrderItemDetail.objects.all()
    serializer_class= OrderItemDetailSerailizer


class OrderViewApi(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class= OrderSerailizer

class CustomizationViewApi(generics.ListAPIView):
    queryset = Customization.objects.all()
    serializer_class= CustomizationSerializer
