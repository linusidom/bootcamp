from django.db import models
from django.db.models.signals import m2m_changed, pre_save, post_save
from billing.models import BillingProfile
from carts.models import Cart
from addresses.models import Address
from orders.utils import unique_order_gen
# Create your models here.

class OrderManager(models.Manager):
	def new_or_get(self, billing_profile=None, cart_obj=None):
		order_obj = None
		created = False
		if billing_profile is not None:
			order_qs = self.model.objects.filter(billing_profile=billing_profile, cart=cart_obj, active=True)
			if order_qs.count() == 1:
				order_obj = order_qs.first()
			else:
				older_order_qs = self.model.objects.filter(billing_profile=billing_profile, cart=cart_obj, active=True)
				if older_order_qs.exists():
					older_order_qs.update(active=False)
				order_obj = self.model.objects.create(billing_profile=billing_profile, cart=cart_obj)
				created = True
		return order_obj, created


class Order(models.Model):
	billing_profile = models.ForeignKey(BillingProfile, on_delete=models.SET_NULL, null=True, blank=True)
	cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
	billing_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, related_name='billing_address')
	shipping_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, related_name='shipping_address')
	order_id = models.CharField(max_length=100, null=True, blank=True)
	shipping = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=60)
	total = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	objects = OrderManager()

	def __str__(self):
		return self.order_id

	def mark_paid(self):
		is_done = self.check_done()
		if is_done:
			self.status = 'paid'
			self.save()
			return True
		return False

	def check_done(self):
		if self.billing_profile and self.shipping_address and self.billing_address and self.total > 0:
			return True
		return False

	def update_total(self):
		cart_total = self.cart.total
		shipping = self.shipping
		new_total = cart_total + shipping
		self.total = new_total
		# print('Update total from Order',self.total)
		self.save()
		return new_total

def pre_save_order_id(sender, instance, *args, **kwargs):
	if not instance.order_id:
		instance.order_id = unique_order_gen(instance)

pre_save.connect(pre_save_order_id, sender=Order)

def post_save_update_total_cart(sender, instance, created, *args, **kwargs):
	if not created:
		cart_id = instance.id
		qs = Order.objects.filter(id=cart_id, active=True)
		if qs.count() == 1:
			order_obj = qs.first()
			order_obj.update_total()

post_save.connect(post_save_update_total_cart, sender=Cart)

def post_save_update_total(sender, instance, created, *args, **kwargs):
	# print('Post Save update total', created)
	if created:
		# print('Update Total Called')
		instance.update_total()
post_save.connect(post_save_update_total, sender=Order)


















