from django.http import HttpResponse
from django.shortcuts import render
from gestion_ped.models import Articulos
from django.conf import settings
from django.core.mail import send_mail
from gestion_ped.forms import Formulario_contacto

# Create your views here.
def busqueda_productos(request):
    return render(request, "busq_prod.html")

def buscar(request):
    if request.GET["prd"]:
        #mensaje = "Artículo buscado: %r" %request.GET["prd"]
        producto = request.GET["prd"]
        
        if len(producto)>20:
            mensaje = "Texto de búsqueda demasiado largo"
        else:
            articulos = Articulos.objects.filter(nombre__icontains=producto)
            return render(request, "resultados_busqueda.html", {"articulos": articulos, "query": producto})
    else:
        mensaje = "No has introducido nada"
    return HttpResponse(mensaje)

def contacto(request):
    if request.method =="POST":
        form1 = Formulario_contacto(request.POST)
        if form1.is_valid():
            info1 = form1.cleaned_data
            send_mail(info1['asunto'], info1['mensaje'], info1.get('email','direccion en el servidor'), ['correo al que se quiere enviar la info del formulario'],)
            return render(request, 'gracias.html')
    else:
        form1 = Formulario_contacto()
    
    return render(request, "formulario_contacto.html", {"form": form1})
            
        
        
"""subject = request.POST["asunto"]
message = request.POST["mensaje"] + " " + request.POST["email"]
email_from = settings.EMAIL_HOST_USER
recipient_list = ["jorandho@gmail.com"]
send_mail (subject, message, email_from, recipient_list)
return render(request, "gracias.html")
return render(request, "contacto.html")"""