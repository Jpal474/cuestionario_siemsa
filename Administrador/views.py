from django.shortcuts import render, redirect


def inicio(request):
    return render(request, 'inicio_admin.html')

def cuestionario(request):
    return render (request, 'inicio_cuestionario.html')

def investigacion(request):
    return render (request, 'ver_investigacion.html')

def editar_investigacion(request):
    return render (request, 'editar_investigacion.html')

def ver_usuarios(request):
    return render (request, 'usuarios.html')

def respuestas(request):
    return render (request, 'respuestas.html')

def nomenclatura(request):
    return render (request, 'nomenclatura.html')

def preguntas_investigacion(request):
    return render (request, 'preguntas_investigacion.html')

def preguntas_desarrollo(request):
    return render (request, 'preguntas_desarrollo.html')

def preguntas_integracion(request):
    return render (request, 'preguntas_integracion.html')

def preguntas_propiedad(request):
    return render (request, 'preguntas_propiedad.html')

def preguntas_normatividad(request):
    return render (request, 'preguntas_normatividad.html')

def preguntas_manufactura(request):
    return render (request, 'preguntas_manufactura.html')

def preguntas_usuarios(request):
    return render (request, 'preguntas_usuarios.html')

def preguntas_aspectos(request):
    return render (request, 'preguntas_aspectos.html')
