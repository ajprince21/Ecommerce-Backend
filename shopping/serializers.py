from rest_framework import serializers
from .models import Product, Cart, ProductImage
from django.conf import settings
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']  # Add additional fields as needed
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cart
        fields = ('id', 'product', 'quantity', 'user')

    def validate_quantity(self, value):
        """
        Validate that quantity is greater than 0.
        """
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than 0.")
        return value

    def create(self, validated_data):
        """
        Create a cart item with the validated data.
        """
        product = validated_data.get('product')
        user = validated_data.get('user')
        quantity = validated_data.get('quantity', 1)

        # Check if the item already exists in the cart
        cart_item = Cart.objects.filter(product=product, user=user).first()
        if cart_item:
            # Update the quantity of the existing cart item
            cart_item.quantity += quantity
            cart_item.save()
            return cart_item

        # Create a new cart item
        cart_item = Cart(product=product, user=user, quantity=quantity)
        cart_item.save()
        return cart_item
