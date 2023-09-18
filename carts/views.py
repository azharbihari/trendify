from django.views import View
from django.views.generic import ListView, DetailView
from carts.models import Cart
from carts.models import Cart, CartItem
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from products.models import Product
from django.contrib import messages


class CartListView(LoginRequiredMixin, ListView):
    model = Cart


class CartDetailView(LoginRequiredMixin, DetailView):
    model = Cart

    def get_object(self, queryset=None):
        return self.request.user.cart


class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        cart, created = Cart.objects.get_or_create(user=request.user)

        if created:
            cart.save()

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product)

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        messages.success(request, "Product added to cart successfully!")
        return redirect(request.META['HTTP_REFERER'])


class UpdateCartItemQuantityView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        quantity = request.POST.get('quantity')

        cart_item = get_object_or_404(CartItem, id=self.kwargs['pk'])
        cart_item.quantity = quantity
        cart_item.save()
        messages.success(request, "Cart item quantity updated successfully!")
        return redirect(request.META['HTTP_REFERER'])
