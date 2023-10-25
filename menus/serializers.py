from rest_framework import serializers
from django.contrib.auth.models import AnonymousUser
from .models import MenuItem, Category, Ingredient, MenuItemIngredient, ComponentChoises, Favourites

# Categories Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =(
            "id",
            "name",
            "image",)

class ComponentChoisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentChoises
        fields = (
            "id", 
            'name',
            'type',
            'price',
            'image',)
        
class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentChoises
        fields = (
            "id", 
            'ingredient',
            'name',
            'type',
            'price',
            'image',
           )     

# Ingredient Serializer
class IngredientSerializer(serializers.ModelSerializer):
    components_choises = ComponentChoisesSerializer(many = True, source = 'componentchoises_set', read_only = True)
    class Meta:
        model = Ingredient
        fields = (
            'id', 
            'name',
            'is_optional',
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
    quantity_list = serializers.CharField(write_only = True, required = False)

    is_fav = serializers.SerializerMethodField()

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
            'is_fav', 
            'item_ingredients',
            'ingredients',
            "quantity_list",)
        
    def get_item_category(self, obj):
        return obj.category.name
    
    def get_is_fav(self, obj):
        user = self.context['request'].user 
        if not isinstance(user, AnonymousUser):
            if Favourites.objects.filter(user=user, item = obj).exists():
                return True
        return False
    

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        quantity_list = validated_data.pop('quantity_list', len(ingredients_data)*"1,") 
        quantity_list = quantity_list.replace(" ", "").split(",")

        menu_item = MenuItem.objects.create(**validated_data)
        for i, item_ingredient in enumerate(ingredients_data):
                ingredient = Ingredient.objects.get(name=item_ingredient)
                # Add menu item ingredient with the correct relationship
                MenuItemIngredient.objects.create(
                    menu_item = menu_item,
                    ingredient = ingredient,
                    quantity =  1 if i >= len(quantity_list) else int(quantity_list[i])
                )
        return menu_item
    

    def update(self, instance, validated_data):
        if 'ingredients' in validated_data:
            ingredients_data = validated_data.pop('ingredients')
            # clean the quantity list
            quantity_list = validated_data.pop('quantity_list', len(ingredients_data)*"1,")
            quantity_list = quantity_list.replace(" ", "").split(",")

            if not self.partial:
                MenuItemIngredient.objects.filter(menu_item = instance).all().delete()
                for i, item_ingredient in enumerate(ingredients_data):
                    ingredient = Ingredient.objects.get(name=item_ingredient)
                    MenuItemIngredient.objects.create(
                        menu_item = instance,
                        ingredient = ingredient,
                        quantity =  1 if i >= len(quantity_list) else int(quantity_list[i])
                    )
            else:
                for i, item_ingredient in enumerate(ingredients_data):
                    ingredient = Ingredient.objects.get(name=item_ingredient)
                    menu_item_ingredient, created = MenuItemIngredient.objects.get_or_create(
                        menu_item = instance,
                        ingredient = ingredient)
                    
                    menu_item_ingredient.quantity =  1 if i >= len(quantity_list) else int(quantity_list[i])
                    menu_item_ingredient.save()
                    
        return super().update(instance, validated_data)
    
class FavouriteSerializer(serializers.ModelSerializer):
    item_name = serializers.SerializerMethodField()
    class Meta:
        model = Favourites
        fields = ("pk","item","item_name")
        
    def get_item_name (self, obj):
        return obj.item.name