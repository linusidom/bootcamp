from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from carts.models import Cart
from billing.models import BillingProfile
from accounts.forms import LoginForm, GuestForm
from accounts.models import GuestEmail
from orders.models import Order
# Create your views here.
def cart_home(request):
	# user = request.user
	# cart_id = request.session.get('cart_id')
	# if cart_id:
	# 	qs = Cart.objects.get(id=cart_id)
	# 	if qs:
	# 		cart_obj = qs
	# else:
	# 	# Create a Cart
	# 	if user.is_authenticated:
	# 		cart_obj, created = Cart.objects.get_or_create(user=user)
	# 		request.session['cart_id'] = cart_obj.id
	# 	else:
	# 		cart_obj = Cart.objects.create()
	# 		request.session['cart_id'] = cart_obj.id
	
	cart_obj, created = Cart.objects.new_or_get(request)
	context = {
		'cart_obj':cart_obj
	}
	return render(request, 'carts/cart_home.html', context)

def cart_update(request, pk):
	# What if I want to re-use an existing cart?
	# user = request.user
	# cart_id = request.session.get('cart_id')
	# if cart_id:
	# 	qs = Cart.objects.get(id=cart_id)
	# 	if qs:
	# 		cart_obj = qs
	# else:
	# 	# Create a Cart
	# 	if user.is_authenticated:
	# 		cart_obj, created = Cart.objects.get_or_create(user=user)
	# 		request.session['cart_id'] = cart_obj.id
	# 	else:
	# 		cart_obj = Cart.objects.create()
	# 		request.session['cart_id'] = cart_obj.id

	cart_obj, created = Cart.objects.new_or_get(request)

	# Now once we've gotten our Cart we can add the Product
	# Get the Product
	product_obj = get_object_or_404(Product, pk=pk) # Product.objects.get(pk=pk)
	

	# If the product is in the cart we want to remove it
	# Or if not in the cart we want to add it
	if product_obj in cart_obj.products.all():
		cart_obj.products.remove(product_obj)
	else:
		cart_obj.products.add(product_obj)
	product_list = Product.objects.all()
	request.session['cart_items'] = cart_obj.products.all().count()
	
	# We want to pass our cart ID back to the product page
	# return redirect('products:product_list')
	context = {
		'cart_obj':cart_obj,
		'product_list':product_list
	}

	return render(request, 'products/product_list.html', context)





def checkout(request):
	billing_profile = None
	login_form = LoginForm()
	guest_form = GuestForm()
	guest_email_id = request.session.get('guest_email_id')


	cart_obj, created = Cart.objects.new_or_get(request)
	user = request.user
	# if not billing_profile:
	if user.is_authenticated:
		billing_profile = BillingProfile.objects.get(user=user)
		print('Billing Profile',billing_profile)
	elif guest_email_id is not None:
		guestEmail = GuestEmail.objects.get(id=guest_email_id)
		billing_profile, bill_created = BillingProfile.objects.get_or_create(email=guestEmail)

	if billing_profile is not None:
		# Create the order with the billing Profile and the cart
		order_qs = Order.objects.filter(billing_profile=billing_profile, cart=cart_obj, active=True)
		if order_qs.count() == 1:
			order_obj = order_qs.first()
		else:
			older_order_qs = Order.objects.filter(billing_profile=billing_profile, cart=cart_obj, active=True)
			if older_order_qs.exists():
				older_order_qs.update(active=False)
			order_obj = Order.objects.create(billing_profile=billing_profile, cart=cart_obj)

	context = {
		'billing_profile': billing_profile,
		'loginForm':login_form,
		'guestForm':guest_form,
		'order_obj':order_obj,

	}

	return render(request, 'carts/checkout.html', context)



















