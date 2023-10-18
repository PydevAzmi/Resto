from rest_framework import generics, viewsets
from .serializers import (CartItemDetailSerailizer, CartSubmitSerailizer,
                          CartSerailizer, OrderItemDetailSerailizer, 
                          OrderSerailizer, CustomizationSerializer, SpecialInstructionsSerializer)

from .models import Cart, CartItemDetail, Order, OrderItemDetail, Customization, SpecialInstructions
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class CartItemDetailListAPIView(generics.ListAPIView):
    serializer_class= CartItemDetailSerailizer
    permission_classes = [IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        last_cart = Cart.objects.filter(user = self.request.user, status ="In_Progress").last()
        queryset = CartItemDetail.objects.filter(cart = last_cart).all()
        return queryset

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

class CustomizationAPIView(viewsets.ModelViewSet):
    serializer_class= CustomizationSerializer

    def get_queryset(self):
        last_cart = Cart.objects.filter(user=self.request.user, status="In_Progress").last()
        cart_items = CartItemDetail.objects.filter(cart = last_cart)
        queryset = Customization.objects.filter(cart_item__in = cart_items)
        return queryset
    

class SpecialInstructionsListAPIView(generics.ListAPIView):
    serializer_class = SpecialInstructionsSerializer

    def get_queryset(self):
        last_cart = Cart.objects.filter(user = self.request.user, status ="In_Progress").last()
        queryset = SpecialInstructions.objects.filter(cart =last_cart )
        return queryset