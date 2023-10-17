from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from .utils import generate_code
from menus.models import MenuItem, Ingredient,MenuItemIngredient, ComponentChoises, COMPONENT_CHOICES

# Create your models here.
ORDER_STATUS = (
    ("In_Progress","In_Progress"),
    ("Submited","Submited"),
    ("Canceled","Canceled"),
    ("Delivered","Delivered"),
    )

CART_STATUS = (
    ("In_Progress","In_Progress"),
    ("Submited","Submited"),
)

class Order(models.Model):
    code = models.CharField(max_length=15, default=generate_code(15))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    received_at = models.DateTimeField(null= True, blank= True)
    is_delivery = models.BooleanField(default = True)
    total = models.DecimalField(max_digits=5, decimal_places=2, null= True, blank= True)
    tax = models.DecimalField(max_digits=5, decimal_places=2, null= True, blank= True)

    def __str__(self):
        return f"{self.user} - {self.code}"


class OrderItemDetail(models.Model):
    order = models.ForeignKey(Order, related_name="order", on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, related_name="order_item", on_delete= models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default = 1)
    
    @property
    def price(self):
        if self.item.is_sale:
            return (self.quantity) * (self.item.sale_price)
        return (self.quantity) * (self.item.price)
    
    def __str__(self):
        return f"{self.item} - {self.order}"
    

class Cart(models.Model):
    code = models.CharField(max_length=9, default=generate_code(9))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=CART_STATUS)

    @property
    def total_price(self):
        total = 0
        for item in self.objects.select_related("order").all():
            total += item.price
        return total

    def __str__(self):
        return f"{self.user} - {self.code}"
    

class CartItemDetail(models.Model):
    cart = models.ForeignKey(Cart, related_name="cart", on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, related_name ="cart_item", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default = 1)
    
    @property
    def details(self):
        text = ''
        for obj in Customization.objects.filter(cart_item = self).all():
            if obj.component and not None:
                text += f"{obj.ingredient.name} : {obj.component.type}, "
        return text
    
    @property
    def price(self):
        total = self.item.price if not self.item.is_sale else self.item.sale_price
        for obj in Customization.objects.filter(cart_item = self).all():
                if obj.component and not None:
                    total += obj.component.price
        return self.quantity * total
    
    def __str__(self):
        return f"{self.item} - {self.cart}"
    

class Customization(models.Model):
    cart_item = models.ForeignKey(CartItemDetail,related_name="cart_item_detail" , on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient,related_name='ingredient', on_delete=models.SET_NULL, null=True,blank=True)
    component = models.ForeignKey(ComponentChoises, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.cart_item}  {self.ingredient}"
    
@receiver(post_save, sender=CartItemDetail)
def create_customizations(sender, instance, created, **kwargs):
    if created and instance.item.ingredients:
        for ingredient in instance.item.ingredients.all():
            quantity = MenuItemIngredient.objects.get(ingredient = ingredient, menu_item = instance.item).quantity
            for _ in range(quantity):
                if not ingredient.is_optional:
                    default = ComponentChoises.objects.filter(ingredient=ingredient).first()
                    Customization.objects.create(cart_item=instance, ingredient=ingredient, component = default)
                else:
                    Customization.objects.create(cart_item=instance, ingredient=ingredient)
