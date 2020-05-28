from django.db import models
from products.models import Product
from billing.models import BillingProfile
from django.db.models.signals import m2m_changed
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class CartManager(models.Manager):
	def new_or_get(self, request):
		created = False
		user = request.user
		cart_id = request.session.get('cart_id')
		if cart_id:
			qs = self.model.objects.filter(id=cart_id)
			if qs:
				cart_obj = qs.first()
				if cart_obj.user is None and user.is_authenticated:
					cart_obj.user = user
					cart_obj.save()
		else:
			if user.is_authenticated:
				cart_obj = self.model.objects.create(user=user)
			else:
				cart_obj = self.model.objects.create()
			request.session['cart_id'] = cart_obj.id
			created = True
		request.session['cart_items'] = cart_obj.products.all().count()
		return cart_obj, created

class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	billing_profile = models.ForeignKey(BillingProfile, on_delete=models.SET_NULL, null=True, blank=True)
	products = models.ManyToManyField(Product)
	total = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
	subtotal = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	objects = CartManager()

	def __str__(self):
		return str(self.id)


	class Meta:
		ordering = ['timestamp']
def m2m_changed_product(sender, instance, *args, **kwargs):
	prod_objs = instance.products.all()
	total = 0
	for prod in prod_objs:
		total += prod.price
	instance.total = total
	instance.save()

m2m_changed.connect(m2m_changed_product, sender=Cart.products.through)	
