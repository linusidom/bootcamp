from django.urls import path
from firstapp import views

app_name = 'firstapp'

urlpatterns = [
	path('', views.BlogListView.as_view(), name='blog_list'),
	path('create', views.BlogCreateView.as_view(), name='blog_create'),	
	path('detail/<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),	
	path('update/<int:pk>', views.BlogUpdateView.as_view(), name='blog_update'),
	path('delete/<int:pk>', views.BlogDeleteView.as_view(), name='blog_delete'),
]