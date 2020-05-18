from django.shortcuts import render, redirect
from carts.models import Cart
from orders.models import Order
def home_page(request):
	# print(dir(self.request.session))
	cart_obj, created = Cart.objects.new_or_get(request)
	# order_obj, created = Order.objects.new_or_get(request)
	return redirect('products:product_list')