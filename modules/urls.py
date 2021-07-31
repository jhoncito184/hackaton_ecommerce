from django.urls import path
from .views import ModulesListAPIView, ModulesRetrieveAPIView

urlpatterns = [
    path('', ModulesListAPIView.as_view(), name='modules'),
    path('<int:id>', ModulesRetrieveAPIView.as_view(), name='modules')
]
