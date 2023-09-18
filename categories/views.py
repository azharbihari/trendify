from django.shortcuts import render
from django.views.generic import ListView, DetailView
from categories.models import Category
from products.models import Product


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_list"] = Product.objects.filter(category=self.object)
        return context
