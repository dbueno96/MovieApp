from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from apps.teatro.models import Teatro
from apps.teatro.forms import TeatroForm
# Create your views here.

class TeatroCreate(LoginRequiredMixin,CreateView): 
    model=Teatro
    login_url=reverse_lazy('login')
    form_class= TeatroForm
    template_name='teatro_form.html'
    success_url=reverse_lazy('teatro:listar_teatro')


class TeatroUpdate(LoginRequiredMixin,UpdateView): 
    model = Teatro
    login_url=reverse_lazy('login')
    form_class= TeatroForm
    template_name= 'teatro_form.html'
    success_url= reverse_lazy('teatro:listar_teatro')

class TeatroList(LoginRequiredMixin,ListView):
    model =Teatro
    login_url=reverse_lazy('login')
    template_name='teatro_list.html'


class TeatroDelete(LoginRequiredMixin,DeleteView): 
    model= Teatro
    login_url=reverse_lazy('login')
    template_name='teatro_delete.html'
    success_url=reverse_lazy('teatro:listar_teatro')
    