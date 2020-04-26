from django.urls import path, re_path
from firstapp import views
app_name = 'firstapp'

urlpatterns = [
	path('', views.BlogListView.as_view()),

	# Generic detail view BlogDetailView must be called with either an object pk or a slug in the URLconf.
	# re_path('detail/(?P<pk>\d+)', views.BlogDetailView.as_view()),

	path('detail/<int:pk>/', views.BlogDetailView.as_view()),
]