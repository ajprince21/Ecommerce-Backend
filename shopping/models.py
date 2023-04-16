from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='product_images')
    images = models.ManyToManyField('ProductImage', blank=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sizes = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.image.name


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cart_images')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    size = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name