from django.shortcuts import render

# Create your views here.

"""
from django.views.generic import (
    TemplateView,
)

class IndexView(TemplateView):
    template_name = "index.html"

"""
def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def favoritos(request):
    return render(request,'favoritos.html')

def ficha(request):
    return render(request,'ficha.html')

def crearevento(request):
    return render(request,'crear-evento.html')

def resultado(request):
    return render(request,'resultado.html')