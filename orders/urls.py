from django.urls import path
from orders.views import CreateOrderView, OrderAddressView, OrderPaymentView

urlpatterns = [
    path('create/', CreateOrderView.as_view(), name='order-create'),
    path('<int:pk>/order-address/',
         OrderAddressView.as_view(), name='order-address'),

    path('<int:pk>/order-payment/',
         OrderPaymentView.as_view(), name='order-payment'),
]
