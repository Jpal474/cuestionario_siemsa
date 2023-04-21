from django.shortcuts import render, redirect
from Administrador.models import Pregunta
from Cuestionario.models import Evaluacion

def inicio(request):
    return render(request, 'inicio_admin.html')

def cuestionario(request):
    return render (request, 'inicio_cuestionario.html')

def investigacion(request):
    return render (request, 'ver_investigacion.html')

def editar_investigacion(request, id):
    pregunta = Pregunta.objects.all()
    post = next(post for post in pregunta if post.id == id)
    return render(request, "editar_investigacion.html", {"pregunta": post})

def actualizar_pregunta(request, id):
    pregunta = Pregunta.objects.all()
    post = next(post for post in pregunta if post.pk == id)
    post.texto = request.POST.get('texto')
    post.save()
    return redirect('cuestionario_administrador')

def ver_usuarios(request):
    return render (request, 'usuarios.html')

def respuestas(request):
    respuesta = Evaluacion.objects.all()
    return render (request, 'respuestas.html',{"respuesta": respuesta})

def eliminar_respuesta(request, id):
    post = Evaluacion.objects.filter(id=id)  # toma el id del curso seleccionado en el modal
    post.delete()
    return redirect('respuestas')

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
