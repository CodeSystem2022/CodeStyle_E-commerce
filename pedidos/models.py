from django.db import models
from tabnanny import verbose

from django.contrib.auth import get_user_model #devuelve el usuario activo actual
from django.db.models import F,Sum, FloatField  # para calcular el total de una orden de pedido
from tienda.models import Producto

User=get_user_model()

# Create your models here.

class DetallePedido(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    pedido = models.ForeignKey('Pedidos', models.DO_NOTHING, blank=True, null=True)
    producto = models.ForeignKey(Producto, models.DO_NOTHING, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_pedido'


class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    #cliente = models.ForeignKey(Clientes, models.DO_NOTHING, blank=True, null=True)
    fecha_hora_pedido = models.DateTimeField(auto_now_add=True)
    estado_pedido = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos'