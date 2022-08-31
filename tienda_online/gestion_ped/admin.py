from django.contrib import admin
from gestion_ped.models import Clientes, Articulos, Pedidos


class Clientes_admin(admin.ModelAdmin):
    list_display=("id", "nombre", "direccion", "email")
    search_fields=("nombre", "tfno")
    
class Articulos_admin(admin.ModelAdmin):
    list_display=("id", "nombre", "seccion", "precio")
    list_filter=("seccion", )
    
class Pedidos_admin(admin.ModelAdmin):
    list_display=("id", "numero", "fecha", "entregado")
    list_filter=("fecha",)
    date_hierarchy="fecha"
    
# Register your models here.
admin.site.register(Clientes, Clientes_admin)
admin.site.register(Articulos, Articulos_admin)
admin.site.register(Pedidos, Pedidos_admin)