import datetime 
from django.db import models
from apps.sala.models import Silla
from apps.funcion.models import Funcion

# Create your models here.

class Boleta(models.Model):
    silla = models.ForeignKey(Silla, null=True, on_delete=models.CASCADE)
    funcion= models.ForeignKey(Funcion, null=True, on_delete=models.CASCADE)
    hora_venta= models.DateTimeField(auto_now_add= True)