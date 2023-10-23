from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from project.settings import AUTH_USER_MODEL
from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in
from djoser.signals import user_registered
from .utils import generate_code, cart_generate_code
from menus.models import MenuItem, Ingredient, MenuItemIngredient, ComponentChoises, COMPONENT_CHOICES

# Create your models here.
ORDER_STATUS = (
    ("In_Progress", "In_Progress"),
    ("Submited", "Submited"),
    ("Canceled", "Canceled"),
    ("Delivered", "Delivered"),
)

CART_STATUS = (
    ("In_Progress", "In_Progress"),
    ("Submited", "Submited"),
)


class Order(models.Model):
    code = models.CharField(max_length=20, default=cart_generate_code)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', related_name="order_cart", on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    received_at = models.DateTimeField(null=True, blank=True)
    is_delivery = models.BooleanField(default=True)
    total = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    tax = models.FloatField(default=0, validators=[MaxValueValidator(1), MinValueValidator(0)], null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.code} {self.status}"


class OrderItemDetail(models.Model):
    order = models.ForeignKey(Order, related_name="order", on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, related_name="order_item", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item} by {self.order.user}"


@receiver(post_save, sender=Order)
def create_order_items(sender, instance, created, **kwargs):
    if created:
        for order in instance.cart.cart.all():
            OrderItemDetail.objects.create(order=instance, item=order.item, quantity=order.quantity)


class Cart(models.Model):
    code = models.CharField(max_length=10, default=generate_code)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=CART_STATUS)

    @property
    def total_price(self):
        total = 0
        for item in self.cart.all():
            total += item.price
        return total

    def __str__(self):
        return f"{self.user} - {self.code} - {self.status}"


@receiver(user_logged_in, sender=get_user_model())
def user_logged_in_handler(sender, request, user, **kwargs):
    if not Cart.objects.filter(user=user, status='In_Progress').exists():
        Cart.objects.create(user=user, status='In_Progress')

@receiver(user_registered)
def user_registered_handler(user, request, **kwargs):
    print("Signal handler called for user registration.")
    if not Cart.objects.filter(user=user, status='In_Progress').exists():
        Cart.objects.create(user=user, status='In_Progress')

@receiver(post_save, sender=Cart)
def create_new_cart_order_on_submit(sender, instance, created, **kwargs):
    if instance.status == 'Submited':
        Cart.objects.create(user=instance.user, status='In_Progress')
        Order.objects.create(
            user=instance.user,
            status='In_Progress',
            cart=instance,
            total=instance.total_price,
            tax=0.20,
        )


class CartItemDetail(models.Model):
    cart = models.ForeignKey(Cart, related_name="cart", on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, related_name="cart_item", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def details(self):
        text = ''
        for obj in Customization.objects.filter(cart_item=self).all():
            if obj.component and not None:
                text += f"({obj.ingredient.name} : {obj.component.type}), "
        return text

    @property
    def price(self):
        total = self.item.price if not self.item.is_sale else self.item.sale_price
        for obj in Customization.objects.filter(cart_item=self).all():
            if obj.component and not None:
                total += obj.component.price
        return self.quantity * total

    def __str__(self):
        return f"{self.item} - {self.cart}"


class Customization(models.Model):
    cart_item = models.ForeignKey(CartItemDetail, related_name="cart_item_detail", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, related_name='ingredient', on_delete=models.SET_NULL, null=True, blank=True)
    component = models.ForeignKey(ComponentChoises, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.cart_item}  {self.ingredient}"


@receiver(post_save, sender=CartItemDetail)
def create_customizations(sender, instance, created, **kwargs):
    if created and instance.item.ingredients:
        for ingredient in instance.item.ingredients.all():
            quantity = MenuItemIngredient.objects.get(ingredient=ingredient, menu_item=instance.item).quantity
            for _ in range(quantity):
                if not ingredient.is_optional:
                    default = ComponentChoises.objects.filter(ingredient=ingredient).first()
                    Customization.objects.create(cart_item=instance, ingredient=ingredient, component=default)
                else:
                    Customization.objects.create(cart_item=instance, ingredient=ingredient)


class SpecialInstructions(models.Model):
    instraction = models.CharField(max_length=100, null=True, blank=True)
    save_for_future = models.BooleanField(default=False, null=True, blank=True)
    ketchup = models.BooleanField(default=False, null=True, blank=True)
    cutlery = models.BooleanField(default=False, null=True, blank=True)
    cart = models.ForeignKey(Cart, related_name="cart_instructions", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cart} instraction"
