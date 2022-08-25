from contextvars import Context
from datetime import datetime
from pipes import Template
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request):   # Primera vista
    
    p1 = Persona("Juanito", "Holes")
    #nombre = "Georgito"
    #apellido = "Holes Arbeja"
    
    temas_curso = ["Plantilas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    ahora = datetime.now()
    
    #doc_externo = open("C:/proyectosDjango/proyecto1/proyecto1/plantillas/plantilla.html") 
    #plt = Template(doc_externo.read())
    #doc_externo.close()
    
    #doc_externo = get_template('plantilla.html')
    
    """ctx = Context({"nombre_persona":p1.nombre, 
                    "apellido_persona": p1.apellido,
                    "momento_actual": ahora, 
                    "temas": temas_curso
                    }) #Puede recibir diccionarios u objetos como argumentos"""
                
    ctx = {"nombre_persona":p1.nombre, 
            "apellido_persona": p1.apellido,
            "momento_actual": ahora, 
            "temas": temas_curso
        }
    #documento = doc_externo.render(ctx)
    
    return render(request, "plantilla.html", ctx)

def cursoC(request):
    fecha_actual = datetime.now()
    return render(request, "cursoC.html", {"fecha": fecha_actual})

def cursoPython(request):
    fecha_actual = datetime.now()
    return render(request, "cursoPython.html", {"fecha": fecha_actual})

def despedida(request):
    return HttpResponse('Hasta luego Georgie')

def fecha(request): # vista (view)
    fecha_actual = datetime.now()
    documento =f"""
    <html>
        <body>
            <h1 style='color:blue'>Fecha y hora actuales %s</h1>
        </body>
    </html>
    """ % fecha_actual
    
    return HttpResponse(documento)

def calculaEdad(request, edad, anho):
    periodo = anho - 2022
    edad_futura = edad + periodo
    documento = "<html><body><h2>En el año %s tendras %s años</h2></body></htmml>" %(anho, edad_futura)
    
    return HttpResponse(documento)