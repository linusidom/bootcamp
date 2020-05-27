from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from django.db.models.signals import m2m_changed
from decimal import Decimal

User = get_user_model()

class CartManager(models.Manager):
	def new_or_get(self, request):
		created = False
		cart_id = request.session.get('cart_id')
		# print('This is the new Cart ID', cart_id)
		user = request.user
		# If the cart exists we want to use that one
		if cart_id:
			cart_obj = Cart.objects.get(id=cart_id)
			# Create a new cart
			if user.is_authenticated and cart_obj.user is None:
				# cart_obj, create = Cart.objects.get_or_create(user=user)
				cart_obj.user = user
				cart_obj.save()
		else:
			cart_obj = Cart.objects.create()
			created = True
			# print(cart_obj)
			request.session['cart_id'] = cart_obj.id
		request.session['cart_items'] = cart_obj.products.all().count()
		return cart_obj, created

# Create your models here.
class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	products = models.ManyToManyField(Product)
	subtotal = models.DecimalField(max_digits=20, decimal_places=2, default=0)
	total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	objects = CartManager()

	def __str__(self):
		return str(self.id)

# We want to update the cart each time an item added or removed

def m2m_changed_update_cart(sender, instance, *args, **kwargs):
	cart_items = instance.products.all()
	total = 0
	for item in cart_items:
		total += item.price
	instance.total = total * Decimal(1.10)
	instance.save()

m2m_changed.connect(m2m_changed_update_cart, sender=Cart.products.through)

















