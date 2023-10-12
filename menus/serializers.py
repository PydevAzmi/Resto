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
    components_choises = ComponentChoisesSerializer(many = True, source = 'componentchoises_set', read_only = True)
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

class MenuItemSerializer(serializers.ModelSerializer):
    category_queryset = Category.objects.all()
    ingredients_queryset = Ingredient.objects.all()

    #  Read/Write Category
    category = serializers.ChoiceField(choices = category_queryset, write_only = True)
    item_category = serializers.SerializerMethodField()
    
    #  Read/Write Ingredient
    ingredients = serializers.MultipleChoiceField(choices = ingredients_queryset ,write_only = True)
    item_ingredients = MenuItemIngredientSerializer(many = True, source = 'menuitemingredient_set', read_only = True)
    extra_data = serializers.CharField(write_only = True, required = False)
    class Meta:
        model = MenuItem
        fields = (
            'id', 
            'name', 
            'description', 
            'item_category', 
            'category', 
            'price', 
            'image',
            'is_sale', 
            'sale', 
            'sale_price', 
            'item_ingredients',
            'ingredients',
            "extra_data")
        
    def get_item_category(self, obj):
        return obj.category.name
    
    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        extra_data = validated_data.pop('extra_data')
        extra_data = extra_data.replace(" ", "").split(",")

        menu_item = MenuItem.objects.create(**validated_data)
        for i, item_ingredient in enumerate(ingredients_data):
                print(item_ingredient)
                ingredient = Ingredient.objects.get(name=item_ingredient)
                print(extra_data[i])
                # Add menu item ingredient with the correct relationship
                MenuItemIngredient.objects.create(
                    menu_item = menu_item,
                    ingredient = ingredient,
                    quantity = extra_data[i]
                )

        return menu_item
