from django.shortcuts import render

from django.views.generic import ListView, DetailView
from brands.models import Brand
from products.models import Product


class BrandListView(ListView):
    model = Brand


class BrandDetailView(DetailView):
    model = Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_list"] = Product.objects.filter(brand=self.object)
        return context
