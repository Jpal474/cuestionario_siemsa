from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from Administrador.models import Pregunta
from Cuestionario.models import *
from weasyprint import HTML
from django.template.loader import render_to_string
from django.http import HttpResponse

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
    res = Pregunta.objects.all()
    sen = next(sen for sen in res if sen.id == id)
    return render(request, "editar_investigacion.html", {"pregunta": sen})

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

def resultado(request,id):
    res = Evaluacion.objects.all()
    evaluacion = next(evaluacion for evaluacion in res if evaluacion.id == id)
    nombre_proyecto=evaluacion.nombre_proyecto
    '''conclusiones=Conclusiones.objects.filter(nombre_proyecto=nombre_proyecto)
    iconos={
     
    }
    colores={}
    cont=0
    cont2=0
    icons=[None]*47
    icons[0]=evaluacion.pregunta1_1
    icons[1]=evaluacion.pregunta1_2
    icons[2]=evaluacion.pregunta2_1 
    icons[3]=evaluacion.pregunta2_2 
    icons[4]=evaluacion.pregunta2_3 
    icons[5]=evaluacion.pregunta2_4
    icons[6]=evaluacion.pregunta2_5
    icons[7]=evaluacion.pregunta2_6
    icons[8]=evaluacion.pregunta3_1
    icons[9]=evaluacion.pregunta3_2
    icons[10]=evaluacion.pregunta3_3
    icons[11]=evaluacion.pregunta3_4
    icons[12]=evaluacion.pregunta3_5 
    icons[13]=evaluacion.pregunta3_6
    icons[14]=evaluacion.pregunta4_1
    icons[15]=evaluacion.pregunta4_2
    icons[16]=evaluacion.pregunta4_3
    icons[17]=evaluacion.pregunta4_4 
    icons[18]=evaluacion.pregunta4_5
    icons[20]=evaluacion.pregunta4_6
    icons[19]=evaluacion.pregunta4_7
    icons[21]=evaluacion.pregunta4_8
    icons[22]=evaluacion.pregunta5_1  
    icons[23]=evaluacion.pregunta5_2 
    icons[24]=evaluacion.pregunta5_3
    icons[25]=evaluacion.pregunta5_4
    icons[26]=evaluacion.pregunta6_0
    icons[27]=evaluacion.pregunta6
    icons[28]=evaluacion.pregunta6_1 
    icons[29]=evaluacion.pregunta6_2
    icons[30]=evaluacion.pregunta6_3 
    icons[31]=evaluacion.pregunta6_4 
    icons[32]=evaluacion.pregunta6_5
    icons[33]=evaluacion.pregunta7
    icons[34]=evaluacion.pregunta7_1 
    icons[35]=evaluacion.pregunta7_2
    icons[36]=evaluacion.pregunta7_3
    icons[37]=evaluacion.pregunta7_4
    icons[38]=evaluacion.pregunta8_1
    icons[39]=evaluacion.pregunta8_2
    icons[40]=evaluacion.pregunta8_3
    icons[41]=evaluacion.pregunta8_4
    icons[42]=evaluacion.pregunta8_5
    icons[43]=evaluacion.pregunta9_1
    icons[44]=evaluacion.pregunta9_2
    icons[45]=evaluacion.pregunta9_3  
    icons[46]=evaluacion.pregunta9_4

    for icono in icons:
        if icono == 0:
            iconos[cont2]="close-outline"
            colores[cont2]="red"
            cont2+=1
        elif icono==12.5:
            iconos[cont2]="notifications-outline"
            colores[cont2]="red"
            cont2+=1 
        elif icono==25:
            iconos[cont2]="alert-outline"
            colores[cont2]="red"
            cont2+=1
        elif icono==50:
            iconos[cont2]="warning-outline"
            colores[cont2]="yellow"
            cont2+=1 
        else:
            iconos[cont2]="checkmark-outline"
            colores[cont2]="green"
            cont2+=1 
    cont2=0'''

    return render(request, "resultado.html", {"res": post})

def exportar_pdf(request,id):
    res = Evaluacion.objects.all()
    context = next(context for context in res if context.id == id)
    html = render_to_string("resultado_pdf.html", {"res": context})
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; report.pdf"
    HTML(string=html).write_pdf(response)
    return response