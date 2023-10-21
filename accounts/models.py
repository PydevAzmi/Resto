from django.db import models

# Create your models here.
from django.contrib.auth.models import  AbstractUser


def profile_image_path(instance, file_name):
    return f"images/users/{instance.username}/{file_name}"


class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField( max_length=14, null=True,blank=True)
    location = models.ForeignKey("Location", on_delete=models.CASCADE, null=True,blank=True)
    profile_image = models.ImageField(upload_to=profile_image_path, null=True,blank=True)


class Location(models.Model):
    place = models.CharField( max_length=50, null=True,blank=True)