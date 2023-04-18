# Generated by Django 4.2 on 2023-04-18 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_productimage_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='products', to='shopping.productimage'),
        ),
    ]