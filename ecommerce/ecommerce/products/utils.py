import random
import string

def rand_gen(num):
	slug = [random.choice(string.ascii_lowercase + string.digits) for _ in range(num)]
	return ''.join(slug)

def unique_slug_generator(instance, new_slug=None):

	instance.title = instance.title.replace(' ', '_')
	if new_slug:
		slug = new_slug
	else:
		slug = f'{instance.title}_{rand_gen(5)}'

	Klass = instance.__class__
	qs = Klass.objects.filter(slug=slug).exists()
	if qs:
		new_slug = f'{instance.title}_{rand_gen(5)}'
		return unique_slug_generator(instance, new_slug=new_slug)
	return slug

