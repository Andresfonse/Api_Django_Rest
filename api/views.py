from rest_framework import viewsets
from .serializer import ClientesSerializer, FacturaSerializer, ProveedoresSerializer, CategoriasSerializer, ProductosSerializer, VentasSerializer
from .models import Clientes, Factura, Proveedores, Categorias, Productos, Ventas

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer 

class FacturasViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()  # Corregir el nombre del modelo a Factura
    serializer_class = FacturaSerializer 

class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializer 

class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer 

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class VentasViewSet(viewsets.ModelViewSet):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializer