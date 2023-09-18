from django.urls import path
from carts.views import CartListView, CartDetailView, AddToCartView, UpdateCartItemQuantityView

urlpatterns = [

    path('', CartDetailView.as_view(), name="cart-detail"),
    path('add-to-cart/<slug:slug>', AddToCartView.as_view(), name="add-to-cart"),
    path('update-cart-item-quantity/<int:pk>',
         UpdateCartItemQuantityView.as_view(), name="update-cart-item-quantity"),

]
