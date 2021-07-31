from django.urls import path
from .views import ProductDetailListAPIView, ProductDetailRetrieveAPIView

urlpatterns = [
    path('', ProductDetailListAPIView.as_view(), name='product_detail'),
    path('<int:id>', ProductDetailRetrieveAPIView.as_view(), name='product_detail')
]
