from django.db import models
from django.core.validators import MinValueValidator
from django_countries.fields import CountryField
from apps.persona.models import Persona
from datetime import time
# Create your models here.


class Pelicula(models.Model): 
    generos= [
        ('acc', 'Acción'),
        ('dr', 'Drama'),
        ('com', 'Comedia'),
        ('ter', 'Terror'),
        ('th', 'Thriller'),
        ('inf', 'Infantil')
    ]
    en_cartelera= models.BooleanField(default=False)
    es_estreno= models.BooleanField(default=False)
    nombre = models.CharField(max_length= 25)
    duracion= models.TimeField(default=time(0,0,0))
    sinopsis= models.CharField(max_length=300, default='Sinopsis pendiente')
    genero= models.CharField(max_length=5,
                            choices=generos)
    pais = CountryField(max_length=15) 
    director = models.ForeignKey(Persona, on_delete=models.CASCADE, null= True, blank=False)  
    imagen= models.ImageField(upload_to='pelicula/', default='pelicula/default.png')
    trailer=models.CharField(max_length=20, blank=True)
   
   
    def __str__(self): 
        return '{}'.format(self.nombre)
        

