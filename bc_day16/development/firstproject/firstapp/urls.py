from django.urls import path, re_path
from firstapp import views
app_name = 'firstapp'

urlpatterns = [
	# Function Call instead of CLASS CALL
	# In this case Blog_List_View would be a Function
	# path('function_based_view', views.Blog_List_View),





	# Use as_view to call a CLASS
	path('', views.BlogListView.as_view(), name='index'),
	re_path('detail/(?P<pk>\d+)/', views.BlogDetailView.as_view()),
	# path('detail/<int:pk>/', views.BlogDetailView.as_view()),

	path('create', views.BlogCreateView.as_view()),
	path('update/<int:pk>/', views.BlogUpdateView.as_view()),
	path('delete/<int:pk>/', views.BlogDeleteView.as_view()),
]