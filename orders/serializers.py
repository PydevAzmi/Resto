from rest_framework import serializers
from .models import Cart, CartItemDetail, Order, OrderItemDetail, Customization
from menus.models import MenuItem, MenuItemIngredient
from menus.serializers import ComponentChoisesSerializer

class CustomizationSerializer(serializers.ModelSerializer):
    component = ComponentChoisesSerializer()
    class Meta:
        model = Customization
        fields = (
            'component',
        )

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
        
class CartSerailizer(serializers.ModelSerializer):
    cart_items = CartItemDetailSerailizer(many = True, source="cart", read_only = True) 
    class Meta:
        model = Cart
        fields = (
            "id",
            "user",
            "status",
            "total_price",
            "code",
            "cart_items"
            )
        
class CartSubmitSerailizer(serializers.ModelSerializer):
    cart_items = CartItemDetailSerailizer(many = True, source="cart", read_only = True) 
    class Meta:
        model = Cart
        fields = (
            "status",
            "cart_items",
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