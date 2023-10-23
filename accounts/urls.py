from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


app_name = "accounts"

router = DefaultRouter()
router.register(r"users", views.CustomUserViewSet, basename="users")

urlpatterns = [
    #path('', include(router.urls)), #If You Wants To Hide The Users From Admins
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),

]
