from django.db import models
from django.utils.text import slugify
from products.models import Product
from django.contrib.auth import get_user_model
from decimal import Decimal

User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}'s Cart"

    @property
    def item_count(self):
        return self.items.count()

    @property
    def subtotal(self):
        return sum(item.total for item in self.items.all())

    @property
    def tax(self):
        return self.subtotal * Decimal('0.10')  # 10% tax rate

    @property
    def total(self):
        return self.subtotal + self.tax


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.cart}"
