from django.urls import path
from orders import views

app_name = 'orders'

urlpatterns = [
	# path('update/<int:pk>', views.cart_update, name='cart_update'),
	# path('detail/<int:pk>', views.CartDetailView.as_view(), name='cart_detail'),
	path('checkout', views.checkout, name='checkout'),
	# path('', views.CartListView.as_view(), name='cart_list'),
]