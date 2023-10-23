from djoser.views import UserViewSet
from .serializers import UserCreateSerializer
# Create your views here.
class CustomUserViewSet(UserViewSet):
    serializer_class = UserCreateSerializer

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)