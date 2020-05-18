from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from products.models import Product
from carts.models import Cart
from orders.models import Order
# Create your views here.
# Add to cart/Remove From cart


class CartDetailView(DetailView):
	model = Cart

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		# print(args, kwargs)
		# cart_obj, created = Cart.objects.new_or_get(self.request)
		# context['cart_item_count'] = cart_obj.products.all().count()
		# context['cart_id'] = cart_obj.id
		return context

def cart_update(request, pk):
	referrer = request.META.get('HTTP_REFERER')
	
	product_obj = Product.objects.get(pk=pk)
	cart_obj, created = Cart.objects.new_or_get(request)
	# print(cart_obj)
	if product_obj in cart_obj.products.all():
		cart_obj.products.remove(product_obj)
	else:
		cart_obj.products.add(product_obj)
	request.session['cart_item_count'] = cart_obj.products.all().count()
	if 'carts' in referrer:
		return redirect('carts:cart_detail', pk=cart_obj.id)
	else:
		return redirect('/')

def cart_home(request):
	cart_obj, created = Cart.objects.new_or_get(request)
	if request.user.is_authenticated:
		qs = Order.objects.filter(user=request.user, cart=cart_obj)
		if qs:
			order_obj = qs.first()
	else:
		order_obj = Order.objects.get_or_create(cart=cart_obj)
		
	return render(request, 'carts/cart_detail',{})


