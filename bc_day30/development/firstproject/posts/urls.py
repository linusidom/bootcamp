from django.urls import path, include
from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('detail/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
]
