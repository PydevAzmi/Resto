from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, mixins
from .permissions import IsAdminOrReadOnly, IsMine
from .models import MenuItem, Category, Ingredient, Favourites, ComponentChoises
from .serializers import CategorySerializer, MenuItemSerializer, IngredientSerializer, FavouriteSerializer, ComponentSerializer
# Create your views here.

class PermissionView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']

class MenuItemsViewSet(PermissionView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filterset_fields = ['category']
    search_fields = ['name', 'description']
    ordering_fields = ['is_fav', 'price', 'is_sale']

class CategoryViewSet(PermissionView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class IngredientViewSet(PermissionView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class FavouriteListCreateAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    permission_classes = [IsMine,]

    serializer_class = FavouriteSerializer
    lookup_field = "pk"
    
    def get_queryset(self):
        queryset = Favourites.objects.filter(user = self.request.user)
        return queryset
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        instance = serializer.validated_data
        instance["user"] = self.request.user
        serializer.save()
        return super().perform_create(serializer)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

        
FavouriteListCreateAPI = FavouriteListCreateAPIView.as_view()

class FavouriteRetrieveDestroyAPIView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    permission_classes = [IsMine,]
    serializer_class = FavouriteSerializer
    lookup_field = "pk"

    def get_queryset(self):
        queryset = Favourites.objects.filter(user = self.request.user)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
FavouriteRetrieveDestroyAPI = FavouriteRetrieveDestroyAPIView.as_view()


class ComponnentApiView(PermissionView):
    queryset = ComponentChoises.objects.all()
    serializer_class= ComponentSerializer
    filterset_fields = ['ingredient']