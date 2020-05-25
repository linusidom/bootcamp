from django.shortcuts import render, redirect
from carts.models import Cart
from products.models import Product
from billing.models import BillingProfile
from orders.models import Order
from addresses.models import Address
from addresses.forms import AddressForm
from accounts.forms import LoginForm, GuestForm
from accounts.models import GuestEmail

# Create your views here.

def cart_home(request):
	cart_obj, created = Cart.objects.new_or_get(request)
	context = {
		'cart_obj':cart_obj
	}
	return render(request, 'carts/cart_home.html', context)


def cart_update(request, pk):
	prod_obj = Product.objects.get(pk=pk)
	next_get = request.GET.get('next')
	next_post = request.POST.get('next')
	redirect_to = next_get or next_post
	cart_obj, created = Cart.objects.new_or_get(request)
	
	if prod_obj in cart_obj.products.all():
		cart_obj.products.remove(prod_obj)
	else:
		cart_obj.products.add(prod_obj)
	request.session['cart_items'] = cart_obj.products.all().count()
	context = {
		'cart_obj':cart_obj
	}
	return redirect(redirect_to)

def cart_checkout(request):

	loginForm = LoginForm()
	guestForm = GuestForm()
	addressForm = AddressForm()
	
	cart_obj, cart_created = Cart.objects.new_or_get(request)
	billing_profile, bill_created = BillingProfile.objects.new_or_get(request)

	if billing_profile is not None:
		order_obj, order_created = Order.objects.new_or_get(billing_profile=billing_profile, cart_obj=cart_obj)

	# if order_obj.check_done():
	# 	return redirect('carts:cart_success')

	context = {
		'order_obj':order_obj,
		'loginForm': loginForm,
		'guestForm': guestForm,
		'addressForm':addressForm,
		'billing_profile':billing_profile,
	}
	return render(request, 'carts/cart_checkout.html', context)
 

def cart_success(request):
	cart_obj, cart_created = Cart.objects.new_or_get(request)
	billing_profile, bill_created = BillingProfile.objects.new_or_get(request)
	order_obj, order_created = Order.objects.new_or_get(billing_profile=billing_profile, cart_obj=cart_obj)
	
	is_done = order_obj.check_done()
	if is_done:
		order_obj.mark_paid()
		del request.session['cart_id']
		del request.session['cart_items']
		context = {
			'order_obj':order_obj
		}
		return render(request,'carts/cart_succes.html', context)

