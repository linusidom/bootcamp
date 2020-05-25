from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
from carts.models import Cart
# Create your views here.

class ProductListView(ListView):
	model = Product

	# Looks for product_list
	# Sends product_list variable with all list items
	# Automatically queries the database for us
	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)

		context['cart_obj'], created = Cart.objects.new_or_get(self.request)
		
		return context