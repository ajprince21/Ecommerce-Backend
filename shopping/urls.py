from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/<int:product_id>/', CartItemView.as_view(), name='add_to_cart'),
    path('cart/update/<int:cart_item_id>/', CartItemUpdateView.as_view(), name='update_cart_item'),
    path('cart/delete/<int:cart_item_id>/', CartItemDeleteView.as_view(), name='delete_cart_item'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)