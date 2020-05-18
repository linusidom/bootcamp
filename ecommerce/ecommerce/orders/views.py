from django.shortcuts import render, redirect
from carts.models import Cart
from orders.models import Order
from billing.models import BillingProfile
# Create your views here.
def checkout(request):
	
	cart_obj, created = Cart.objects.new_or_get(request)
	print(cart_obj)
	order_obj = None
	billing_profile = None
	if created or cart_obj.products.count() == 0:
		return redirect('carts:cart_detail', pk=cart_obj.id)
	else:
		qs = Order.objects.filter(cart=cart_obj)
		if qs:
			order_obj = qs.first()
	if request.user.is_authenticated:	
		qs = Order.objects.filter(user=request.user, cart=cart_obj)
		if qs:
			order_obj = qs.first()
		billing_profile = BillingProfile.objects.get(user=request.user)
	context = {
		'order_obj': order_obj,
		'billing_profile':billing_profile,
	}
	return render(request, 'orders/checkout_home.html', context)