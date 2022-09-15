from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido, Linea_Pedido
from carro.carro import Carro
from django.contrib import messages

# Create your views here.

@login_required(login_url="/autenticacion/login_usuario")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = list()
    for key, value in carro.carro.items():
        lineas_pedido.appended(Linea_Pedido(
            producto_id = key, 
            cantidad = value["cantidad"],
            user = request.user,
            pedido =pedido
        ))
        
        # Guardar los datos del pedido en la tabla correspondiente en la bbdd
    Linea_Pedido.objects.bulk_create()
    
    enviar_mail(pedido= pedido,
                lineas_pedido= lineas_pedido,
                nombreusuario = request.username,
                emailusuario = request.usermail
    )
    
    messages.success(request, "El pedido se ha creado correctamente")
    return redirect("../tienda")