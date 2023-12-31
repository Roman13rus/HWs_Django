"""api_with_restrictions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from advertisements.views import AdvertisementViewSet
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('advertisements', AdvertisementViewSet)
# TODO: подключите `AdvertisementViewSet`
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]

# ee01c95299a852d168f8f56758953ca47463b69b
# d4a1289ec196fc6752bcaf753c431b624a9ba142