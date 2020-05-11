from django.urls import path, include
from posts.api import views

app_name = 'post_api'

urlpatterns = [
    path('', views.PostListAPIView.as_view(), name='post_list_api'),
    path('detail/<int:pk>', views.PostDetailAPIView.as_view(), name='post_detail_api'),
]
