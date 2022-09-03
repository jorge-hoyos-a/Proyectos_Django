from ssl import SSLCertVerificationError
from django.contrib import admin
from .models import Servicio

# Register your models here.
class Servicio_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display=("id", "titulo", "contenido", "imagen", "created", "updated")
    
admin.site.register(Servicio, Servicio_admin)
