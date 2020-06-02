from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.funcion.models import Funcion
from apps.funcion.forms import FuncionForm

# Create your views here.

class FuncionCreate(LoginRequiredMixin,CreateView):
    model=Funcion
    form_class= FuncionForm
    template_name= 'funcion/funcion_form.html'
    success_url= reverse_lazy('funcion:listar_funcion')
    login_url=reverse_lazy('login')


class FuncionUpdate(LoginRequiredMixin,UpdateView):
    model=Funcion
    form_class= FuncionForm
    template_name= 'funcion/funcion_form.html'
    success_url= reverse_lazy('funcion:listar_funcion')
    login_url=reverse_lazy('login')

    
class FuncionList(LoginRequiredMixin,ListView):
    model= Funcion
    template_name= 'funcion/funcion_list.html'
    paginate_by=6
    login_url=reverse_lazy('login')


class FuncionDelete(LoginRequiredMixin,DeleteView):
    model= Funcion
    template_name='funcion/funcion_delete.html'
    success_url=reverse_lazy('funcion:listar_funcion')
    login_url=reverse_lazy('login')
