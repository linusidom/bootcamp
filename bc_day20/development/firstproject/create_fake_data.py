import random
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')

import django
django.setup()

from posts.models import Post
from comments.models import Comment

dummy_text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis repellendus ipsa sit delectus, repudiandae illum distinctio mollitia, cupiditate nostrum fugit, totam cumque rem aspernatur facere. Sequi ullam aut assumenda ducimus, accusamus deserunt nobis alias, in exercitationem eligendi, aperiam eum ipsum quae rerum, id enim! Itaque voluptatem placeat assumenda qui, sint enim minima ad, aliquam officiis eum minus velit magnam pariatur animi omnis. Alias molestias magnam illo deleniti, odio nostrum qui fuga accusantium aperiam quos sequi. Sed nostrum beatae sapiente perferendis adipisci natus quod. Nisi, beatae in! Autem illum distinctio minima enim incidunt aspernatur, dolorem aperiam odit maiores! Ipsam, perspiciatis, rerum.'.split()

def rand_select(num):
	return [random.choice(dummy_text) for i in range(num)]

# print(dummy_text)

blog_entries = 20
comment_entries = 100


for i in range(blog_entries):
	title = ' '.join(rand_select(random.randint(3,7))).title()
	author = ' '.join(rand_select(random.randint(1,3))).title()
	message = ' '.join(rand_select(random.randint(40,100))).capitalize()

	Post.objects.get_or_create(
		title=title,
		author=author,
		message=message)

posts = Post.objects.all()
post_ids = [post.id for post in posts]

for i in range(comment_entries):
	post = Post.objects.get(pk=random.choice(post_ids))
	author = ' '.join(rand_select(random.randint(1,3))).title()
	message = ' '.join(rand_select(random.randint(10,30))).capitalize()

	Comment.objects.get_or_create(
		post=post,
		author=author,
		message=message)