from django.urls import path
from .views import CategoryListAPIView, CategoryRetrieveAPIView

urlpatterns = [
    path('', CategoryListAPIView.as_view(), name='category'),
    path('<int:id>', CategoryRetrieveAPIView.as_view(), name='category')
]
