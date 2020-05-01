from django.urls import path
from posts.api import views

app_name = 'api_posts'

urlpatterns = [
	path('', views.PostListAPIView.as_view(), name='api_post_list'),
	path('<int:pk>', views.PostRetrieveAPIView.as_view(), name='api_post_detail'),
]
