import random
import string

def rand_gen(num):
	slug = [random.choice(string.ascii_lowercase + string.digits) for _ in range(num)]
	return ''.join(slug)


def unique_order_generator(instance, new_order=None):

	if new_order:
		order = new_order
	else:
		order = f'{rand_gen(10)}'

	Klass = instance.__class__
	qs = Klass.objects.filter(order_id=order).exists()
	if qs:
		new_order = f'{rand_gen(10)}'
		return unique_order_generator(instance, new_order=new_order)
	return order

