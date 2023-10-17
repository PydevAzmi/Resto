from django.contrib import admin
from .models import OrderItemDetail, Order, CartItemDetail, Cart, Customization, SpecialInstructions
# Register your models here.

class CustomizationInline(admin.TabularInline):
    model = Customization
    
class SpecialInstructionsInline(admin.TabularInline):
    model = SpecialInstructions

class CartItemDetailAdmin(admin.ModelAdmin):
    inlines = [
        CustomizationInline
    ]

class CartAdmin(admin.ModelAdmin):
    inlines = [
        SpecialInstructionsInline
    ]


admin.site.register(Customization)
admin.site.register(SpecialInstructions)
admin.site.register(Order)
admin.site.register(Cart,CartAdmin)
admin.site.register(OrderItemDetail)
admin.site.register(CartItemDetail,CartItemDetailAdmin)