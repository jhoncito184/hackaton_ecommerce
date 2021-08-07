"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title='Ecommerce Hackaton',
        default_version='v1',
        description='Ven y escoge el curso que más te guste! Juntos aprenderemos!',
        contact=openapi.Contact(email='SV70676142@idat.edu.pe')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('benefits/', include('benefits.urls')),
    path('category/', include('category.urls')),
    path('products/', include('products.urls')),
    path('postulations/', include('postulations.urls')),
    path('products_detail/', include('products_detail.urls')),
    path('schedule/', include('schedule.urls')),
    path('modules/', include('modules.urls')),
    path('modules_detail/', include('modules_detail.urls')),
    path('coupon/', include('coupon.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
