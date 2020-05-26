from django.shortcuts import render, redirect
from carts.models import Cart
from products.models import Product
from billing.models import BillingProfile
from accounts.forms import LoginForm, GuestForm
from accounts.models import GuestEmail
from orders.models import Order
# Create your views here.

def cart_home(request):
	cart_obj, created = Cart.objects.new_or_get(request)
	context = {
		'cart_obj':cart_obj
	}	
	return render(request, 'carts/cart_home.html', context)


def cart_update(request, pk):

	next_get = request.GET.get('next')


	# Get the Product object
	product_obj = Product.objects.get(id=pk)
	print('Product ', product_obj)
	# First we have to have a cart

	cart_obj, created = Cart.objects.new_or_get(request)

	# cart_id = request.session.get('cart_id')
	# print('This is the new Cart ID', cart_id)

	# user = request.user
	# # If the cart exists we want to use that one
	# if cart_id:
	# 	cart_obj = Cart.objects.get(id=cart_id)
	# 	# Create a new cart
	# 	if user.is_authenticated and cart_obj.user is None:
	# 		# cart_obj, create = Cart.objects.get_or_create(user=user)
	# 		cart_obj.user = user
	# 		cart_obj.save()
	# else:
	# 	cart_obj = Cart.objects.create()
	# 	# print(cart_obj)
	# 	request.session['cart_id'] = cart_obj.id

	# print('This is the new Cart ID', cart_id)	
	

	# Now we can add Products to the cart

	# If the product is in the cart already
	if product_obj in cart_obj.products.all():
		cart_obj.products.remove(product_obj)
	# If it is not in the cart, we can add it to the cart
	else:
		cart_obj.products.add(product_obj)
	request.session['cart_items'] = cart_obj.products.all().count()


	return redirect(next_get)


def cart_checkout(request):

	billing_profile = None
	# guest_email_id = request.session.get('guest_email_id') #returns ID or None



	cart_obj, created = Cart.objects.new_or_get(request)
	billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
	# if request.user.is_authenticated:
	# 	billing_profile = BillingProfile.objects.filter(user=request.user)
	# elif guest_email_id:
	# 	guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
	# 	billing_profile = BillingProfile.objects.create(email=guest_email_obj)

	# Create the order Object
	if billing_profile is not None:
		# Check if an active order exists
		order_obj, created = Order.objects.new_or_get(billing_profile, cart_obj)
		
		# print('Order Obj from Checkout', order_obj)
		# order_qs = Order.objects.filter(billing_profile=billing_profile, cart=cart_obj, active=True)
		# print('Order that came back', order_qs)
		# if order_qs.count() == 1:
		# 	order_obj = order_qs.first()
		# else:
		# 	older_order_qs = Order.objects.filter(billing_profile=billing_profile, cart=cart_obj)
		# 	if older_order_qs.exists():
		# 		older_order_qs.update(active=False)
		# 	order_obj = Order.objects.create(billing_profile=billing_profile, cart=cart_obj)

	context = {
		'order_obj': order_obj,
		'cart_obj': cart_obj,
		'billing_profile':billing_profile,
		'loginForm': LoginForm,
		'guestForm': GuestForm
	}
	return render(request, 'carts/cart_checkout.html', context)



















