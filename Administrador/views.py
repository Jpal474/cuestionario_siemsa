from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


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

def editar_investigacion(request):
    return render (request, 'editar_investigacion.html')

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






