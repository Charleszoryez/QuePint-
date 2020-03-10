from django.urls import path, re_path
from .views import *

#from . import views
#app_name="home_app"

urlpatterns = [
    path('',Inicio.as_view() , name = 'index'),
    path('login/',Login.as_view(), name = 'login'),
    path('favoritos/',Favoritos.as_view(), name = 'favoritos'),
    path('ficha/',Ficha.as_view(), name = 'ficha'),
    path('crearevento/',CrearEvento.as_view(), name = 'crearevento'),
    path('resultado/',Resultado.as_view(), name = 'resultado'),
]

