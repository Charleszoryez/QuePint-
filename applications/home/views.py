from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from .forms import PersonaForm
from .models import Persona,Evento
# Create your views here.

class Inicio(TemplateView):
    template_name = 'index.html'

class Login(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'login.html'

class Favoritos(TemplateView):
    template_name = 'favoritos.html'

class Ficha(TemplateView):
    template_name = 'ficha.html'

class CrearEvento(TemplateView):
    template_name = 'crear-evento.html'

class Resultado(TemplateView):
    template_name = 'resultado.html'

def crearUsuario(request):
    if request.method == 'POST':
        persona_Form = PersonaForm(request.POST)
        if persona_Form.is_valid():
            persona_Form.save()
            return redirect('home:index')
    else:
        persona_Form = PersonaForm()

    return render(request,'login.html',{'persona_Form':persona_Form})
