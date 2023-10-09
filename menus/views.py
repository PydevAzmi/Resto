from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import MenuItem, Category, MenuItemIngredient
from .serializers import CategorySerializer, MenuItemSerializer, MenuItemIngredientSerializer
# Create your views here.

class MenuItemsViewSet(ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemIngredientViewSet(ModelViewSet):
    queryset = MenuItemIngredient.objects.all()
    serializer_class = MenuItemIngredientSerializer