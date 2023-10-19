from rest_framework import generics, viewsets
from django.shortcuts import get_object_or_404
from .serializers import (
    CartItemSerailizer,CartItemDetailSerailizer , CartUpdateSerailizer,CartSerailizer, OrderItemDetailSerailizer, 
    OrderSerailizer, CustomizationSerializer, CustomizationUpdateSerializer, SpecialInstructionsSerializer)
from .models import Cart, CartItemDetail, Order, OrderItemDetail, Customization, SpecialInstructions
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class UserCartView():
    permission_classes=[IsAuthenticated, IsOwner]
    def get_queryset(self):
        # Retrieves only one list item, because the shopping cart is managed by signals to be created dynamically
        queryset=Cart.objects.filter(user=self.request.user, status="In_Progress")
        return queryset


class CartListAPIView(UserCartView, generics.ListAPIView):
    serializer_class=CartSerailizer


class CartRetrieveUpdateAPIView(UserCartView, generics.RetrieveUpdateAPIView):
    serializer_class=CartUpdateSerailizer
    lookup_field='pk'


class UserCartItemView():
    def get_queryset(self):
        last_cart=Cart.objects.filter(user=self.request.user, status="In_Progress").last()
        queryset=CartItemDetail.objects.filter(cart=last_cart).all()
        return queryset


class CartItemDetailListAPIView(UserCartItemView, UserCartView, generics.ListAPIView):
    serializer_class=CartItemSerailizer


class CartItemDetailUpdateAPIView(UserCartItemView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class=CartItemDetailSerailizer
    lookup_field="pk"


class CustomizationListAPIView(generics.ListAPIView):
    serializer_class=CustomizationSerializer

    def get_queryset(self):
        pk=self.kwargs['item_pk']
        last_cart=get_object_or_404(Cart , user=self.request.user, status="In_Progress")
        cart_item=get_object_or_404(CartItemDetail, cart=last_cart, id=pk)
        queryset=Customization.objects.filter(cart_item=cart_item)
        return queryset
    
class CustomizationRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class=CustomizationUpdateSerializer
    lookup_field="pk"

    def get_queryset(self):
        item_pk=self.kwargs['item_pk']
        pk=self.kwargs['pk']
        last_cart=get_object_or_404(Cart , user=self.request.user, status="In_Progress")
        cart_item=get_object_or_404(CartItemDetail, cart=last_cart, id=item_pk)
        queryset=Customization.objects.filter(cart_item=cart_item, pk=pk)
        return queryset
    
    def get_serializer_context(self):
        context=super().get_serializer_context()
        customization_instance=self.get_object()
        context.update({"customization_instance": customization_instance})
        return context
    
class SpecialInstructionsListAPIView(generics.ListAPIView):
    serializer_class=SpecialInstructionsSerializer

    def get_queryset(self):
        last_cart=Cart.objects.filter(user=self.request.user, status="In_Progress").last()
        queryset=SpecialInstructions.objects.filter(cart=last_cart )
        return queryset


class OrderItemDetailViewApi(generics.ListAPIView):
    queryset=OrderItemDetail.objects.all()
    serializer_class=OrderItemDetailSerailizer


class OrderViewApi(generics.ListAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerailizer