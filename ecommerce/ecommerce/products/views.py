from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from products.models import Product
from products.forms import ProductForm
from django.db.models import Q
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

class ProductCreateView(CreateView):
	model = Product
	form_class = ProductForm

class ProductUpdateView(UpdateView):
	model = Product
	form_class = ProductForm

class ProductDeleteView(DeleteView):
	model = Product
	success_url = reverse_lazy('posts:post_list')

class SearchListView(ListView):
	
	def get_queryset(self):
		query = self.request.GET.get('query')
		lookup = Q(title__icontains = query) | Q(description__icontains = query)
		queryset = Product.objects.filter(lookup)
		return queryset
