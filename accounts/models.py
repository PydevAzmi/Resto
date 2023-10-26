from django.db import models
from django_countries.fields import CountryField

# Create your models here.
from django.contrib.auth.models import AbstractUser


def profile_image_path(instance, file_name):
    return f'images/users/{instance.username}/{file_name}'


class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=150)
    phone_number = models.CharField( max_length=14, null=True,blank=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True,blank=True)
    profile_image = models.ImageField(upload_to=profile_image_path, null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']

class Location(models.Model):
    country = CountryField()
    city = models.CharField(max_length=50, null=True, blank=True)
    place = models.CharField( max_length=50, null=True,blank=True)

    def __str__(self):
        return f"{self.place}, {self.city}, {self.country.name}"
