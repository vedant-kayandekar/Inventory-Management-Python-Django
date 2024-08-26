from django.contrib import admin
from . models import Product, Order
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
# admin.site.unregister(Group)
