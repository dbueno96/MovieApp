from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from apps.pelicula.models import Pelicula
from apps.pelicula.forms import PeliculaForm
# Create your views here.


def index(request):
    return render(request, 'index.html')

class PeliculaList(LoginRequiredMixin,ListView): 
    model = Pelicula
    login_url=reverse_lazy('login')
    template_name= 'pelicula_list.html'

class PeliculaCreate(LoginRequiredMixin,CreateView): 
    model= Pelicula
    login_url=reverse_lazy('login')
    template_name= 'pelicula_form.html'
    success_url=reverse_lazy('pelicula:listar_pelicula')
    form_class= PeliculaForm



class PeliculaUpdate(LoginRequiredMixin,UpdateView):
    model= Pelicula
    login_url=reverse_lazy('login')
    template_name= 'pelicula_form.html'
    success_url=reverse_lazy('pelicula:listar_pelicula')
    form_class=PeliculaForm

class PeliculaDelete(LoginRequiredMixin,DeleteView): 
    model=Pelicula
    login_url=reverse_lazy('login')
    template_name='pelicula_delete.html'
    success_url=reverse_lazy('pelicula:listar_pelicula')
    