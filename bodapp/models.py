from django.db import models


# Create your models here.

class Invitado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    si_viene = models.BooleanField()
    extra_invitado = models.CharField(max_length=60)
    mensaje = models.CharField(max_length=255)