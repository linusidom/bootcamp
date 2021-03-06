from django.shortcuts import render, redirect
from carts.models import Cart
from products.models import Product
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