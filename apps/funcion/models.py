from datetime import time
from django.db import models
from apps.pelicula.models import Pelicula
from apps.sala.models import Sala
from apps.persona.models import Empleado
from apps.teatro.models import Teatro
from apps.funcion.validators import *
# Create your models here.

class Funcion(models.Model): 
    fecha= models.DateField()
    hora_inicio = models.TimeField(default=time(0,0,0))
    hora_final = models.TimeField(null=True)
    empleado =models.ForeignKey(Empleado, null=True, blank=False, on_delete=models.CASCADE)
    teatro= models.ForeignKey(Teatro, blank= True,null=True, on_delete=models.CASCADE)
    sala= models.ForeignKey(Sala, null=True, blank=False, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, null=True, blank=False, on_delete= models.CASCADE)


    def hora_fin(self): 
        duracion= (self.pelicula.duracion.hour, self.pelicula.duracion.minute)
        hora_fin= duracion[0] + self.hora_inicio.hour
       
        
        min_fin = duracion[1] + self.hora_inicio.minute
        if min_fin>=60: 
            min_fin-=60
            hora_fin+=1

        if hora_fin>=24:
            hora_fin-=24

        return time(hora_fin, min_fin,0)


    def save(self, *args, **kwargs):
        self.hora_final = self.hora_fin()
        super(Funcion, self).save(*args, **kwargs)

    
