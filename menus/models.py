from django.db import models
from project.settings import AUTH_USER_MODEL
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

COMPONENT_CHOICES = [
    ("Regular", "Regular"),
    ("Extra", "Extra"),
    ("Spicy", "Spicy"),
    ("1L", "1L"),
    ("2L", "2L"),
    ("Can", "Can"),
]


def item_image_path(instance, file_name):
    return f"images/{instance.category}/{instance.name}/{file_name}"


def ingredient_image_path(instance, file_name):
    return f"images/ingredient/{instance.ingredient}/{instance.type}/{file_name}"


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/categories/", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class ComponentChoises(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=COMPONENT_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to=ingredient_image_path, null=True, blank=True)
    ingredient = models.ForeignKey("Ingredient", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.type} - {self.price}"


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    is_optional = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class MenuItemIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    menu_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True, blank=True, default=1)

    def __str__(self):
        return f"{self.menu_item} - {self.quantity} {self.ingredient}"


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to=item_image_path, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient, through=MenuItemIngredient)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_sale = models.BooleanField(default=False)
    is_fav = models.BooleanField(default=False)
    sale = models.FloatField(default=0, validators=[MaxValueValidator(1), MinValueValidator(0)], null=True, blank=True)

    @property
    def sale_price(self):
        if self.is_sale:
            return self.price - round(float(self.price) * (self.sale))
        else:
            return None

    def __str__(self):
        return f"{self.name}"


class Favourites(models.Model):
    item = models.ForeignKey(MenuItem, related_name="fav_item", on_delete=models.CASCADE)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} Likes {self.item}"
