from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from django.db import models
from apps.teatro.models import Teatro

# Create your models here.
class Sala(models.Model):

    formatos= [
        ('2d', 'Sala 2D'),
        ('3d', 'Sala 3D'),
        ('4d', 'Sala 4D'),
        ('mega', 'Megasala'),
        ('vip', 'Sala VIP'),
    ]
    numero = models.PositiveSmallIntegerField(validators=[MinValueValidator(1,'El número de la sala debe ser mayor 1')])
    cap_general= models.PositiveSmallIntegerField()
    cap_primera_clase= models.PositiveSmallIntegerField()
    cap_discapacitados= models.PositiveSmallIntegerField()
    tipo_formato= models.CharField(max_length=4, 
                                    choices=formatos,
                                    default='2d')
    teatro= models.ForeignKey(Teatro, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return 'Sala {} - {}'.format(self.numero, self.teatro)

    class Meta: 
        unique_together=(('numero', 'teatro'))



class Silla(models.Model): 
 
    DISCAPACITADOS= _('DISCAPACITADOS')
    GENERAL= _('GENERAL')
    PRIMERA= _('PRIMERA CLASE')


    sala= models.ForeignKey(Sala, null=True, blank= False, on_delete=models.CASCADE) 
    pos_x= models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    pos_y= models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    tipo= models.CharField(max_length=20)
    nombre= models.CharField(max_length=10, default= '')


    def __str__(self):
        return ''.format(self.nombre) 

    

    