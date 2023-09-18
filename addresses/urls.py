from django.urls import path
from addresses.views import AddressCreateView, AddressUpdateView, AddressListView, AddressDeleteView, DefaultAddressView

urlpatterns = [
    path("", AddressListView.as_view(), name="address-list"),
    path('create/', AddressCreateView.as_view(), name='address-create'),
    path('<int:pk>/update/', AddressUpdateView.as_view(), name='address-update'),
    path('<int:pk>/delete/', AddressDeleteView.as_view(), name='address-delete'),
    path('<int:pk>/default/', DefaultAddressView.as_view(), name='address-default'),
]
