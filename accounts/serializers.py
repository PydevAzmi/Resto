from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.signals import user_logged_in

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            'id',
            'email',
            'phone_number',
            'username',
            'password',
            )


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['is_super_user'] = user.is_superuser
        token['email'] = user.email

        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # sends Django's user_logged_in signal
        user_logged_in.send(sender=self.user.__class__, request=self.context['request'], user=self.user)
        return data