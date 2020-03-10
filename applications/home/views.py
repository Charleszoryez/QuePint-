from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Inicio(TemplateView):
    template_name = 'index.html'
    
class Login(TemplateView):
    template_name = 'login.html'

class Favoritos(TemplateView):
    template_name = 'favoritos.html'

class Ficha(TemplateView):
    template_name = 'ficha.html'

class CrearEvento(TemplateView):
    template_name = 'crear-evento.html'

class Resultado(TemplateView):
    template_name = 'resultado.html'
