from django.db.models import F
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from apps.persona.forms import EmpleadoForm, PersonaForm, JefeForm
from apps.persona.models import Empleado,Persona,Jefe
from apps.pelicula.models import Pelicula
from apps.teatro.models import Teatro 

# Create your views here.




def index(request): 
    context={}
    cartelera = Pelicula.objects.filter(en_cartelera=True)
    teatros = Teatro.objects.filter(nombre= F('nombre'))
    context['teatros']=teatros
    context['cartelera']= cartelera    
    
    return render(request, 'index.html', context)


class EmpleadoCreate(LoginRequiredMixin,CreateView): 
    template_name= 'empleado_form.html'
    form_class= EmpleadoForm
    second_form_class=PersonaForm
    model=Empleado
    login_url=reverse_lazy('login')
    success_url= reverse_lazy('persona:listar_empleado')

    def get_context_data(self, **kwargs): 
        context= super(EmpleadoCreate, self).get_context_data(**kwargs)
        if 'form' not in context: 
            context['form']=self.form_class(self.request.GET)
        if 'form2' not in context: 
            context['form2'] =self.second_form_class(self.request.GET) 
        
        return context

    def post(self, request, *args, **kwargs):
        self.object= self.get_object
        form = self.form_class(request.POST)
        form2= self.second_form_class(request.POST)
       
        if form.is_valid() and form2.is_valid():
            jefe= form.save(commit=False)
            jefe.persona= form2.save()
            jefe.persona.username= form2.cleaned_data['cedula']
            jefe.persona.set_password(form2.cleaned_data['cedula'])
            jefe.persona.save()
            jefe.save()
            return redirect(self.get_success_url())
        else: 
            print(form2.is_valid())
            print(form.is_valid())
            print(form2.cleaned_data)

            return render(request, 'jefe_form.html', 
                            context= self.get_context_data(form=form, form2=form2))

class EmpleadoList(LoginRequiredMixin,ListView): 
    model = Empleado
    login_url=reverse_lazy('login')
    template_name= 'empleado_list.html'



class EmpleadoUpdate(LoginRequiredMixin,UpdateView): 
    model=Empleado
    login_url=reverse_lazy('login')
    template_name='empleado_form.html'
    success_url= reverse_lazy('persona:listar_empleado')
    form_class=EmpleadoForm

class EmpleadoDelete(LoginRequiredMixin,DeleteView):
    model=Empleado
    login_url=reverse_lazy('login')
    template_name='empleado_delete.html'
    success_url=reverse_lazy('persona:listar_empleado')



class JefeCreate(LoginRequiredMixin,CreateView): 
    template_name= 'jefe_form.html'
    form_class= JefeForm
    second_form_class=PersonaForm
    model=Jefe
    login_url=reverse_lazy('login')
    success_url= reverse_lazy('persona:listar_jefe')

    def get_context_data(self, **kwargs): 
        context= super(JefeCreate, self).get_context_data(**kwargs)
        print('getting c data')
        if 'form' not in context: 
            print('form in context')
            context['form']= self.form_class(self.request.GET)
        
        if 'form2' not in context: 
            print('form2 in context')
            context['form2']= self.second_form_class(self.request.GET)
             
        return context

    

    def post(self, request, *args, **kwargs):
        self.object= self.get_object
        form = self.form_class(request.POST)
        form2= self.second_form_class(request.POST)
       
        if form.is_valid() and form2.is_valid():
            jefe= form.save(commit=False)
            jefe.persona= form2.save()
            jefe.persona.username= form2.cleaned_data['cedula']
            jefe.persona.set_password(form2.cleaned_data['cedula'])
            jefe.persona.save()
            jefe.save()
            return redirect(self.get_success_url())
        else: 
            return render(request, 'jefe_form.html', 
                            context= self.get_context_data(form=form, form2=form2))



class JefeList(LoginRequiredMixin,ListView): 
    model = Jefe
    login_url=reverse_lazy('login')
    template_name= 'jefe_list.html'



class JefeUpdate(LoginRequiredMixin,UpdateView): 
    model=Jefe
    login_url=reverse_lazy('login')
    second_model= Persona
    template_name='jefe_form.html'
    success_url= reverse_lazy('persona:listar_jefe')
    form_class=JefeForm
    second_form_class= PersonaForm

    def get_context_data(self, **kwargs): 
        context= super(JefeUpdate, self).get_context_data(**kwargs)
        pk= self.kwargs.get('pk',0)
        jefe= self.model.objects.get(id=pk)
        persona= self.second_model.objects.get(id= jefe.persona_id)
        if 'form' not in context: 
            context['form']= self.form_class()
        if 'form2'not in context: 
            context['form2']= self.second_form_class(instance=persona)
        context['id']= pk

        return context

   


class JefeDelete(LoginRequiredMixin,DeleteView):
    model=Jefe
    login_url=reverse_lazy('login')
    template_name='jefe_delete.html'
    success_url=reverse_lazy('persona:listar_jefe')





class PersonaCreate(LoginRequiredMixin,CreateView): 
    template_name= 'persona_form.html'
    form_class= PersonaForm
    model=Persona
    login_url=reverse_lazy('login')
    success_url= reverse_lazy('persona:listar_persona')


class PersonaList(LoginRequiredMixin,ListView): 
    model = Persona
    login_url=reverse_lazy('login')
    template_name= 'persona_list.html'



class PersonaUpdate(LoginRequiredMixin,UpdateView): 
    model=Persona
    login_url=reverse_lazy('login')
    template_name='persona_form.html'
    success_url= reverse_lazy('persona:listar_persona')
    form_class=PersonaForm

class PersonaDelete(LoginRequiredMixin,DeleteView):
    model=Persona
    login_url=reverse_lazy('login')
    template_name='persona_delete.html'
    success_url=reverse_lazy('persona:listar_persona')


