from django.urls import path, include
from billing import views

app_name = 'billing'

urlpatterns = [ 
    path('stripe_payment', views.stripe_payment, name='stripe_payment'),
    path('billing_stripe_create', views.billing_stripe_create, name='billing_stripe_create'),
]
