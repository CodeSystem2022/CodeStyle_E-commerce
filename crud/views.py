from django.shortcuts import render, redirect, HttpResponse

#from.models import Pedidos, DetallePedido

from carro.carro import Carro



# Create your views here.

def home(request):

   carro=Carro(request)
   
   return render(request, '../templates/crud/index.html')

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
'''