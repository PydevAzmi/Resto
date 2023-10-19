from rest_framework import serializers
from .models import Cart, CartItemDetail, Order, OrderItemDetail, Customization, SpecialInstructions
from menus.models import MenuItem, MenuItemIngredient
from menus.serializers import ComponentChoisesSerializer
from django.shortcuts import get_object_or_404
class CustomizationSerializer(serializers.ModelSerializer):
    component = ComponentChoisesSerializer(read_only = True)
    ingredient = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Customization
        fields = (
            'id',
            'ingredient',
            'component',
        )
    def get_ingredient(self, obj):
        return obj.ingredient.name
    
class MenuItemIngredientSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    is_optional = serializers.SerializerMethodField()
    #components_choises = ComponentChoisesSerializer(many = True, source = 'ingredient.componentchoises_set')
    class Meta:
        model = MenuItemIngredient
        fields = (
            'name', 
            'quantity',
            'is_optional',
            )
        
    def get_name(self, obj):
        return obj.ingredient.name
    
    def get_is_optional(self, obj):
        return obj.ingredient.is_optional

class ItemSerializer(serializers.ModelSerializer):
    Ingredients = MenuItemIngredientSerializer(many = True, source = 'menuitemingredient_set', read_only = True)
    class Meta:
        model = MenuItem
        fields = (
            "name",
            "Ingredients",
            )

class CartItemDetailSerailizer(serializers.ModelSerializer):
    item = ItemSerializer()
    class Meta:
        model = CartItemDetail
        fields = (
            "item",
            "quantity",
            "price",
            "details",
            )
class SpecialInstructionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialInstructions
        fields = (
            'id',
            'instraction',
            'save_for_future',
            'ketchup',
            'cutlery',)
        
class CartSerailizer(serializers.ModelSerializer):
    cart_items = CartItemDetailSerailizer(many = True, source="cart", read_only = True) 
    cart_instructions = SpecialInstructionsSerializer(many = True, read_only = True)
    class Meta:
        model = Cart
        fields = (
            "id",
            "user",
            "status",
            "total_price",
            "code",
            "cart_items",
            'cart_instructions'
            )
        
class CartUpdateSerailizer(serializers.ModelSerializer):
    queryset = MenuItem.objects.all()
    cart_items = CartItemDetailSerailizer(many = True, source="cart", read_only = True)
    item = serializers.ChoiceField(choices=queryset, write_only = True)
    quantity = serializers.IntegerField(write_only = True, default= 1)
    cart_instructions = SpecialInstructionsSerializer(many = True, read_only = True)
    class Meta:
        model = Cart
        fields = (
            "status",
            "cart_items",
            "item",
            "cart_instructions",
            "quantity"
        )

    # Only Accept Partial Update
    def update(self, instance, validated_data):
        if 'item' in validated_data:
            item_name = validated_data['item']
            item = get_object_or_404(MenuItem, name = item_name)
            if self.partial:
                quantity = 1 if 'quantity' not in validated_data else validated_data['quantity']
                CartItemDetail.objects.create(cart=instance, item=item, quantity=quantity)
        return super().update(instance, validated_data)
        
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