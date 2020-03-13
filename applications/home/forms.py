from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['name','ci','email','password']
        labels = {
            'name': 'Ingrese el nombre',
            'ci': 'Ingrese Cedula de identidad',
            'email': 'Ingrese email',
            'password': 'Contraseña',
        }

        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class':'form-control filter-input',
                    'placeholder':'Nombre y Apellido',
                    'id': 'name'
                }
            ),
            'ci': forms.TextInput(
                attrs = {
                    'class':'form-control filter-input',
                    'placeholder':'Cedula de identidad',
                    'id': 'ci'
                }
            ),
            'email': forms.TextInput(
                attrs = {
                    'class':'form-control filter-input',
                    'placeholder':'Email',
                    'id': 'email'
                }
            ),
            'password': forms.TextInput(
                attrs = {
                    'class':'form-control filter-input',
                    'placeholder':'Contraseña',
                    'id': 'email'
                }
            ),
        }
