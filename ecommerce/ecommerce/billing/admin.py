from django.contrib import admin

# Register your models here.
from billing.models import BillingProfile

class BillingAdmin(admin.ModelAdmin):
	list_display = ['user', 'email']

admin.site.register(BillingProfile, BillingAdmin)