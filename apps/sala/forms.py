from django import forms
from apps.sala.models import Sala, Silla
class SalaForm(forms.ModelForm):
    class Meta: 
        model=Sala
        fields= [
            'numero' ,
            'cap_general',
            'cap_primera_clase',
            'cap_discapacitados',
            'tipo_formato',
            'teatro',
        ]

        labels={
            'numero' :'Numero de Sala',
            'cap_general': 'Capacidad en clase general',
            'cap_primera_clase' : 'Capacidad en primera clase',
            'cap_discapacitados':'Capacidad para discapacitados' ,
            'tipo_formato' : 'Tipo de Sala',
            'teatro': 'Teatro',
        }

        widgets={
            'numero': forms.NumberInput(attrs={'class':'form-control'}),
            'cap_general': forms.NumberInput(attrs={'class':'form-control'}),
            'cap_primera_clase': forms.NumberInput(attrs={'class':'form-control'}),
            'cap_discapacitados': forms.NumberInput(attrs={'class':'form-control'}),
            'tipo_formato': forms.Select(attrs={'class': 'form-control'}),
            'teatro': forms.Select(attrs={'class':'form-control'})
        }

class SearchForm(forms.Form):
    search = forms.CharField(max_length=20)
    
