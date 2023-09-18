from django.urls import path
from brands.views import BrandListView, BrandDetailView

urlpatterns = [
    path('', BrandListView.as_view(), name="brand-list"),
    path('<slug:slug>/', BrandDetailView.as_view(), name="brand-detail"),
]
