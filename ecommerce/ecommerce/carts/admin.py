from django.contrib import admin

# Register your models here.
from carts.models import Cart

class CartAdmin(admin.ModelAdmin):
	list_display = ['id', 'total', 'user']

admin.site.register(Cart, CartAdmin)
