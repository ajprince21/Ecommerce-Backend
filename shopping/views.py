from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import viewsets
from .models import Product, Cart
from .serializers import ProductSerializer, CartSerializer
from rest_framework import generics, status

  

class ProductDetail(APIView):
    def get(self, request, *args, **kwargs):
        try:
            product_id = kwargs.get('pk')  # Retrieve the pk from URL kwargs
            product = Product.objects.get(id=product_id)  # Retrieve the product by id
        except Product.DoesNotExist:
            # If product does not exist, return appropriate error response
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the product details and return the response
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class ProductView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        print(serializer.data)
        return Response({
            'status':200,
            'data':serializer.data,
        })
    
    def post(self, request):    
        return Response({
            'status':200,
            'message':'post Method called',
        })


    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer