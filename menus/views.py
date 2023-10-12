from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .permissions import IsAdminOrReadOnly
from .models import MenuItem, Category, Ingredient
from .serializers import CategorySerializer, MenuItemSerializer, IngredientSerializer
# Create your views here.

class PermissionView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

class MenuItemsViewSet(PermissionView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filterset_fields = ['category']
    search_fields = ['name', 'description']
    ordering_fields = ['price','is_sale']

class CategoryViewSet(PermissionView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class IngredientViewSet(PermissionView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer