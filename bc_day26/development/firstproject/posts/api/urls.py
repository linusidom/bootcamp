from django.urls import path
from posts.api import views

urlpatterns = [
	path('', views.PostListAPIView.as_view()),
	path('create', views.PostCreateAPIView.as_view()),
	path('retrieve/<int:pk>', views.PostRetrieveAPIView.as_view()),
	path('update/<int:pk>', views.PostUpdateAPIView.as_view()),
	path('destroy/<int:pk>', views.PostDestroyAPIView.as_view()),
]