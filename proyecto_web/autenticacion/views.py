from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

class VRegistro(View):
    '''Clase que crea el formulario a partir del paquete UserCreationForm'''
    def get(self, request):
        '''Crea el formulario de registro y lo vincula al html registro'''
        form = UserCreationForm()
        return render(request, "registro/registro.html", {"form":form})
    
    def post(self, request):
        '''Gestiona el envío de información a través del formulario'''
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            #Guarda la información del formulario en la variable usuario
            usuario = form.save()
            '''username = request.POST['username']
            password = request.POST['password']
            user =authenticate(request, username=username, password=password)'''
            login(request, usuario)
            return redirect('Home')
        
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            
            return render(request, "registro/registro.html", {"form":form})
        
def cerrar_sesion(request):
    logout(request)
    return redirect('Home')

def login_usuario(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contrasena = form.cleaned_data.get("password")
            
            usuario = authenticate(username= nombre_usuario, password=contrasena)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información incorrecta")
    
    form = AuthenticationForm()
    return render(request, "login/login.html", {"form":form}) 