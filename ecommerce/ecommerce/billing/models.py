from django.db import models
from django.db.models.signals import post_save, pre_save
from django.contrib.auth import get_user_model
from accounts.models import GuestEmail
from billing import stripe_keys
import stripe

stripe.api_key = stripe_keys.STRIPE_SECRET_KEY


User = get_user_model()
# Create your models here.

class BillingManager(models.Manager):
	def new_or_get(self, request):
		billing_profile = None
		created = False
		user = request.user
		guest_email_id = request.session.get('guest_email_id')

		billing_profile_id = request.session.get('billing_profile_id')
		if billing_profile_id:
			qs = self.model.objects.get(id=billing_profile_id)
			if qs:
				billing_profile = qs
				if billing_profile.user is None and user.is_authenticated:
					billing_profile.user = user
					billing_profile.save()
		elif user.is_authenticated:
			if user.email:
				billing_profile = self.model.objects.create(user=user, email=email)
			else:
				billing_profile = self.model.objects.create(user=user)
			request.session['billing_profile_id'] = billing_profile.id
		elif guest_email_id:
			guest_email = GuestEmail.objects.get(id=guest_email_id)
			billing_profile = self.model.objects.create(email=guest_email)
			created = True
			request.session['guest_email_id'] = billing_profile.id
			request.session['billing_profile_id'] = billing_profile.id
		return billing_profile, created

class BillingProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	customer_id = models.CharField(max_length=100, null=True, blank=True)
	default = models.BooleanField(default=True)
	objects = BillingManager()

	def __str__(self):
		return str(self.email)

	def charge(self, billing_profile, order_obj, card=None):
		return Charge.objects.create_charge(self, order_obj, card)

def pre_save_customer_id_stripe(sender, instance, *args, **kwargs):
	if not instance.customer_id and instance.email:
		print('API RESPONSE FROM STRIPE')
		customer = stripe.Customer.create(
			email=instance.email,
			)
		print(customer)
		instance.customer_id = customer.id
		
pre_save.connect(pre_save_customer_id_stripe, sender=BillingProfile)

def post_save_user_created(sender, instance, created, *args, **kwargs):
	if created and instance.email:
		BillingProfile.objects.get_or_create(user=instance, email=instance.email)

post_save.connect(post_save_user_created, sender=User)

class CardManager(models.Manager):
	def add_new(self, billing_profile, stripe_card_response):
		print(stripe_card_response.object)
		if str(stripe_card_response.object) == 'card':
			new_card = self.model(
				stripe_id = stripe_card_response.id,
				billing_profile=billing_profile,
				brand=stripe_card_response.brand,
				country=stripe_card_response.country,
				exp_month=stripe_card_response.exp_month,
				exp_year=stripe_card_response.exp_year,
				last4=stripe_card_response.last4
				)
			new_card.save()
			return new_card
		return None

class Card(models.Model):
	stripe_id = models.CharField(max_length=120, null=True, blank=True)
	billing_profile = models.ForeignKey(BillingProfile, on_delete=models.SET_NULL, null=True)
	brand = models.CharField(max_length=120, null=True, blank=True)
	country = models.CharField(max_length=120, null=True, blank=True)
	exp_month = models.IntegerField(null=True, blank=True)
	exp_year = models.IntegerField(null=True, blank=True)
	last4 = models.CharField(max_length=4, null=True, blank=True)

	objects = CardManager()

	def __str__(self):
		return f'{self.brand} {self.last4}'



class ChargeManager(models.Manager):
	def create_charge(self, billing_profile, order_obj, card=None):
		card_obj = card
		if card_obj is None:
			cards = billing_profile.card_set.filter(default=True)
			if cards.exists():
				card_obj = cards.first()
		if card_obj is None:
			return False, 'No cards available'
		charge = stripe.Charge.create(
			amount=int(order_obj.total) * 100,
			currency='usd',
			customer=billing_profile.customer_id,
			source=card_obj.stripe_id,
			# metadata={"order_id":order_obj.order_id}
			)
		new_charge = self.model(
			billing_profile=billing_profile,
			stripe_id=charge.id,
			paid = charge.paid,
			refunded = charge.refunded,
			outcome = charge.outcome,
			outcome_type = charge.outcome['type'],
			seller_message = charge.outcome.get('seller_message'),
			risk_level = charge.outcome.get('risk_level'),
			)
		new_charge.save()
		return new_charge.paid, new_charge.seller_message

class Charge(models.Model):
	stripe_id = models.CharField(max_length=120, null=True, blank=True)
	billing_profile = models.ForeignKey(BillingProfile, on_delete=models.SET_NULL, null=True)
	paid = models.BooleanField(default=False)
	refunded = models.BooleanField(default=False)
	outcome = models.TextField(null=True, blank=True)
	outcome_type = models.CharField(max_length=120, null=True, blank=True)
	seller_message = models.CharField(max_length=120, null=True, blank=True)
	risk_level = models.CharField(max_length=120, null=True, blank=True)

	objects = ChargeManager()
