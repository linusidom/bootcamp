from django.test import TestCase
from posts.models import Post

# Functional Unit Testing
# Do the elements work
# I don't care if the pages look good
# I just want the functionality to work

# For user testing we have a whole different method

# Create your tests here.
class PostFeatures(TestCase):

	data = {
		'title':'A new title',
		'author': 'A new author',
		'message': 'A new message'
	}

	updated_data = {
		'title':'Updated title',
		'author': 'Updated author',
		'message': 'Updated message'
	}
	# Test Home Page - should return 200
	# 200 is OK status code from HTML
	# My goal is to get the Test to Pass - That's it!
	def test_post_list_page(self):
		# print('Self Client', dir(self.client))
		request = self.client.get('/')
		# print(request)
		self.assertEqual(request.status_code, 200)
	
	# Test Create Page
	def test_create_page(self):
		request = self.client.get('/create')
		self.assertEqual(request.status_code, 200)
	
	# Test Detail Page
	def test_detail_page(self):
		self.client.post('/create', self.data)
		post = Post.objects.all().first()
		request = self.client.get(f'/detail/{post.id}')
		self.assertEqual(request.status_code, 200)
	
	# Test Update Page
	def test_update_page(self):
		self.client.post('/create', self.data)
		post = Post.objects.all().first()
		request = self.client.get(f'/update/{post.id}')
		self.assertEqual(request.status_code, 200)
	
	# Test Delete Page
	def test_update_page(self):
		self.client.post('/create', self.data)
		post = Post.objects.all().first()
		request = self.client.get(f'/delete/{post.id}')
		self.assertEqual(request.status_code, 200)

	# Test Create Functionality
	# Should return 302 - Redirect
	def test_create_post(self):
		request = self.client.post('/create', self.data)
		self.assertEqual(request.status_code, 302)

	# Test Did a post get created?
	def test_post_created(self):
		request = self.client.post('/create', self.data)
		post = Post.objects.all().first()
		self.assertEqual('A new title', post.title)
	

	# Test Update Functionality
	def test_update_post(self):
		# Create Post
		request = self.client.post('/create', self.data)
		post = Post.objects.all().first()
		
		# Update Post
		request = self.client.post(f'/update/{post.id}', self.updated_data)
		post = Post.objects.all().first()
		self.assertEqual(self.updated_data['title'], post.title)

	# Test Delete Functionality
	def test_delete_post(self):
		# Create Post
		request = self.client.post('/create', self.data)
		post = Post.objects.all().first()

		# Delete Post
		request = self.client.post(f'/delete/{post.id}')
		self.assertEqual(request.status_code, 302)


help(PostFeatures)






