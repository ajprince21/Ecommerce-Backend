from django.urls import path
from .views import *


urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
]