from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from django.db.models.signals import m2m_changed
from decimal import Decimal

User = get_user_model()

class CartManager(models.Manager):
	def new_or_get(self, request):
		created = False
		user = request.user
		cart_id = request.session.get('cart_id')
		if cart_id:
			qs = Cart.objects.get(id=cart_id)
			if qs:
				cart_obj = qs
				if user.is_authenticated and cart_obj.user is None:
					cart_obj.user = user
					cart_obj.save()
		else:
			# Create a Cart
			if user.is_authenticated:
				cart_obj, created = Cart.objects.get_or_create(user=user)
				request.session['cart_id'] = cart_obj.id
			else:
				cart_obj = Cart.objects.create()
				created = True
				request.session['cart_id'] = cart_obj.id
		return cart_obj, created

# Create your models here.
class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	products = models.ManyToManyField(Product)
	subtotal = models.DecimalField(max_digits=20, decimal_places=2, default=0)
	total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = CartManager()

	def __str__(self):
		return str(self.id)

def m2m_changed_cart_total(sender, instance, *args, **kwargs):
	prod_objs = instance.products.all()
	total = 0
	for prod in prod_objs:
		total += prod.price
	instance.total = total * Decimal(1.10)
	instance.save()

m2m_changed.connect(m2m_changed_cart_total, sender=Cart.products.through)