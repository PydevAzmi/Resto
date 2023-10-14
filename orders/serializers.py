from rest_framework import serializers
from .models import Cart, CartItemDetail, Order, OrderItemDetail


class CartItemDetailSerailizer(serializers.ModelSerializer):
    class Meta:
        model = CartItemDetail
        fields = (
            "cart",
            "item",
            "quantity",
            "price",
            )

class CartSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = (
            "user",
            "status",
            "total_price",
            "code",
            )

class OrderItemDetailSerailizer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemDetail
        fields = (
            "order",
            "item",
            "price",
            "quantity",
            )

class OrderSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "code",
            "user",
            "status",
            "created_at",
            "received_at",
            "is_delivery",
            "total",
            "tax",
            )