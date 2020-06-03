from django import forms
from durationwidget.widgets import TimeDurationWidget
from django_countries.widgets import CountrySelectWidget
from apps.pelicula.models import Pelicula


class HourInput(forms.TimeInput):
    input_type='time'
    format='%H:%M'

class ImageUpload(forms.widgets.ClearableFileInput):
    def __init__(self, *args, **kwargs): 
        super(ImageUpload, self).__init__(*args, **kwargs)
        self.template_name='image_upload.html'
        self.initial_text='Imagen Actual'
        self.input_text= 'Cambiar Imagen'

     
class PeliculaForm(forms.ModelForm):
    class Meta: 
        model = Pelicula

        fields= [
            'nombre',
            'duracion',
            'genero',
            'pais',
            'director',
            'sinopsis',
            'en_cartelera',
            'es_estreno',
            'imagen',
            'trailer'
        ]

        labels={
            'nombre': 'Nombre',
            'duracion': 'Duración',
            'genero': 'Género',
            'pais': 'Pais',
            'director':'Director',
            'sinopsis': 'Sinopsis',
            'en_cartelera': '¿Publicar en Cartelera?',
            'es_estreno': '¿Está Proxima a Estrenar?',
            'imagen': 'Poster Promocional',
            'trailer': 'Trailer'
        }

        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'duracion': HourInput(attrs={'class':'form-control'}),
            'genero': forms.Select(attrs={'class':'form-control'}),
            'pais': CountrySelectWidget(attrs={'class':'form-control'}),
            'director': forms.Select(attrs={'class':'form-control'}),
            'sinopsis': forms.TextInput(attrs={'class':'form-control'}),
            'en_cartelera': forms.CheckboxInput(attrs={'class':'form-control'}),
            'es_estreno': forms.CheckboxInput(attrs={'class':'form-control'}),
            'imagen': ImageUpload(attrs={'class':'form-control'}), 
            'trailer': forms.TextInput(attrs={'class':'form-control'})
        }