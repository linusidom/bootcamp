from django.shortcuts import render, get_object_or_404, redirect
from carts.models import Cart
from billing.models import BillingProfile
from products.models import Product
from accounts.forms import GuestForm, LoginForm
from accounts.models import GuestEmail
from addresses.forms import AddressForm

# Create your views here.
def cart_home(request):
	cart_obj, created = Cart.objects.new_or_get(request)
	context = {
		'cart_obj':cart_obj,
	}
	return render(request, 'carts/cart_home.html', context)

def cart_update(request, slug):
	next_get = request.GET.get('next')
	next_post = request.POST.get('next')
	redirect_to = next_post or next_get
	product = get_object_or_404(Product, slug=slug)
	cart_obj, created = Cart.objects.new_or_get(request)

	if product in cart_obj.products.all():
		cart_obj.products.remove(product)
	else:
		cart_obj.products.add(product)
	if redirect_to:
		return redirect(redirect_to)
	return redirect('carts:cart_home')

def checkout(request):
	# Get my Cart Object
	billing_profile = None
	cart_obj, created = Cart.objects.new_or_get(request)
	loginForm = LoginForm()
	guestForm = GuestForm()
	addressForm = AddressForm()

	guest_email = request.session.get('guest_email_id')
	if guest_email:
		print('dont have email')
		guest_obj = GuestEmail.objects.get(id=guest_email)
		billing_profile = BillingProfile.objects.create(email=guest_obj.email)


	# Get my billing Object
	
	
	# Create an Order Profile based on the Cart and Billing Profile

	context = {
		'guestForm':guestForm,
		'loginForm':loginForm,
		'billing_profile': billing_profile,
		'addressForm': addressForm,
	}

	return render(request, 'carts/checkout.html', context)













