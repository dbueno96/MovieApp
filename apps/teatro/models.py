from django.db import models

# Create your models here.
class Teatro(models.Model): 
    nombre= models.CharField(max_length=30)
    ubicacion=models.CharField(max_length=50) 
    ciudad= models.CharField(max_length=15)


    def __str__(self):
        return '{}'.format(self.nombre)