from django.contrib import admin

# Register your models here.
from accounts.models import MyAbstractUser

admin.site.register(MyAbstractUser)