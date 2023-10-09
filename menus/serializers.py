from rest_framework import serializers
from .models import MenuItem, Category, Ingredient, MenuItemIngredient

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

# Ingredient Serializer
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = (
            "id", 
            'name',)

# All Menu Items Ingredients Serializers
class MenuItemIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

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
            'sale_price', 
            'ingredients',)

