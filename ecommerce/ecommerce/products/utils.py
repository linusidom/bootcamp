import random
import string

def rand_gen(num):
	val = [random.choice(string.ascii_lowercase + string.digits) for i in range(num)]
	return ''.join(val)

def unique_order_gen(instance, new_order=None):
	if new_order is not None:
		order_id = new_order
	else:
		order_id = rand_gen(10)

	Klass = instance.__class__
	qs = Klass.objects.filter(order_id=order_id).exists()
	if qs:
		new_order = rand_gen(10)
		return unique_order_gen(instance, new_order)
	return order_id


def unique_slug_gen(instance, new_slug=None):
	if new_slug is not None:
		slug = new_slug
	else:
		slug = rand_gen(10)

	Klass = instance.__class__
	qs = Klass.objects.filter(slug=slug).exists()
	if qs:
		new_slug = rand_gen(10)
		return unique_slug_gen(instance, new_slug)
	return slug
