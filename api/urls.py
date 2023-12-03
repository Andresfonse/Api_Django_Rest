from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()  
# router.register(r'programmers', views.ProgrammerViewSet)
router.register(r'clientes', views.ClientesViewSet)
router.register(r'facturas', views.FacturasViewSet)
router.register(r'proveedores', views.ProveedoresViewSet)
router.register(r'categorias', views.CategoriasViewSet)
router.register(r'productos', views.ProductosViewSet)
router.register(r'ventas', views.VentasViewSet)
urlpatterns = [
    path('', include(router.urls))
]
