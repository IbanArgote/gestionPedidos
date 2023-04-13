from django.db import models

class Pedido(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    fecha = models.DateField()
    cif = models.CharField(max_length=100)
    nombre_empresa = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    datos_contacto = models.CharField(max_length=100)
    producto =  models.ManyToManyField(Producto) 
    cantidad = models.IntegerField()
    precio_total = models.FloatField()

class Componente(models.Model):
    codigo_referencia = models.CharField(max_length=100)
    nombre_modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)

class Producto(models.Model):
    referencia = models.CharField(max_length=100, unique=True)
    precio = models.FloatField()
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    componentes = models.ManyToManyField(Componente)    	