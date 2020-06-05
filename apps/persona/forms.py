from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _
from apps.persona.models import Empleado, Persona,Jefe,User


class UserForm(forms.ModelForm):
    class Meta: 
        model= User 
        fields=[
            'first_name',
            'last_name',
            'email'
        ]

        labels={
            'first_name': 'Nombres',
            'last_name':'Apellidos',
            'email': 'E-mail',
        }

        widgets={
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),

        }
    def clean(self): 
        cleaned = super().clean() 
        if 'username' not in cleaned: 
            cleaned['username']= cleaned['cedula']
        if 'password1' not in cleaned: 
            cleaned['password1']= cleaned['cedula']
        if 'password2' not in cleaned: 
            cleaned['password2']= cleaned['cedula']

        print(cleaned)

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model= Empleado
        fields= [
            'is_staff',
            'jefe',
            'cargo' 
        ]
        labels= {
            'is_staff': '¿Es Emplead@',
            'jefe': 'Jefe Encargado',
            'cargo': 'Cargo' 
        }

        widgets={
            'is_staff': forms.CheckboxInput(),
            'jefe': forms.Select(attrs={'class':'form-control'}),
            'cargo': forms.Select(attrs={'class': 'form-control'})    
        }


class JefeForm(forms.ModelForm):
    class Meta: 
        model=Jefe
        fields =[
            'is_boss',
            'teatro'
        ]

        labels={
            'is_boss': '¿Es jefe?',
            'teatro': 'Teatro a cargo'
        }

        widgets={
            'is_boss': forms.CheckboxInput(),
            'teatro': forms.Select(attrs={'class':'form-control'})
        }


class PersonaForm(forms.ModelForm): 
    class Meta:
        model=Persona
        fields= [
            'cedula',
            'nacimiento',
            'celular',
        ]
        labels= {
            'cedula' : 'Identificación',
            'nacimiento': 'Fecha de Nacimiento',
            'celular': 'Celular', 
        }

        widgets={
            'cedula' : forms.TextInput(attrs={'class': 'form-control'}),
            'nacimiento': forms.SelectDateWidget(attrs={'class': 'form-control'},
                                                years= range(1950, 2021),
                                                months= {
                                                    1:_('Enero'), 2:_('Febrero'), 3:_('Marzo'), 4:_('Abril'),
                                                    5:_('Mayo'), 6:_('Junio'), 7:_('Julio'), 8:_('Agosto'),
                                                    9:_('Septiembre'), 10:_('Octubre'), 11:_('Noviembre'), 12:_('Diciembre')
                                                },
                                                empty_label=("Choose Year", "Choose Month", "Choose Day"),),
            'celular':forms.TextInput(attrs={'class':'form-control'}),
        }

  