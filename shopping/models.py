from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


# class User(AbstractUser):
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='users_shopping',
#         blank=True,
#         help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
#         verbose_name='groups',
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='users_shopping',
#         blank=True,
#         help_text='Specific permissions for this user.',
#         verbose_name='user permissions',
#     )

#     def __str__(self):
#         return self.username

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    overall_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart item {self.product.name} for user {self.user.username}'

    def save(self, *args, **kwargs):
        self.overall_price = self.quantity * self.product.price
        super(Cart, self).save(*args, **kwargs)