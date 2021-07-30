from django.urls import path
from .views import PostulationsListAPIView, PostulationsRetrieveAPIView

urlpatterns = [
    path('', PostulationsListAPIView.as_view(), name='postulations'),
    path('<int:id>', PostulationsRetrieveAPIView.as_view(), name='postulations')
]
