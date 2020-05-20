from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, m2m_changed
from decimal import Decimal

User = get_user_model()

class CartManager(models.Manager):
	def new_or_get(self, request):
		user = request.user
		created = False
		cart_id = request.session.get('cart_id')
		if cart_id:
			cart_obj = self.model.objects.get(id=cart_id)
			if user.is_authenticated and cart_obj.user is None:
				cart_obj.user = user
				cart_obj.save()
		else:
			if user.is_authenticated:
				cart_obj = self.model.objects.create(user=user)
			else:
				cart_obj = self.model.objects.create()
			created = True
			request.session['cart_id'] = cart_obj.id
		request.session['cart_items'] = cart_obj.products.all().count()
		return cart_obj, created
		# If the user logs in we want to associate the cart to the user



# Create your models here.
class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	products = models.ManyToManyField(Product)
	subtotal = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
	total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
	timestamp = models.DateTimeField(auto_now=True)
	updated = models.DateTimeField(auto_now_add=True)
	
	objects = CartManager()

	def __str__(self):
		return str(self.id)

def pre_save_total(sender, instance, *args, **kwargs):
	if instance.subtotal > 0:
		instance.total = instance.subtotal * Decimal(1.10)

pre_save.connect(pre_save_total, sender=Cart)

def m2m_changed_subtotal(sender, instance, *args, **kwargs):
	products = instance.products.all()
	total = 0
	for prod in products:
		total += prod.price
	instance.subtotal = total
	instance.save()

m2m_changed.connect(m2m_changed_subtotal, sender=Cart.products.through)
