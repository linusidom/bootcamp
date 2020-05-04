from django.urls import path
from posts.api import views
urlpatterns = [
	path('', views.list_view),
	path('<int:pk>', views.detail_view),
	path('create', views.create_view),
	path('test_another_view/<int:pk>', views.main_view)
]