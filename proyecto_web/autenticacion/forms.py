from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Form_Registro(UserCreationForm):
    #Crea un formulario de registro personalizado que muestra los campos que aparecen en la bbdd
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']