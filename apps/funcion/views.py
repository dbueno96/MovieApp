from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.funcion.models import Funcion
from apps.persona.models import Empleado, Jefe
from apps.sala.models import Sala
from apps.funcion.forms import FuncionForm

# Create your views here.


class FuncionCreate(LoginRequiredMixin,CreateView):
    model=Funcion
    form_class= FuncionForm
    template_name= 'funcion_form.html'
    success_url= reverse_lazy('funcion:listar_funcion')
    login_url=reverse_lazy('login')


class FuncionUpdate(LoginRequiredMixin,UpdateView):
    model=Funcion
    form_class= FuncionForm
    template_name= 'funcion_form.html'
    success_url= reverse_lazy('funcion:listar_funcion')
    login_url=reverse_lazy('login')

    
class FuncionList(LoginRequiredMixin,ListView):
    model= Funcion
    template_name= 'funcion_list.html'
    paginate_by=6
    login_url=reverse_lazy('login')


    def get_queryset(self): 
        user= self.request.user
        
        if user.is_superuser: 
            return Funcion.objects.all()
        
        user= Jefe.objects.get(persona=user.id)
        print('User= {}'.format(user))

        if user.is_boss: 
            return Funcion.objects.filter(teatro=user.teatro)
        
        else:
            return None

class FuncionDelete(LoginRequiredMixin,DeleteView):
    model= Funcion
    template_name='funcion_delete.html'
    success_url=reverse_lazy('funcion:listar_funcion')
    login_url=reverse_lazy('login')


def salas_ajax(request):
    teatro= request.GET.get('teatro')
    try: 
        salas = Sala.objects.filter(teatro=teatro).values()
        print('SALAS===={}'.format(salas))
        return JsonResponse(list(salas), safe=False)
    except NameError: 
        return JsonResponse({'error': 500})