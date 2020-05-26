from django.urls import path, include
from products import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('detail/<slug:slug>', views.ProductDetailView.as_view(), name='product_detail'),
    
]
