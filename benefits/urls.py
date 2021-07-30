from django.urls import path
from .views import BenefitsListAPIView, BenefitsRetrieveAPIView

urlpatterns = [
    path('', BenefitsListAPIView.as_view(), name='benefits'),
    path('<int:id>', BenefitsRetrieveAPIView.as_view(), name='benefits')
]
