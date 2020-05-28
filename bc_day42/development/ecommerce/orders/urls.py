from django.urls import path, include
from orders import views

app_name='orders'

urlpatterns = [
	path('order_history', views.order_history, name='order_history'),
]
