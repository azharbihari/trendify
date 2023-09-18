from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from orders.models import Order, OrderItem, Payment
from carts.models import Cart, CartItem
from addresses.models import Address
from django.conf import settings
import razorpay
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
client.set_app_details(
    {"title": settings.APP_TITLE, "version": settings.APP_VERSION})


class CreateOrderView(View):
    def post(self, request):
        cart = Cart.objects.get(user=request.user)
        address = Address.objects.filter(
            user=request.user, is_default=True).first()
        order = Order.objects.create(user=request.user, address=address)

        for cart_item in cart.items.all():
            OrderItem.objects.create(
                order=order, product=cart_item.product, quantity=cart_item.quantity)
        cart.items.all().delete()

        return redirect('order-address', pk=order.pk)


class OrderAddressView(View):
    def get(self, request, *args, **kwargs):
        order = get_object_or_404(Order, pk=kwargs["pk"])
        addresses = Address.objects.filter(user=request.user)
        return render(request, 'orders/order_address.html', {'addresses': addresses, 'order': order})

    def post(self, request, *args, **kwargs):
        order = get_object_or_404(Order, pk=kwargs["pk"])
        address = get_object_or_404(Address, pk=request.POST.get('address'))
        order.address = address
        order.save()

        return redirect('order-payment', pk=order.pk)


@method_decorator(csrf_exempt, name='dispatch')
class OrderPaymentView(View):
    def get(self, request, *args, **kwargs):
        order = get_object_or_404(Order, pk=kwargs["pk"])

        try:
            payment = order.payment
        except Payment.DoesNotExist:
            payment = None

        if not payment:
            razorpay_order = client.order.create({
                "amount": int(order.total * 100),
                "currency": "INR",
                "receipt": str(order.pk),
            })
            payment = Payment.objects.create(
                user=request.user,
                order=order,
                razorpay_order_id=razorpay_order["id"],
                amount=order.total,
                status="Created",
            )

        razorpay_order = client.order.fetch(payment.razorpay_order_id)
        return render(request, 'orders/order_payment.html', {'order': order, 'razorpay_order': razorpay_order})

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        order = get_object_or_404(Order, pk=kwargs["pk"])
        payment = get_object_or_404(Payment, order=order)

        razorpay_payment_id = request.POST.get("razorpay_payment_id")
        razorpay_signature = request.POST.get("razorpay_signature")

        try:
            client.utility.verify_payment_signature(
                {
                    "razorpay_order_id": payment.razorpay_order_id,
                    "razorpay_payment_id": razorpay_payment_id,
                    "razorpay_signature": razorpay_signature,
                }
            )

            payment.razorpay_payment_id = razorpay_payment_id
            payment.razorpay_signature = razorpay_signature
            payment.status = "Success"
            payment.save()

            return render(
                request, "orders/payment_success.html", {
                    "order": order, "payment": payment}
            )

        except razorpay.errors.SignatureVerificationError as e:
            payment.status = "Failed"
            payment.save()

            return render(
                request, "orders/payment_failed.html", {
                    "order": order, "payment": payment}
            )
