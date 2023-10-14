from django.contrib import admin
from .models import MenuItem, ComponentChoises, Ingredient, MenuItemIngredient, Category, Favourites
# Register your models here.

class ComponentTabularInline(admin.TabularInline):
    model = ComponentChoises

class ComponentAdmin(admin.ModelAdmin):
    inlines = [
        ComponentTabularInline
    ]

class IngredientTabularInline(admin.TabularInline):
    model = MenuItemIngredient


class ItemIngredientAdmin(admin.ModelAdmin):
    inlines = [
        IngredientTabularInline
    ]

admin.site.register(ComponentChoises)
admin.site.register(Category)
admin.site.register(Favourites)
admin.site.register(MenuItemIngredient)
admin.site.register(Ingredient,ComponentAdmin)
admin.site.register(MenuItem, ItemIngredientAdmin)