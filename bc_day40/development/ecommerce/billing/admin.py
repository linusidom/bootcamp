from django.contrib import admin

# Register your models here.
from billing.models import BillingProfile

admin.site.register(BillingProfile)