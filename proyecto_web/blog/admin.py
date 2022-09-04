from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

class Categoria_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display=("nombre", "created", "updated")
    
class Post_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display=("titulo", "contenido", "autor", "created", "updated")

admin.site.register(Categoria, Categoria_admin)
admin.site.register(Post, Post_admin)