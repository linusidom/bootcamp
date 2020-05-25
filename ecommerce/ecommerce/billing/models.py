from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import GuestEmail
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

	objects = BillingManager()

	def __str__(self):
		return self.email