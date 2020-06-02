from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from apps.persona.authForms import LoginForm,PChangeForm
from apps.persona.models import Persona
class Login(LoginView): 
    template_name='auth/login.html'
    authentication_form= LoginForm
    def get(self,request):
        user = request.user
        if not user.is_authenticated: 
            return super(Login,self).get(request)
        else:
            return redirect('/funcion/listar')



class PasswordChange(PasswordChangeView):
    template_name='auth/password_change.html'
    success_url= reverse_lazy('funcion:listar_funcion')
    form_class=PChangeForm



