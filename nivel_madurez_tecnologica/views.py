from datetime import datetime
from django.shortcuts import redirect, render
from Cuestionario.models import *

def login(request):
    return render(request, 'login.html')

def registrar(request):
    return render(request, 'registro.html')



def inicio(request):
    return render (request, 'inicio.html')

def guardar_registro(request):
    registro=Registro()
    registro.nombre=request.POST.get('nombre')
    registro.nombre_proyecto=request.POST.get('nombre_proyecto')
    registro.correo_electronico=request.POST.get('correo')
    registro.institucion=request.POST.get('institucion')
    registro.categoria=request.POST.get('categoria')
    registro.fecha=datetime.now()
    registro.save()
    return redirect ('investigacion')

def investigación(request):
    return render(request, 'investigacion.html')

#def guardar_investigacion(request):

def desarrollo(request):
    return render(request, 'desarrollo.html')

#def guardar_desarrollo(request): 

def integracion(request):
    return render(request, 'integracion.html')

#def guardar_integracion(request):

def propiedad(request):
    return render(request, 'propiedad.html')

#def guardar_propiedad(reuqest):

def normatividad(request):
    return render(request, 'normatividad.html')

#def guardar_normatividad(request):

def manufactura(request):
    return render(request, 'manufactura.html')

#def guardar_manufactura(request):
    
def usuarios_producto(request):
    return render(request, 'usuarios_producto.html')

#def guardar_usuarios_producto(request):

def aspectos(request):
    return render(request, 'aspectos.html')

#def guardar_aspectos(request):

def resultados(request):
    return render(request,'resultados.html')
