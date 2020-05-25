from django.urls import path, include
from addresses import views

app_name = 'addresses'

urlpatterns = [
    path('address_check', views.address_check, name='address_check'),
    path('address_update', views.address_update, name='address_update'),
]
