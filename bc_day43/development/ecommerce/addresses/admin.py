from django.contrib import admin

# Register your models here.
from addresses.models import Address

admin.site.register(Address)