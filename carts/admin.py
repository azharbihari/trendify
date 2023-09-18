from django.contrib import admin
from carts.models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):
    pass


class CartItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cart)
admin.site.register(CartItem)
