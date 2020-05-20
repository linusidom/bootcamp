from django.db import models
from carts.models import Cart
from billing.models import BillingProfile
from addresses.models import Address
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, post_save
from orders.utils import unique_order_gen
from decimal import Decimal
User = get_user_model()
# Create your models here.

class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	order_id = models.CharField(max_length=100, null=True, blank=True)
	billing_profile = models.ForeignKey(BillingProfile, on_delete=models.SET_NULL, null=True, blank=True)
	cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
	shipping_address = models.ForeignKey(Address, related_name='shipping_address', on_delete=models.SET_NULL, null=True, blank=True)
	billing_address = models.ForeignKey(Address, related_name='billing_address', on_delete=models.SET_NULL, null=True, blank=True)
	total = models.DecimalField(max_digits=2, default=0.00, decimal_places=2)
	shipping_total = models.DecimalField(max_digits=2, default=60, decimal_places=2)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now_add=True)
	timestamp = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.order_id

	def update_total(self):
		total = self.cart.total
		shipping_total = self.shipping_total
		new_total = Decimal(total) + Decimal(shipping_total)
		self.total = new_total
		self.save()
		return new_total

def pre_save_order_id(sender, instance, *args, **kwargs):
	if not instance.order_id:
		instance.order_id = unique_order_gen(instance)

pre_save.connect(pre_save_order_id, sender=Order)

def post_save_total(sender, instance, created, *args, **kwargs):
	if not created:
		qs = Order.objects.get(cart=instance.id)
		if qs.count() == 1:
			order_obj = qs.first()
			order_obj.update_total()

post_save.connect(post_save_total, sender=Cart)


def post_save_total(sender, instance, created, *args, **kwargs):
	if created:
		instance.update_total()

post_save.connect(post_save_total, sender=Order)




