from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import viewsets
from .models import Product, Cart
from .serializers import ProductSerializer, CartSerializer
from rest_framework import generics, status


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        product = self.get_object()
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        print(serializer.data)
        return Response({
            'status':200,
            'data':serializer.data,
            'message':'Get Method called',
        })
    
    def post(self, request):    
        return Response({
            'status':200,
            'message':'post Method called',
        })


    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer