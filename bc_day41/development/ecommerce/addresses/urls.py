from django.urls import path
from addresses import views

app_name = 'addresses'

urlpatterns = [
    path('address_create', views.address_create, name='address_create'),
    path('address_update', views.address_update, name='address_update'),
]