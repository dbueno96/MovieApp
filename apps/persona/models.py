from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.teatro.models import Teatro
# Create your models here.



class User(AbstractUser): 
    REQUIRED_FIELDS= [
        'first_name',
        'last_name', 
        'email',
        'is_active',
    ]    
    USERNAME_FIELD='username'
    
class Persona(models.Model):

    cedula= models.CharField(max_length=20, unique=True)
    celular=models.CharField(max_length=20)
    nacimiento = models.DateField()
    

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Cliente(models.Model):
 
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, null=True, related_name='cliente')
    saldo= models.DecimalField(max_digits=8, decimal_places=2)
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='cliente_user')
    def __str__(self):
        return '{}'.format(self.persona)

class Jefe(models.Model): 
    persona=models.OneToOneField(Persona, on_delete=models.CASCADE, null=True, related_name='jefe')
    user=models.OneToOneField(User, on_delete=models.CASCADE, null= True, related_name='jefe_user')
    is_boss= models.BooleanField(default=True) 
    teatro= models.OneToOneField(Teatro, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self): 
        return '{} -- {}'.format(self.persona, self.persona.cedula )

class Empleado(models.Model):
    cargos= [
        ('ta', 'Taquilla'),
        ('co', 'Comidas'),
        ('si', 'Sillas'),
    ]
    persona= models.OneToOneField(Persona,on_delete=models.CASCADE,null=True, related_name='empleado')
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='empleado_user')
    is_staff= models.BooleanField(default=True)
    jefe = models.ForeignKey(Jefe, null=True, blank=True, on_delete=models.CASCADE, related_name='empleado_jefe')
    cargo = models.CharField(max_length=3,
                            choices=cargos,
                            default='Taquillero')

    def __str__(self): 
        return '{} -- {}'.format(self.persona, self.persona.cedula)