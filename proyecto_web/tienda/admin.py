from django.contrib import admin
from .models import Categoria_prod, Producto

# Register your models here.

class Categoria_prod_admin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("nombre", "created", "updated")

class Producto_admin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("nombre", "categorias", "imagen", "precio", "disponibilidad",  "created", "updated")


admin.site.register(Categoria_prod, Categoria_prod_admin)
admin.site.register(Producto, Producto_admin)