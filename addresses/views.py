from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from addresses.models import Address
from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View


class AddressListView(LoginRequiredMixin, ListView):
    model = Address
    paginate_by = 10


class AddressCreateView(LoginRequiredMixin, CreateView):
    model = Address
    success_url = reverse_lazy('address-list')
    fields = ['name', 'mobile', 'street', 'city', 'state', 'postal_code',
              'country', 'address_type']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Add Address'
        return context


class AddressDeleteView(LoginRequiredMixin, DeleteView):
    model = Address
    success_url = reverse_lazy("address-list")


class AddressUpdateView(LoginRequiredMixin, UpdateView):
    model = Address
    success_url = reverse_lazy('address-list')
    fields = ['name', 'mobile', 'street', 'city', 'state', 'postal_code',
              'country', 'address_type', 'is_default']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Edit Address'
        return context


class DefaultAddressView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = self.request.user

        address = get_object_or_404(Address, pk=self.kwargs["pk"], user=user)

        Address.objects.filter(
            user=user, is_default=True).update(is_default=False)

        address.is_default = True
        address.save()

        return redirect("address-list")
