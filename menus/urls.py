from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
app_name = "menus"

router = DefaultRouter()
router.register(r"items", views.MenuItemsViewSet, basename="Menu_Items")
router.register(r"categories", views.CategoryViewSet, basename="Menu_Categories")
router.register(r"ingredients", views.IngredientViewSet, basename="Ingredient")
router.register(r"componnents", views.ComponnentApiView, basename="Components")


urlpatterns = [
     path("", include(router.urls)),
     path("favorites/", views.FavouriteListCreateAPI, name="favorites"),
     path("favorites/<int:pk>", views.FavouriteRetrieveDestroyAPI, name="favorites-instance"),
]
