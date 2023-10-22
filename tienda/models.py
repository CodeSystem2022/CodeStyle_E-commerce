from django.db import models

# Create your models here.
'''
class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="categoriaProd"
        verbose_name_plural="categoriasProd"

    def __str__(self):
        return self.nombre
'''

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    #categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    img_url=models.ImageField(upload_to="tienda", null=True, blank=True)
    precio_por_porcion=models.FloatField()
    calorias_por_porcion=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    #created=models.DateTimeField(auto_now_add=True)
    #updated=models.DateTimeField(auto_now_add=True)

  

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"