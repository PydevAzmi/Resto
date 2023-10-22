from django.urls import path, include
app_name = "accounts"

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
