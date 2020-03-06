from django.urls import path, re_path
from .views import *

#from . import views
#app_name="home_app"

urlpatterns = [
    path('',home, name = 'index'),
    path('login/',login, name = 'login'),
    path('favoritos/',favoritos, name = 'favoritos'),
    path('ficha/',ficha, name = 'ficha'),
    path('crearevento/',crearevento, name = 'crearevento'),
    path('resultado/',resultado, name = 'resultado'),
]
