from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from posts.models import Post
from posts.api.serializers import PostSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# GET request
def list_view(request):
	queryset = Post.objects.all()
	print('Posts', queryset)
	serialization = PostSerializer(queryset, many=True)
	print('Serialization ', serialization.data)
	return JsonResponse(serialization.data, safe=False)

# GET reqest
def detail_view(request, pk):
	queryset = Post.objects.get(pk=pk)
	# for obj in queryset:
	# 	print(obj)
	# print(Post.objects.get(pk=pk))
	# print(Post.objects.filter(pk=pk))
	
	serialization = PostSerializer(queryset)
	print('Serialization ', serialization.data)
	return JsonResponse(serialization.data, safe=False)

# POST Request
@csrf_exempt
def create_view(request):
	print(request.POST.get('title'))
	data = JSONParser().parse(request)
	serialization = PostSerializer(data=data)
	if serialization.is_valid():
		serialization.save()
		return JsonResponse(serialization.data, safe=False, status = 201)
	return JsonResponse(serialization.errors, safe=False, status=400)

@csrf_exempt
def main_view(request, pk):
	if request.method == 'GET':
		print('GET')
		return HttpResponse('GET METHOD')

	if request.method == 'POST':
		data = JSONParser().parse(request)
		serialization = PostSerializer(data=data)
		if serialization.is_valid():
			serialization.save()
			return JsonResponse(serialization.data, safe=False, status = 201)
		return JsonResponse(serialization.errors, safe=False, status=400)
		
	if request.method == 'DELETE':
		print('DELETE')
		post = get_object_or_404(Post, pk=pk)
		# print(Post.objects.get(pk=pk))
		# Post.objects.get(pk=pk).delete()
		post.delete()
		return HttpResponse(status=204)



