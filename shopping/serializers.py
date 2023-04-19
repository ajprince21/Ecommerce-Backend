from rest_framework import serializers
from .models import Product, Cart, ProductImage
from django.conf import settings

class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'

    def get_image_url(self, obj):
        return '%s%s' %(settings.SITE_URL.rstrip('/'),obj.image.url)

class ProductImageSerializer(serializers.ModelSerializer):
    # Define a custom method to get the complete image URL
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ('image', 'image_url')

    def get_image_url(self, obj):
        # Use the request object to get the complete image URL with protocol
        request = self.context.get('request')
        image_url = request.build_absolute_uri(obj.image.url)
        return image_url



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart,
        fields= '__all__'