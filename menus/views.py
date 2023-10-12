from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAdminOrReadOnly
from .models import MenuItem, Category, Ingredient
from .serializers import CategorySerializer, MenuItemSerializer, IngredientSerializer
# Create your views here.

class PermissionView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]

class MenuItemsViewSet(PermissionView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class CategoryViewSet(PermissionView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class IngredientViewSet(PermissionView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer