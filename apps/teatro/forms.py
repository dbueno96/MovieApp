from django import forms
from apps.teatro.models import Teatro


class TeatroForm(forms.ModelForm):
    class Meta: 
        model = Teatro

        fields= [
            'nombre',
            'ubicacion',
            'ciudad'
        ]

        labels={
            'nombre': 'Nombre del Teatro',
            'ubicacion': 'Ubicación del Teatro',
            'ciudad': 'Ciudad'
        }

        widgets={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
        }
        