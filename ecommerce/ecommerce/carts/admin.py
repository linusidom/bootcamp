from django.contrib import admin
from carts.models import Cart
# Register your models here.

class CartAdmin(admin.ModelAdmin):
	list_display = ['id', 'user','total']
admin.site.register(Cart, CartAdmin)