import numpy as np
import math
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from apps.sala.models import Sala, Silla
from apps.sala.forms import SalaForm, SearchForm

# Create your views here.


class SalaCreate(LoginRequiredMixin, CreateView): 
    model= Sala
    login_url=reverse_lazy('login')
    form_class= SalaForm
    template_name= 'sala_form.html'
    success_url= reverse_lazy('sala:listar_sala')


    def crearSillas(self, caps, sala): 
        cap_dis, cap_gen, cap_prim = [*caps.values()]
        f1, f2, f3 = 1,8,2
        dis = np.full(cap_dis, '')
        gen = np.full((f2, math.ceil(cap_gen / f2)), '')
        prim= np.full ((f3, math.ceil(cap_prim/f3)), '')

        total= cap_dis+cap_gen+ cap_prim
        fila_actual = 1
        silla_actual=1 
        for i in range(dis.shape[0]): 
            if dis[i] == '':     
                tmp= str(chr(96+fila_actual)).upper()+'-'+ str(i+1)
                silla = Silla()
                silla.sala= sala
                silla.nombre= tmp
                silla.pos_x=i
                silla.pos_y=0
                silla.tipo=Silla.DISCAPACITADOS
                silla.save()
        fila_actual +=1
        for i in range(gen.shape[0]): 
            for col in range(gen.shape[1]):
                if gen[i][col]== '':
                    tmp= str(chr(96+fila_actual)).upper()+'-'+ str(col+1)
                    silla = Silla()
                    silla.sala= sala
                    silla.nombre= tmp
                    silla.pos_x=col
                    silla.pos_y=i
                    silla.tipo=Silla.GENERAL
                    silla.save()
            fila_actual+=1

        for i in range(prim.shape[0]):
            for col in range(prim.shape[1]): 
                if prim[i][col]== '': 
                    tmp= str(chr(96+fila_actual)).upper()+'-'+ str(col+1)
                    silla = Silla()
                    silla.sala= sala
                    silla.nombre= tmp
                    silla.pos_x=col
                    silla.pos_y=i
                    silla.tipo=Silla.PRIMERA
                    silla.save()
            fila_actual+=1
        


    def post(self, request, **kwargs): 
        form = SalaForm(request.POST)
        if form.is_valid():
            pk=form.save()
            cleaned= form.cleaned_data
            caps ={
                'discapacitados': cleaned['cap_discapacitados'],
                'general': cleaned['cap_general'],
                'primera': cleaned['cap_primera_clase']
            }
            
            self.crearSillas(caps, pk)
        return redirect('/sala/listar')

class SalaUpdate(LoginRequiredMixin, UpdateView):
    model=Sala
    login_url=reverse_lazy('login')
    form_class=SalaForm
    template_name='sala_form.html'
    success_url= reverse_lazy('sala:listar_sala')
    
    def post(self, request, **kwargs): 
        super(SalaUpdate, self).post(request,**kwargs)
        return redirect('/sala/listar')



class SalaList(LoginRequiredMixin, ListView):
    model=Sala
    login_url=reverse_lazy('login')
    template_name='sala_list.html'

    

    def get_queryset(self): 
        order_by= self.request.GET.get('order_by' , 'tipo_formato')
        new_context= Sala.objects.all().order_by(order_by)

        return new_context

    

class SalaDelete(LoginRequiredMixin, DeleteView):
    model=Sala
    login_url=reverse_lazy('login')
    template_name='sala_delete.html'
    success_url=reverse_lazy('sala:listar_sala')