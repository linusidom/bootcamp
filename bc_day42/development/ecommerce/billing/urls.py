from django.urls import path, include
from billing import views

app_name='billing'

urlpatterns = [
	path('payment_view', views.payment_view, name='payment_view'),
	path('payment_processing', views.payment_processing, name='payment_processing'),
]
