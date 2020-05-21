from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
# Create your views here.

class ProductListView(ListView):
	model = Product

	# Looks for product_list
	# Sends product_list variable with all list items
	# Automatically queries the database for us
