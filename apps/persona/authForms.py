
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    class Meta: 
        fields= [
            'username',
            'password',
        ]

        labels={
            'username': 'Nombre de Usuario',
            'password': 'Contraseña',
        }




class PChangeForm(PasswordChangeForm): 
    class Meta: 
        fields= [
            'old_password',
            'new_password1',
            'new_password2', 
        ]

        labels={
            'old_password': 'Contraseña Antigua',
            'new_password1': 'Nueva Contraseña',
            'new_password2': 'Confirmación de Nueva Contraseña'
        }