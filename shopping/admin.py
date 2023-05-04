from django.contrib import admin
from .models import Product, ProductImage, Order
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Order)
# admin.site.register(User, UserAdmin)
