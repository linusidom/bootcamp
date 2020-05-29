from django.shortcuts import render
import stripe
from billing import stripe_keys, omise_keys
from django.views.decorators.csrf import csrf_exempt
import json
import omise
import stripe
# Create your views here.

STRIPE_PUB_KEY = stripe_keys.STRIPE_PUB_KEY
stripe.api_key = stripe_keys.STRIPE_SECRET_KEY

# OMISE

OMISE_PUB_KEY = omise_keys.OMISE_PUB_KEY
omise.api_secret = omise_keys.OMISE_SECRET_KEY


def stripe_payment_view(request):
	print(request.POST)
	context = {
		'publish_key' : STRIPE_PUB_KEY
	}
	return render(request, 'billing/stripe_payment.html', context)

@csrf_exempt
def stripe_payment_processing(request):
	print('Made it',request.POST, request.body)
	response = json.loads(request.body)
	print(response['token'])
	token = response['token']
	if request.user.is_authenticated:
		print(request.user, request.user.email)

		# Create Customer
		# If I want to re-use the same customer ID
		# I have to save it in the database
		# It's a good idea to tie it to the billing profile
		# We won't cover this right now

		# Creates a new customer every time
		customer = stripe.Customer.create(email=request.user.email)
		print('Customer', customer)
		

		# Create Card
		card = stripe.Customer.create_source(customer.id,source=token)
		print('Card', card)

		total = 1000 * 100
		# Charge the card
		# By default the amount is divided by 100
		# Example 2000 => 20.00, 200000 => 2000
		charge = stripe.Charge.create(
		  customer=customer.id,
		  amount=total,
		  currency="usd",
		  source=card.id,
		  description="My First Test Charge (created for API docs)",
		)
		print('Charge', charge)


	context = {
		'publish_key' : STRIPE_PUB_KEY
	}
	return render(request, 'billing/stripe_payment.html', context)





# OMISE
def omise_payment_view(request):
	print(request.POST)
	context = {
		'publish_key' : OMISE_PUB_KEY
	}
	return render(request, 'billing/omise_payment.html', context)

@csrf_exempt
def omise_payment_processing(request):
	print('Made it',request.POST, request.body)
	response = json.loads(request.body)
	print(response['token'])
	token = response['token']
	if request.user.is_authenticated:
		print(request.user, request.user.email)

		# Create Customer
		# If I want to re-use the same customer ID
		# I have to save it in the database
		# It's a good idea to tie it to the billing profile
		# We won't cover this right now


		# Creates a new customer every time
		customer = omise.Customer.create(
		    email=request.user.email,
		    card=token)
		print('Customer', customer.id, customer.default_card)
		

		# Create Card
		
		# Charge the card
		# By default the amount is divided by 100
		# Example 2000 => 20.00, 200000 => 2000
		charge = omise.Charge.create(
			amount=1000 * 100,
			currency="thb",
			customer=customer.id,
			card=customer.default_card)
		print('Charge', charge)


	context = {
		'publish_key' : OMISE_PUB_KEY
	}
	return render(request, 'billing/omise_payment.html', context)