from django.db import models
from django.db.models.signals import pre_save
from orders.utils import unique_order_gen
from billing.models import BillingProfile
from carts.models import Cart
# Create your models here.
class Order(models.Model):
	billing_profile = models.ForeignKey(BillingProfile, on_delete=models.SET_NULL, null=True, blank=True)
	cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
	# shipping_address
	# billing_address
	order_id = models.CharField(max_length=100, null=True, blank=True)
	status = models.CharField(max_length=100, null=True, blank=True)
	shipping_total = models.DecimalField(max_digits=20, decimal_places=2, default=300)
	total = models.DecimalField(max_digits=20, decimal_places=2, default=300)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.order_id

def pre_save_gen_order_id(sender, instance, *args, **kwargs):
	if not instance.order_id:
		instance.order_id = unique_order_gen(instance)

pre_save.connect(pre_save_gen_order_id, sender=Order)