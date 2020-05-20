from django.shortcuts import render
from django.views.generic import ListView, DetailView
from products.models import Product
from carts.models import Cart
# Create your views here.

class ProductListView(ListView):
	model = Product

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		cart_obj, created = Cart.objects.new_or_get(self.request)
		context['cart_obj'] = cart_obj
		return context

class ProductDetailView(DetailView):
	model = Product