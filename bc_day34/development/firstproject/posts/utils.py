import random
import string

# Can't import files into each other - Circular Import
# from posts.models import Post


# We want to generate random slug

def rand_slug(num):
	slug = [random.choice(string.ascii_lowercase + string.digits) for i in range(num)]
	return ''.join(slug)

# print(string.ascii_lowercase)
# print(string.digits)
 # that is not already in use every time
 # Check the Database
 
def unique_or_not(instance, new_slug=None):
	print('instance from utils', instance.title)

	if new_slug:
		slug = new_slug
	else:
		slug = f'{rand_slug(10)}'
	Klass = instance.__class__
	queryset = Klass.objects.filter(slug=slug).exists()
	if queryset:
		new_slug = rand_slug(10)
		return unique_or_not(instance, new_slug)

	return slug