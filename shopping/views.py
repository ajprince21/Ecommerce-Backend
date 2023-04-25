from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import viewsets
from .models import Product, User, Cart, CartItem
from .serializers import ProductSerializer, UserSerializer, CartItemSerializer
from rest_framework import generics, status
from rest_framework.authtoken.models import Token


class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(username=username).first()
        if user is None:
            return Response({'error': 'No user found !!'},
                status=status.HTTP_401_UNAUTHORIZED)
        if not user.check_password(password):
            return Response({'error': 'Invalid Password'},status=status.HTTP_401_UNAUTHORIZED)
        # token = Token.objects.get(user=user)
        token, created = Token.objects.get_or_create(user=user)
        userToken = {}
        userToken['username'] = user.username
        userToken['user_id'] = user.id
        userToken['first_name'] = user.first_name
        userToken['last_name'] = user.last_name
        userToken['email'] = user.email
        userToken['is_superuser'] = user.is_superuser
        userToken['token'] = token.key
        return Response({'message': 'Login successful', 'userToken': userToken},status=status.HTTP_200_OK)





class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class CartView(APIView):
    def get(self, request):
        cart = Cart.objects.get_or_create(user=request.user)[0]
        cart_items = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)

class CartItemView(APIView):
    def post(self, request, product_id):
        cart = Cart.objects.get_or_create(user=request.user)[0]
        product = Product.objects.get(id=product_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CartItemUpdateView(APIView):
    def put(self, request, cart_item_id):
        quantity = int(request.data.get('quantity'))
        cart_item = CartItem.objects.get(id=cart_item_id)
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            serializer = CartItemSerializer(cart_item)
            return Response(serializer.data)
        else:
            cart_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class CartItemDeleteView(APIView):
    def delete(self, request, cart_item_id):
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)