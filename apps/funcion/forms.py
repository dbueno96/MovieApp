from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from django.db.models import Q
from apps.funcion.models import Funcion

class HourInput(forms.TimeInput):
    input_type='time'

class FuncionForm(forms.ModelForm):
    class Meta: 

        model= Funcion
        fields= [
            'fecha',
            'hora_inicio',
            'empleado',
            'sala',
            'pelicula'
        ]

        labels= {
            'fecha': 'Fecha', 
            'hora_inicio': 'Hora de Inicio', 
            'empleado': 'Empleado en Sillas', 
            'pelicula': 'Película'
        }

        widgets={
            'fecha': forms.SelectDateWidget(attrs={'class':'form-control'},
                                            years= range(2020, 2031),
                                            months= {
                                                1:_('Enero'), 2:_('Febrero'), 3:_('Marzo'), 4:_('Abril'),
                                                5:_('Mayo'), 6:_('Junio'), 7:_('Julio'), 8:_('Agosto'),
                                                9:_('Septiembre'), 10:_('Octubre'), 11:_('Noviembre'), 12:_('Diciembre')
                                            },empty_label=("Choose Year", "Choose Month", "Choose Day"),),
            'hora_inicio': HourInput(attrs={'class':'form-control'}),
            'empleado': forms.Select(attrs={'class': 'form-control'}),
            'pelicula': forms.Select(attrs={'class': 'form-control'}),
        }


    
    def clean(self): 
        cleaned_data = self.cleaned_data
        sala= cleaned_data.get('sala')
        fecha= cleaned_data.get('fecha')
        hora_inicio = cleaned_data.get("hora_inicio")
        hora_fin = cleaned_data.get('hora_final')
        conflict=None
        if self.instance:
            print('if')
            conflict = Funcion.objects.filter(sala=sala).filter(fecha=fecha).filter(
                            Q(hora_inicio__lte=hora_inicio, hora_final__gte=hora_inicio) |
                            Q(hora_inicio__lte=hora_inicio, hora_final__gte=hora_inicio)
            ).exclude(pk=self.instance.id)
        else: 
            print('else')
            conflict = Funcion.objects.filter(sala=sala).filter(fecha=fecha).filter(
                            Q(hora_inicio__lte=hora_inicio, hora_final__gte=hora_inicio) |
                            Q(hora_inicio__lte=hora_inicio, hora_final__gte=hora_inicio)
            )
        if conflict: 
            raise ValidationError(
                _('Sala no disponible a esta hora: %(hora_inicio)s '),
                params={'hora_inicio': hora_inicio}) 