from django.urls import path
from posts.api import views

app_name = 'post_api'

urlpatterns = [
	path('', views.PostListAPIView.as_view()),
	path('create', views.PostCreateAPIView.as_view()),
	path('detail/<int:pk>', views.PostDetailAPIView.as_view()),
	path('update/<int:pk>', views.PostUpdateAPIView.as_view()),
	path('delete/<int:pk>', views.PostDeleteAPIView.as_view()),
	path('search', views.SearchAPIView.as_view()),
]