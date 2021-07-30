from django.urls import path
from .views import ProductListAPIView, ProductRetrieveAPIView

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product'),
    path('<int:id>', ProductRetrieveAPIView.as_view(), name='product')
]
