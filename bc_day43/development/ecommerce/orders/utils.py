import random
import string

# print(string.ascii_lowercase)
# print(string.digits)

def rand_gen(num):
	value = [random.choice(string.ascii_lowercase + string.digits) for i in range(num)]
	# print(value)
	return ''.join(value)

def unique_order_gen(instance, new_order = None):

	if new_order:
		order_id = new_order
	else:
		order_id = rand_gen(10)

	# Check the entite table not just the instance for repeats
	# I can call the model that I want to check on
	Klass = instance.__class__

	qs = Klass.objects.filter(order_id=order_id).exists()
	if qs:
		new_order_id = rand_gen(10)
		return unique_order_gen(instance, new_order=new_order_id)
	return order_id