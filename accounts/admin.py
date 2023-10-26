from django.contrib import admin
from project.settings import AUTH_USER_MODEL
from .models import User, Location
# Register your models here.

admin.site.register(User)
admin.site.register(Location)