# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion_entrega = models.TextField(blank=True, null=True)
    preferencias_alimentarias = models.TextField(blank=True, null=True)
    informacion_medica = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class DetallePedido(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    pedido = models.ForeignKey('Pedidos', models.DO_NOTHING, blank=True, null=True)
    producto = models.ForeignKey('Producto', models.DO_NOTHING, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_pedido'


class InformacionNutricional(models.Model):
    nombre_caloria = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    producto = models.ForeignKey('Producto', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'informacion_nutricional'


class Ingredientes(models.Model):
    id_ingrediente = models.AutoField(primary_key=True)
    nombre_ingrediente = models.CharField(max_length=255, blank=True, null=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredientes'


class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Clientes, models.DO_NOTHING, blank=True, null=True)
    fecha_hora_pedido = models.DateTimeField(blank=True, null=True)
    estado_pedido = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos'


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    calorias_por_porcion = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    precio_por_porcion = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tipo_producto = models.CharField(max_length=255, blank=True, null=True)
    disponibilidad = models.BooleanField(blank=True, null=True)
    img_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    apellido = models.CharField(max_length=255, blank=True, null=True)
    contrasena = models.CharField(max_length=255, blank=True, null=True)
    rol = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
