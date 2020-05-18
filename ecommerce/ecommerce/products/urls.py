from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
	path('', views.ProductListView.as_view(), name='product_list'),
	path('create', views.ProductCreateView.as_view(), name='product_create'),
	path('detail/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
	path('update/<int:pk>', views.ProductUpdateView.as_view(), name='product_update'),
	path('delete/<int:pk>', views.ProductDeleteView.as_view(), name='product_delete'),

	path('search', views.SearchListView.as_view(), name='search'),
]