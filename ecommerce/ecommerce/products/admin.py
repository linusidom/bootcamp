from django.contrib import admin
from products.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = ['title','slug','price']

admin.site.register(Product, ProductAdmin)
