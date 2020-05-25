from django.urls import path, include
from carts import views

app_name = 'carts'

urlpatterns = [
    path('cart_home', views.cart_home, name='cart_home'),
    path('cart_success', views.cart_success, name='cart_success'),
    path('cart_checkout', views.cart_checkout, name='cart_checkout'),
    path('cart_update/<int:pk>', views.cart_update, name='cart_update'),
]
