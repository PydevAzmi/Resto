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
    components_choises = ComponentChoisesSerializer(many=True,source='componentchoises_set', read_only =True)
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
        
# Menu Items Ingredients Serializers
class MenuItemIngredientSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = MenuItemIngredient
        fields = (
            'name', 
            'quantity',)
        
    def get_name(self, obj):
        return obj.ingredient.name

# Items With All Information
class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    ingredients = MenuItemIngredientSerializer(many=True, source='menuitemingredient_set', read_only= True)

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
        
    def get_category(self, obj):
        return obj.category.name

