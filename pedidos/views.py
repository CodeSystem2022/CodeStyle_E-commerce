from django.contrib import messages
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from carro.carro import Carro

from pedidos.models import DetallePedido, Pedidos

from django.template.loader import render_to_string

from django.utils.html import strip_tags

from django.core.mail import send_mail

from .models import Producto


# Create your views here.

'''
@login_required(login_url='/autenticacion/logear')
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user) # damos de alta un pedido
    carro=Carro(request)  # cogemos el carro
    detalle_pedido=list()  # lista con los pedidos para recorrer los elementos del carro
    for key, value in carro.carro.items(): #recorremos el carro con sus items
        detalle_pedido.append(DetallePedido(
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido                 
            ))

    DetallePedido.objects.bulk_create(detalle_pedido) # crea registros en BBDD en paquete
    #enviamos mail al cliente
    enviar_mail(
        pedido=pedido,
        detalle_pedido=detalle_pedido,
        nombreusuario=request.user.username,
        email_usuario=request.user.email
        

    )
    #mensaje para el futuro
    messages.success(request, "El pedido se ha creado correctamente")
    
    #return redirect('../templates/crud/pagos.html')
    return render(request, '../templates/crud/pagos.html')
    #return redirect('listado_productos')
    #return render(request, "tienda/tienda.html",{"productos":productos})
    

def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "detalle_pedido": kwargs.get("detalle_pedido"),
        "nombreusuario":kwargs.get("nombreusuario") 
                       
        })

    mensaje_texto=strip_tags(mensaje)
    from_email="cursos@pildorasinformaticas.es"
    #to=kwargs.get("email_usuario")
    to="aquí la dirección del destinatario"
    send_mail(asunto,mensaje_texto,from_email,[to], html_message=mensaje)

'''

def procesar_pedido(request):
    if request.method == 'POST':
        # toma los datos del formulario de compra
        producto = request.POST['producto']
        cantidad = int(request.post['cantidad'])

        # crea un nuevo pedido en la base de datos
        pedido = Pedidos.objects.create()
        detalle_pedido = DetallePedido.objects.create(
            pedido=pedido,
            producto=producto,
            cantidad=cantidad
        )

        #Agregar calculo del precio total

        return redirect('pagina_de_confirmacion') # Redirigir a una página de confirmación de compra
    return render(request, '../templates/crud/pagos.html') # Renderizar la página de compra