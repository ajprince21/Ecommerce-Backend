from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='product_images')
    images = models.ManyToManyField('ProductImage', related_name='products', blank=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sizes = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='product_images')
    sequence_no = models.IntegerField(default=0)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', through='CartItem')

    def __str__(self):
        return f'Cart for {self.user.username}'
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.cart.user.username} - {self.product.name}'
