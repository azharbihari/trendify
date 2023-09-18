from django.shortcuts import render

from django.views.generic import ListView, DetailView
from products.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
