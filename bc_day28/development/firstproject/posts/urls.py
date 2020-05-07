from django.urls import path, include
from posts import views

app_name = 'posts'

urlpatterns = [
    
    path('', views.PostListView.as_view(), name='post_list'),
    path('create', views.PostCreateView.as_view()),
    path('detail/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('update/<int:pk>', views.PostUpdateView.as_view()),
    path('delete/<int:pk>', views.PostDeleteView.as_view()),
]