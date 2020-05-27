from django.db import models
from billing.models import BillingProfile
from carts.models import Cart
from django.db.models.signals import pre_save, post_save
from orders.utils import unique_order_gen
from addresses.models import Address



class OrderManager(models.Manager):
	def new_or_get(self, billing_profile, cart_obj):
		order_obj = None
		created = False
		order_qs = Order.objects.filter(billing_profile=billing_profile, cart=cart_obj, active=True)
		print('Order that came back', order_qs)
		if order_qs.count() == 1:
			order_obj = order_qs.first()
		else:
			older_order_qs = Order.objects.filter(billing_profile=billing_profile, cart=cart_obj)
			if older_order_qs.exists():
				older_order_qs.update(active=False)
			order_obj = Order.objects.create(billing_profile=billing_profile, cart=cart_obj)
		
		return order_obj, created









STATUSES = (
	('paid','Paid'),
	('shipped','Shipped'),
	('competed','Completed'),
	('refunded','Refunded'),
	('processing','Processing'),
	)

# Create your models here.
class Order(models.Model):
	billing_profile = models.ForeignKey(BillingProfile, on_delete=models.SET_NULL, null=True, blank=True)
	cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
	shipping_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, related_name='shipping_address')
	billing_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, related_name='billing_address')
	order_id = models.CharField(max_length = 100, null=True, blank=True)
	shipping_total = models.DecimalField(max_digits=20, decimal_places=2, default=60)
	total = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
	status = models.CharField(max_length=100, null=True, blank=True, choices=STATUSES)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = OrderManager()

	def __str__(self):
		return str(self.id)

	def update_total(self):
		total = self.cart.total

		new_total = total + self.shipping_total
		self.total = new_total
		print(self.total, new_total, self.shipping_total, total)
		self.save()
		return new_total
			


def pre_save_order_id(sender, instance, *args, **kwargs):
	if not instance.order_id:
		instance.order_id = unique_order_gen(instance)

	# I want to run the above before the object get's saved
	# I don't have to use the save() method in here
	# Pre-save just fills in the fields
	# Orders.objects.save()

pre_save.connect(pre_save_order_id, sender=Order)



# If the cart changes
def post_save_cart_updated(sender, instance, created, *args, **kwargs):
	if not created:
		cart_id = instance.id
		qs = Order.objects.filter(cart=cart_id, active=True)
		if qs.count() == 1:
			order_obj = qs.first()
			order_obj.update_total()

			# total = order_obj.cart.total
			# new_total = total + order_obj.shipping_total
			# order_obj.total = new_total


post_save.connect(post_save_cart_updated, sender=Cart)
				
# If the order is created
def post_save_order_created(sender, instance, created, *args, **kwargs):
	if created:
		instance.update_total()

post_save.connect(post_save_order_created, sender=Order)



