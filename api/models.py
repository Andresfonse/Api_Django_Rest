from django.db import models

# Create your models here.

#class Programmer(models.Model):
#    fullname = models.CharField(max_length=100)
#    nickname = models.CharField(max_length=50)
#    age = models.PositiveSmallIntegerField()
#    is_active = models.BooleanField(default=True)

# Modificaciones para la API

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    
    def __str__(self):
        return self.nombre
    
class Factura(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.fecha} - {self.cliente}"
    
    

class Proveedores(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    
    def __str__(self):
        return self.nombre

class Categorias(models.Model):
    nombre = models.CharField(max_length=50, default=True)
    descripcion = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Productos(models.Model):
    nomProducto = models.CharField(max_length=50, verbose_name="Nombre del Producto")
    desProducto = models.CharField(max_length=200, verbose_name="Descripcion del Producto")
    catProducto = models.ForeignKey(Categorias, on_delete=models.CASCADE, verbose_name="categoria del Producto")
    canProducto = models.PositiveIntegerField(default=True, verbose_name="Cantidad del Producto")
    precioProducto = models.PositiveBigIntegerField(default=True)
    estProducto = models.BooleanField(default=True)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.nomProducto

class Ventas(models.Model):
    cantidad = models.CharField(max_length=20)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    
    
