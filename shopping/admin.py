from django.contrib import admin
from .models import Product, Cart, ProductImage
# Register your models here.

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(ProductImage)
