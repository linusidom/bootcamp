from django.shortcuts import render, redirect
from billing.models import BillingProfile
from carts.models import Cart
from addresses.models import Address
from orders.models import Order
from addresses.forms import AddressForm
from addresses.models import Address
# Create your views here.
def address_check(request):
	if request.method == 'POST':
		form = AddressForm(request.POST)
		next_post = request.POST.get('next')
		billing_profile, bill_created = BillingProfile.objects.new_or_get(request)
		cart_obj, cart_create = Cart.objects.new_or_get(request)
		order_obj, order_create = Order.objects.new_or_get(billing_profile=billing_profile, cart_obj=cart_obj)

		address_type = request.POST.get('address_type')
		if form.is_valid():
			address = form.save(commit=False)

			address.address_type = address_type
			address.billing_profile = billing_profile
			address.save()

			if address_type == 'shipping':

				order_obj.shipping_address = address
				order_obj.save()
			else:
				order_obj.billing_address = address
				order_obj.save()
			return redirect(next_post)
	else:
		form = AddressForm()
	return redirect('carts:cart_checkout')

def address_update(request):
	if request.method == 'POST':
		form = AddressForm(request.POST)
		next_post = request.POST.get('next')

		billing_profile, bill_created = BillingProfile.objects.new_or_get(request)
		cart_obj, cart_create = Cart.objects.new_or_get(request)
		order_obj, order_create = Order.objects.new_or_get(billing_profile=billing_profile, cart_obj=cart_obj)

		address_type = request.POST.get('address_type')

		address_id = request.POST.get('address')
		address = Address.objects.get(id=address_id)
		if address_type == 'shipping':
			order_obj.shipping_address = address
			order_obj.save()
		else:
			order_obj.billing_address = address
			order_obj.save()
		return redirect(next_post)
	else:
		form = AddressForm()
	return redirect('carts:cart_checkout')


