import Administrador.views
from django.urls import path

urlpatterns = [
    path('inicio/', Administrador.views.inicio, name="inicio_administrador"),
    path('cuestionario/', Administrador.views.cuestionario, name="cuetionario_administrador"),
    path('investigacion/', Administrador.views.investigacion, name="investigacion_administrador"),
    path('editar_pregunta/', Administrador.views.editar_investigacion, name="editar_pregunta"),
    path('login/', Administrador.views.login_user, name="login"),
    path('logout/', Administrador.views.logout_user, name="logout"),
    path('registrar/', Administrador.views.registrar, name="registrar"),
    path('usuarios/', Administrador.views.usuarios, name="ver_usuarios"),
    path('editar_usuario/<int:id>', Administrador.views.editar_usuario, name="editar_usuario"),
    path('eliminar_usuario/<int:id>', Administrador.views.eliminar_usuario, name="eliminar_usuario"),

    
]