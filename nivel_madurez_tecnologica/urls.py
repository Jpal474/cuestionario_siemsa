"""nivel_madurez_tecnologica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from . import views
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('administrador/', include('Administrador.urls')),
    path('administrador/', include('django.contrib.auth.urls')),
    path('inicio/', views.inicio, name="home"),
    path('guardar_registro/', views.guardar_registro, name="guardar_registro"),
    path('investigacion/', views.investigación, name="investigacion"),
    path('guardar_investigacion/', views.guardar_investigacion, name="guardar_investigacion"),
    path('desarrollo/', views.desarrollo, name="desarrollo"), 
    path('guardar_desarrollo/', views.guardar_desarrollo, name="guardar_desarrollo"),
    path('integracion_tecnologica/', views.integracion, name="integracion"),
    path('guardar_integracion/', views.guardar_integracion, name="guardar_integracion"),
    path('propiedad_intelectual/', views.propiedad, name="propiedad"),
    path('guardar_propiedad/', views.guardar_propiedad, name="guardar_propiedad"),
    path('normatividad/', views.normatividad, name="normatividad"),
    path('guardar_normatividad/', views.guardar_normatividad, name="guardar_normatividad"),
    path('manufactura/', views.manufactura, name="manufactura"),
    path('guardar_manufactura/', views.guardar_manufactura, name="guardar_manufactura"),
    path('usuarios_producto/', views.usuarios_producto, name="usuarios"),
    path('guardar_usuarios_producto/', views.guardar_usuarios_producto, name="guardar_usuarios"),
    path('aspectos_organizativos/', views.aspectos, name="aspectos"),
    path('guardar_aspectos_organizativos/', views.guardar_aspectos, name="guardar_aspectos"),
    path('resultados/', views.resultados, name="resultados"),
    
]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
