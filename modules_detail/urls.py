from django.urls import path
from .views import ModulesDetailListAPIView, ModulesDetailRetrieveAPIView

urlpatterns = [
    path('', ModulesDetailListAPIView.as_view(), name='modules_detail'),
    path('<int:id>', ModulesDetailRetrieveAPIView.as_view(), name='modules_detail')
]
