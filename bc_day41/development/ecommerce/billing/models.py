from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from accounts.models import GuestEmail

User = get_user_model()

# Create your models here.

class BillingManager(models.Manager):
	def new_or_get(self, request):	
		billing_profile = None
		created = False
		guest_email_id = request.session.get('guest_email_id') #returns ID or None
		billing_profile_id = request.session.get('billing_profile_id')

		if billing_profile_id is not None:
			billing_profile = self.model.objects.get(id=billing_profile_id)
			if request.user.is_authenticated and billing_profile.user is None:
				billing_profile.user = request.user
				billing_profile.email = request.user.email
				billing_profile.save()
		elif request.user.is_authenticated:
			billing_profile, created = self.model.objects.get_or_create(email=request.user.email)
			
		elif guest_email_id:
			guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
			billing_profile = self.model.objects.create(email=guest_email_obj)
			request.session['billing_profile_id'] = billing_profile.id
			created = True

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

def post_save_user_created(sender, instance, created, *args, **kwargs):
	print('Sender',sender)
	print('Instance',instance, instance.email)
	print('Created', created)
	print('Arguments', args)
	print('KeyWord Arguments', kwargs)
	if created:
		BillingProfile.objects.create(user=instance, email=instance.email)


post_save.connect(post_save_user_created, sender=User)