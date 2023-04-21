from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from Administrador.models import Pregunta
from Cuestionario.models import Evaluacion

def login_user(request):
    if request.method=="POST":
        print("entré")
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('inicio_administrador')
        else:
            messages.error(request, ("Hubo un error al iniciar sesión, intente de nuevo"))
            return render(request, "authentication/login.html")
    else:
        return render(request, 'authentication/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("Fuite deslogueado exitosamente!"))
    return redirect('login')

def registrar(request):
    if request.method=="POST":
        username=request.POST.get("nombreu")
        name=request.POST.get("nombre")
        lastname=request.POST.get("apellido")
        mail=request.POST.get("correo")
        password=request.POST.get("contraseña")
        password2=request.POST.get("contraseña2")
        if password == password2:
            user=User.objects.create_user(username, mail, password)
            user.first_name=name
            user.last_name=lastname
            user.save()
            return redirect ('inicio_administrador')
        else:
            messages.error(request, ("Hubo un error al hacer el registro, intente de nuevo"))    
            return redirect ('registrar')

    else:
         return render(request, 'registro.html')

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

def usuarios(request):
    usuarios=User.objects.all()
    return render(request, "lista_usuarios.html", {"usuarios":usuarios})

def editar_usuario(request, id):
    if request.method=="POST":
        password=request.POST.get('contraseña')
        password2=request.POST.get('contraseña2')
        if password == password2:
            usuario=User.objects.all()
            user=next(user for user in usuario if user.pk==id)
            user.first_name=request.POST.get('nombre')
            user.last_name=request.POST.get('apellido')
            user.username=request.POST.get('nombreu')
            user.mail=request.POST.get('correo')
            user.set_password(password)
            user.save()
            return redirect('ver_usuarios')   
    else:  
        usuario=User.objects.all()
        user=next(post for post in usuario if post.pk==id)
        return render(request, "editar_usuario.html", {"usuario":user})

def eliminar_usuario(request, id):
    user=User.objects.filter(id=id)
    user.delete()
    return redirect ('ver_usuarios')




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
