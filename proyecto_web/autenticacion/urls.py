from django.urls import path
from .views import VRegistro, cerrar_sesion, login_usuario

urlpatterns = [
    path('', VRegistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('login_usuario', login_usuario, name="login_usuario"),
]

