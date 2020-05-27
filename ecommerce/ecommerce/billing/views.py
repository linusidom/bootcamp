from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from billing import stripe_keys
from billing.models import BillingProfile, Card
import stripe
STRIPE_PUB_KEY = stripe_keys.STRIPE_PUB_KEY
stripe.api_key = stripe_keys.STRIPE_SECRET_KEY


# Create your views here.
def stripe_payment(request):
	return render(request, 'billing/stripe_payment.html', {'publish_key': STRIPE_PUB_KEY, 'clientSecret':stripe.api_key})

@csrf_exempt
def billing_stripe_create(request):
	# print('Request Method', request.method)

	if request.method == 'POST' and request.is_ajax():
		billing_profile, created = BillingProfile.objects.new_or_get(request)
		if not billing_profile:
			return HttpResponse({"message":"Cannot find this user"}, status_code=404)
		token = request.POST.get('token')
		if token is not None:
			customer = stripe.Customer.retrieve(billing_profile.customer_id)
			# stripe_card_response = customer.sources.create(source=token)
			stripe_card_response = stripe.Customer.create_source(customer.id, source=token)
			new_card_object = Card.objects.add_new(billing_profile, stripe_card_response)
			print(new_card_object)
		return JsonResponse({"message":"DONE"}, safe=False)
	return render(request, 'billing/stripe_payment.html', {'publish_key': STRIPE_PUB_KEY, 'clientSecret':stripe.api_key})