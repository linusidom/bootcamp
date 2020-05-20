from django.urls import path, include
from addresses import views

app_name = 'addresses'

urlpatterns = [
	path('create', views.AddressCreateView.as_view(), name='address_create'),
]
