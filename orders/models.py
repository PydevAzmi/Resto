from django.db import models
from django.contrib.auth.models import User
from .utils import generate_code
from menus.models import MenuItem

# Create your models here.
ORDER_STATUS = (
    ("In_Progress","In_Progress"),
    ("Submited","Submited"),
    ("Completed","Completed"),
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
        for item in self.objects.select_related("order").item:
            total += item.price
        return total

    def __str__(self):
        return f"{self.user} - {self.code}"
    

class CartItemDetail(models.Model):
    cart = models.ForeignKey(Cart, related_name="cart", on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, related_name ="cart_item", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default = 1)

    @property
    def price(self):
        if self.item.is_sale:
            return (self.quantity) * (self.item.sale_price)
        return (self.quantity) * (self.item.price)
    
    def __str__(self):
        return f"{self.item} - {self.cart}"