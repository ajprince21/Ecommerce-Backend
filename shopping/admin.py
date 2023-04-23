from django.contrib import admin
from .models import Product, Cart, ProductImage
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(ProductImage)
# admin.site.register(User, UserAdmin)
