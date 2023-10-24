from django.contrib import admin

# Register your models here.
from .models import Clientes, InformacionNutricional, Ingredientes, Producto, Usuarios

#admin.site.register(Pedidos)
admin.site.register(Clientes)
#admin.site.register(DetallePedido)
admin.site.register(InformacionNutricional)
admin.site.register(Ingredientes)
admin.site.register(Producto)
admin.site.register(Usuarios)

