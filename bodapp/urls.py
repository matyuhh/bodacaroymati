from django.urls import path
from bodapp import views

urlpattern = [
    path('registro/',views.registro,name='registro'),
    path('viaje/', views.ViajeView.as_view(), name='viaje'),
    path('fotos/', views.FotosView.as_view(), name='fotos'),
    path('boda/', views.BodaView.as_view(), name='boda'),
    path('regalos/', views.RegalosView.as_view(), name='regalos'),
]