from rest_framework import serializers
from .models import Clientes, Factura, Proveedores, Categorias, Productos, Ventas


#la importacion Programmer si quieres activar denuevo la clase

#class ProgrammerSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Programmer
#        fields = '__all__'

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'
        
class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'
        
class ProveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = '__all__'
        
class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'
        
class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class VentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ventas
        fields = '__all__'