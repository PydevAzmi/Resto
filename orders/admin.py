from django.contrib import admin
from .models import OrderItemDetail, Order, CartItemDetail, Cart, Customization
# Register your models here.


admin.site.register(Customization)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(OrderItemDetail)
admin.site.register(CartItemDetail)