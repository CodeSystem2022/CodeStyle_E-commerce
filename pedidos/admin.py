from django.contrib import admin

from .models import Pedidos, DetallePedido

# Register your models here.

admin.site.register([Pedidos, DetallePedido])
