from rest_framework import serializers
from .models import MenuItem, Category, Ingredient, MenuItemIngredient, ComponentChoises

# Categories Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =(
            "id",
            "name",
            "image")

# Category Serializer for Each Item
class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id", 
            'name',)
        
class ComponentChoisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentChoises
        fields = (
            "id", 
            'name',
            'type',
            'price',
            'image',)
        

# Ingredient Serializer
class IngredientSerializer(serializers.ModelSerializer):
    components_choises = ComponentChoisesSerializer(many=True, source='componentchoises_set')
    class Meta:
        model = Ingredient
        fields = (
            'id', 
            'name',
            'components_choises',)
        
class IngredientViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name',)
        
# All Menu Items Ingredients Serializers
class MenuItemIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientViewSerializer()

    class Meta:
        model = MenuItemIngredient
        fields = (
            "id", 
            'ingredient', 
            'quantity',)

# Items With All Information
class MenuItemSerializer(serializers.ModelSerializer):
    category = ItemCategorySerializer()
    ingredients = MenuItemIngredientSerializer(many=True, source='menuitemingredient_set')

    class Meta:
        model = MenuItem
        fields = (
            'id', 
            'name', 
            'description', 
            'category', 
            'price', 
            'image',
            'is_sale', 
            'sale', 
            'sale_price', 
            'ingredients',)

