from django.db import models
from django.db.models.signals import pre_save, m2m_changed
from products.models import Product
from decimal import Decimal
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class CartManager(models.Manager):
	def new_or_get(self, request):
		# del request.session['cart_id']
		created = False
		cart_id = request.session.get('cart_id', None)
		qs = Cart.objects.filter(id=cart_id)
		if qs.count() == 1:
			cart_obj = qs.last()
			if request.user.is_authenticated and cart_obj.user is None:
				cart_obj.user = request.user
				cart_obj.save()
		else:
			cart_obj = Cart.objects.new(user=request.user)
			created = True
			request.session['cart_id'] = cart_obj.id
			print(request.session['cart_id'], cart_obj.id)
		return cart_obj, created

	def new(self, user=None):
		user_obj = None
		if user is not None:
			if user.is_authenticated:
				user_obj = user
		return Cart.objects.create(user=user_obj)

class Cart(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    products    = models.ManyToManyField(Product, blank=True)
    subtotal    = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total       = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    created_cart = models.BooleanField(null=True, blank=True)
    objects = CartManager()

    def __str__(self):
        return str(self.id)

def m2m_changed_total(sender, instance, *args, **kwargs):
	# print('Sender', sender)
	# print('Instance', instance)
	# print('Args', args)
	# print('Kwargs', kwargs)
	products = instance.products.all()
	total = 0
	tax = 1.1
	# print(products)
	for product in products:
		# print(product.price)
		total += product.price
	instance.subtotal = total
	instance.total = total * Decimal(tax)
	instance.save()

m2m_changed.connect(m2m_changed_total, sender=Cart.products.through)