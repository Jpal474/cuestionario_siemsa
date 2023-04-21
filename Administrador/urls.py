import Administrador.views
from django.urls import path

urlpatterns = [
    path('inicio/', Administrador.views.inicio, name="inicio_administrador"),
    path('cuestionario/', Administrador.views.cuestionario, name="cuestionario_administrador"),
    path('investigacion/', Administrador.views.investigacion, name="investigacion_administrador"),
    path('login/', Administrador.views.login_user, name="login"),
    path('logout/', Administrador.views.logout_user, name="logout"),
    path('registrar/', Administrador.views.registrar, name="registrar"),
    path('usuarios/', Administrador.views.usuarios, name="ver_usuarios"),
    path('editar_usuario/<int:id>', Administrador.views.editar_usuario, name="editar_usuario"),
    path('eliminar_usuario/<int:id>', Administrador.views.eliminar_usuario, name="eliminar_usuario"),
    path('editar_pregunta/<int:id>', Administrador.views.editar_investigacion, name="editar_pregunta"),
    path('actualizar_pregunta/<int:id>', Administrador.views.actualizar_pregunta , name="actualizar_pregunta"),
    path('eliminar_respuesta/<int:id>', Administrador.views.eliminar_respuesta , name="eliminar_respuesta"),
    path("respuestas/", Administrador.views.respuestas, name="respuestas"),
    path("nomenclatura/", Administrador.views.nomenclatura, name="nomenclatura"),
    path('preguntas_investigacion/', Administrador.views.preguntas_investigacion, name="preguntas_investigacion"),   
    path('preguntas_desarrollo/', Administrador.views.preguntas_desarrollo, name="preguntas_desarrollo"),   
    path('preguntas_integracion/', Administrador.views.preguntas_integracion, name="preguntas_integracion"),   
    path('preguntas_propiedad/', Administrador.views.preguntas_propiedad, name="preguntas_propiedad"),   
    path('preguntas_normatividad/', Administrador.views.preguntas_normatividad, name="preguntas_normatividad"),   
    path('preguntas_manufactura/', Administrador.views.preguntas_manufactura, name="preguntas_manufactura"),   
    path('preguntas_usuarios/', Administrador.views.preguntas_usuarios, name="preguntas_usuarios"),   
    path('preguntas_aspectos/', Administrador.views.preguntas_aspectos, name="preguntas_aspectos"),        
]