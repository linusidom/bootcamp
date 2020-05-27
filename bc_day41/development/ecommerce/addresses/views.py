from django.shortcuts import render, redirect
from addresses.models import Address
from addresses.forms import AddressForm
from billing.models import BillingProfile
from orders.models import Order
from carts.models import Cart
# Create your views here.
def address_create(request):
	if request.method == 'POST':
		
		form = AddressForm(request.POST)

		# Is this a shipping or billing address????
		address_type = request.POST.get('address_type')
		print('address_type', address_type)

		billing_profile, bill_created = BillingProfile.objects.new_or_get(request)
		cart_obj, cart_created = Cart.objects.new_or_get(request)
		order_obj, order_created = Order.objects.new_or_get(billing_profile=billing_profile, cart_obj=cart_obj)

		if form.is_valid():

			address = form.save(commit=False)
			# print('Form and Address', type(form), form)
			# print('Address', type(address), address)

			address.billing_profile = billing_profile
			address.address_type = address_type
			address.save()

			# Now we have to associate to the order
			if address_type == 'shipping':
				# How do we get the order?
				order_obj.shipping_address = address
				order_obj.save()
			if address_type == 'billing':
				order_obj.billing_address = address
				order_obj.save()
			return redirect('carts:cart_checkout')
	else:
		return redirect('carts:cart_checkout')



def address_update(request):
	if request.method == 'POST':
		# Is this a shipping or billing address????
		address_type = request.POST.get('address_type')
		address_id = request.POST.get('address')
		print('address', address_id)

		address = Address.objects.get(id=address_id)

		billing_profile, bill_created = BillingProfile.objects.new_or_get(request)
		cart_obj, cart_created = Cart.objects.new_or_get(request)
		order_obj, order_created = Order.objects.new_or_get(billing_profile=billing_profile, cart_obj=cart_obj)

		
		form = AddressForm(request.POST)
		if form.is_valid():

			# Now we have to associate to the order
			if address_type == 'shipping':
				# How do we get the order?
				order_obj.shipping_address = address
				order_obj.save()
			if address_type == 'billing':
				order_obj.billing_address = address
				order_obj.save()
			return redirect('carts:cart_checkout')
	else:
		return redirect('carts:cart_checkout')


