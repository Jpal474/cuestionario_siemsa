import Administrador.views
from django.urls import path

urlpatterns = [
    path('inicio/', Administrador.views.inicio, name="inicio_administrador"),
    path('cuestionario/', Administrador.views.cuestionario, name="cuetionario_administrador"),
    path('investigacion/', Administrador.views.investigacion, name="investigacion_administrador"),
    path('editar_pregunta/', Administrador.views.editar_investigacion, name="editar_pregunta")

    
]