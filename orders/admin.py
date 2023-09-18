from django.contrib import admin
from orders.models import Order, OrderItem, Payment

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
