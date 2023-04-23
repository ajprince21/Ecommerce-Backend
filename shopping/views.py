from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import viewsets
from .models import Product, Cart, User
from .serializers import ProductSerializer, CartSerializer, UserSerializer
from rest_framework import generics, status


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
        userToken = {}
        userToken['username'] = user.username
        userToken['user_id'] = user.id
        userToken['first_name'] = user.first_name
        userToken['last_name'] = user.last_name
        userToken['email'] = user.email
        userToken['is_superuser'] = user.is_superuser
        return Response({'message': 'Login successful', 'userToken': userToken},status=status.HTTP_200_OK)





class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer







class CartView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retrieve cart items for the currently authenticated user
        user = self.request.user
        queryset = Cart.objects.filter(user=user)
        return queryset

    def perform_create(self, serializer):
        # Set the user to the currently authenticated user
        serializer.save(user=self.request.user)

class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retrieve cart items for the currently authenticated user
        user = self.request.user
        queryset = Cart.objects.filter(user=user)
        return queryset