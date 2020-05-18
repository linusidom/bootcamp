from django.db import models
from carts.models import Cart
from django.contrib.auth import get_user_model
from orders.utils import unique_order_generator
from django.db.models.signals import pre_save, post_save
from decimal import Decimal

User = get_user_model()
# Create your models here.




class Order(models.Model):
	STATUS = (
		('Paid','Paid'),
		('Processing','Processing'),
		('Shipped','Shipped'),
		('Delivered','Delivered'),
		('Refunded','Refunded'),
		)

	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	order_id = models.CharField(max_length=100, null=True, blank=True)
	# billing_profile = models.ForeignKey(BillingProfile, on_delete=models.SET_NULL, null=True)
	# shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.SET_NULL, null=True)
	# billing_address = models.ForeignKey(BillingAddress, on_delete=models.SET_NULL, null=True)
	cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
	status = models.CharField(max_length=100, null=True, blank=True, choices=STATUS)
	shipping_total = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
	total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

	# objects = OrderManager()

	def __str__(self):
		return str(self.order_id)

	def update_total(self):
		cart_total = self.cart.total
		shipping_total = self.shipping_total
		new_total = Decimal(cart_total) + Decimal(shipping_total)
		self.total = Decimal("{:.2f}".format(new_total))
		self.save()
		return new_total

def pre_save_order_id_gen(sender, instance, *args, **kwargs):
	if not instance.order_id:
		instance.order_id = unique_order_generator(instance)

pre_save.connect(pre_save_order_id_gen, sender=Order)

# Update Total each time Cart gets updated
def post_save_update_total(sender, instance, created, *args, **kwargs):
	if not created:
		# print(instance.id)
		cart_obj = instance
		cart_total = instance.total
		qs = Order.objects.filter(cart__id=instance.id)
		if qs.count() == 1:
			order_obj = qs.first()
			order_obj.update_total()

post_save.connect(post_save_update_total, sender=Cart)

# Update Total when at the checkout page and order is saved
def post_save_order_update(sender, instance, created, *args, **kwargs):
	if created:
		instance.update_total()
post_save.connect(post_save_order_update, sender=Order)