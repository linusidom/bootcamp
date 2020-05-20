import string
import random

def rand_gen(num):
	slug = [random.choice(string.ascii_lowercase + string.digits) for i in range(num)]
	return ''.join(slug)

def unique_order_gen(instance, order_id=None):
	if order_id:
		order = order_id
	else:
		order = rand_gen(10)

	Klass = instance.__class__
	qs = Klass.objects.filter(order_id=order).exists()
	if qs:
		order_id = rand_gen(10)
		return unique_order_gen(instance, order_id=order_id)
	return order

def unique_slug_gen(instance, new_slug=None):
	if new_slug:
		slug = new_slug
	else:
		slug = rand_gen(10)

	Klass = instance.__class__
	qs = Klass.objects.filter(slug=slug).exists()
	if qs:
		new_slug = rand_gen(10)
		return unique_slug_gen(instance, new_slug=new_slug)
	return slug