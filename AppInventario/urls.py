from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


#Se crean las rutas para el acceso al módulo de producción.

urlpatterns = [
    path('', views.dashinventario, name='dashinventario'),
    path('exportar_excel_productos/', views.exportar_excel_productos, name='exportar_excel_productos'),
    path('InventarioCaducidad', views.inventario_caducidad, name='inventario_caducidad'),
    path('InventarioAnalisis', views.inventario_analisis, name='inventario_analisis'),
    path('InventarioProductos', views.inventario_productos, name='inventario_productos'),
    path('InventarioDevoluciones', views.inventario_devoluciones, name='inventario_devoluciones'),
   
]


# Configuración para servir archivos estáticos en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Manejo de errores personalizado
#handler500 = 'cascada.views.server_error'  # Vista para errores de servidor (500)
#handler404 = 'cascada.views.page_not_found'  # Vista para errores 404 (página no encontrada)