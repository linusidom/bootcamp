from django.shortcuts import render
from products.models import Product
from carts.models import Cart
from django.views.generic import ListView
# Create your views here.



class ProductListView(ListView):
	model = Product

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['cart_obj'], created = Cart.objects.new_or_get(self.request)
		return context
