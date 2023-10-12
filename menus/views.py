from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import MenuItem, Category, Ingredient
from .serializers import CategorySerializer, MenuItemSerializer, IngredientSerializer
# Create your views here.

class MenuItemsViewSet(ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer