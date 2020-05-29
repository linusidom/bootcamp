from django.urls import path, include
from billing import views

app_name='billing'

urlpatterns = [
	path('stripe_payment_view', views.stripe_payment_view, name='stripe_payment_view'),
	path('stripe_payment_processing', views.stripe_payment_processing, name='stripe_payment_processing'),

	path('omise_payment_view', views.omise_payment_view, name='omise_payment_view'),
	path('omise_payment_processing', views.omise_payment_processing, name='omise_payment_processing'),
]
