from django.shortcuts import render, redirect

from.models import Pedidos, DetallePedido

# Create your views here.

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
    return render(request, 'pagos.html') # Renderizar la página de compra