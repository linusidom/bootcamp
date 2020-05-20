from django.shortcuts import render
from addresses.models import Address
from addresses.forms import AddressForm
from django.views.generic import CreateView

# Create your views here.

class AddressCreateView(CreateView):
	model = Address
	form_class = AddressForm

	def get_success_url(self,*args,**kwargs):
		next_get = self.request.GET.get('next')
		next_post = self.request.POST.get('next')
		redirect_to = next_get or next_post
		return redirect(redirect_to)

	def form_valid(self, form):

		return super(AddressCreateView, self).form_valid(form)
