from django.urls import path, include
from carts import views

app_name = 'carts'

urlpatterns = [
	path('', views.cart_home, name='cart_home'),
	path('update/<slug:slug>', views.cart_update, name='cart_update'),
	path('checkout', views.checkout, name='checkout'),
	
]
