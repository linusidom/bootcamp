from django.urls import path
from comments import views

app_name = 'comments'

urlpatterns = [
    
    path('', views.CommentListView.as_view(), name='comment_list'),
    path('create/<int:pk>', views.CommentCreateView.as_view(), name='comment_create'),
    path('detail/<int:pk>', views.CommentDetailView.as_view(), name='comment_detail'),
    path('update/<int:pk>', views.CommentUpdateView.as_view(), name='comment_update'),
    path('delete/<int:pk>', views.CommentDeleteView.as_view(), name='comment_delete'),
]
