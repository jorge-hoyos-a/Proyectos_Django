from django.shortcuts import render, redirect
from .forms import Formulario_contacto
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    formulario_contacto = Formulario_contacto()
    
    if request.method=="POST":
        formulario_contacto = Formulario_contacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            
            email = EmailMessage("Mensaje desde app django", 
                                "El ususario con nombre {} con la dirección {} escribe lo siguiente: \n\n{}".format(nombre, email, contenido),
                                "",
                                ["jorandho@gmail.com"],
                                reply_to= [email]
                                )
            
            try:
                email.send()
                return redirect("/contacto/?valido")
            
            except:
                return redirect("/contacto/?novalido")
            
    return render(request, "contacto/contacto.html", {'mi_formulario': formulario_contacto})