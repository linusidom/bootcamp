from django.urls import path
from carts import views

app_name = 'carts'

urlpatterns = [
	path('update/<int:pk>', views.cart_update, name='cart_update'),
	path('detail/<int:pk>', views.CartDetailView.as_view(), name='cart_detail'),
	# path('checkout', views.checkout_view, name='checkout_home'),
	# path('', views.CartListView.as_view(), name='cart_list'),
]