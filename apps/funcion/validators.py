from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import time

def validate_sala_disponible(self):
    print('Validating! {}'.format(self))
    # funciones_dia= Funcion.objects.all(sala= )

    if self > time(15,00,00): 
        raise ValidationError(
                _('%(hora)s no disponible en esta sala'),
                params={'hora': self}) 