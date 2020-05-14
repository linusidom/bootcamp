import random
import requests
# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')

# import django
# django.setup()


# from posts.models import Post

dummy_text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis repellendus ipsa sit delectus, repudiandae illum distinctio mollitia, cupiditate nostrum fugit, totam cumque rem aspernatur facere. Sequi ullam aut assumenda ducimus, accusamus deserunt nobis alias, in exercitationem eligendi, aperiam eum ipsum quae rerum, id enim! Itaque voluptatem placeat assumenda qui, sint enim minima ad, aliquam officiis eum minus velit magnam pariatur animi omnis. Alias molestias magnam illo deleniti, odio nostrum qui fuga accusantium aperiam quos sequi. Sed nostrum beatae sapiente perferendis adipisci natus quod. Nisi, beatae in! Autem illum distinctio minima enim incidunt aspernatur, dolorem aperiam odit maiores! Ipsam, perspiciatis, rerum.'.split()

def rand_select(num):
	return [random.choice(dummy_text) for i in range(num)]


post_entries = 5

message_dict = {}

url = 'https://glacial-gorge-20698.herokuapp.com/post_api/create'

# url = 'http://127.0.0.1:8000/post_api/create'

for i in range(post_entries):
	title = ' '.join(rand_select(random.randint(3,5))).title()
	author = ' '.join(rand_select(random.randint(2,3))).title()
	message = ' '.join(rand_select(random.randint(10,20))).capitalize()

	message_dict["title"] = title
	message_dict["author"] = author
	message_dict["message"] = message


	result = requests.post(url, data=message_dict)
	print(result, result.content)