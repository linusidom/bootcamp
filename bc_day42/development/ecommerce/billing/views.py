from django.shortcuts import render
import stripe
from billing import stripe_keys
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

STRIPE_PUB_KEY = stripe_keys.STRIPE_PUB_KEY
# stripe.api_key = OUR SECRET KEY


def payment_view(request):
	print(request.POST)
	context = {
		'publish_key' : STRIPE_PUB_KEY
	}
	return render(request, 'billing/stripe_payment.html', context)

@csrf_exempt
def payment_processing(request):
	print('Made it',request.POST, request.body)
	response = json.loads(request.body)
	print(response['token'])
	context = {
		'publish_key' : STRIPE_PUB_KEY
	}
	return render(request, 'billing/stripe_payment.html', context)