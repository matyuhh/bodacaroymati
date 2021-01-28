"""boda URL Configuration

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
from django.contrib import admin
from django.urls import path
from bodapp import views, urls
from django.conf.urls import include

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('admin/', admin.site.urls),
    #path('bodapp/', include('bodapp.urls')),
    path('registro/',views.registro,name='registro'),
    path('viaje/', views.ViajeView.as_view(), name='viaje'),
    path('fotos/', views.FotosView.as_view(), name='fotos'),
    path('boda/', views.BodaView.as_view(), name='boda'),
    path('regalos/', views.RegalosView.as_view(), name='regalos'),
]
