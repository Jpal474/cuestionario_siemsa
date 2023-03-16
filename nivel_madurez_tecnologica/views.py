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

def guardar_investigacion(request):
    investigacion=Respuestas_Investigacion()
    evalu=0
    evalu1=0
    investigacion.respuesta1_1=request.POST.get('investigacion')
    investigacion.evidencia1_1=request.POST.get('evidencia_investigacion')
    investigacion.respuesta1_2=request.POST.get('principios')
    investigacion.evidencia1_2=request.POST.get('evidencia_principios')
    investigacion.respuesta2_1=request.POST.get('analisis')
    investigacion.evidencia2_1=request.POST.get('evidencia_analisis')
    investigacion.save()
    valor1=request.POST.get('investigacion')
    valor2=request.POST.get('evidencia_investigacion')
    valor3=request.POST.get('principios')
    valor4=request.POST.get('evidencia_principios')
    valor5=request.POST.get('analisis')
    valor6=request.POST.get('evidencia_analisis')
    if(valor1=="Sí"):
        evalu=25.0
    if(valor2=="Sí"):
        evalu=evalu+25.0
    if(valor3=="Sí"):
        evalu=evalu+25.0
    if(valor4=="Sí"):
        evalu=evalu+25.0
    if(valor5=="Sí"):
        evalu1=50.0
    if(valor6=="Sí"):
        evalu1=evalu1+50.0
    
    prom=(evalu+evalu1)/2

    evaluacion=Evaluacion
    evaluacion.pregunta1_1=evalu
    evaluacion.pregunta1_2=evalu1
    evaluacion.promedio_trl1=prom
    

 

    return redirect ('desarrollo')

def desarrollo(request):
    return render(request, 'desarrollo.html')

def guardar_desarrollo(request): 
    desarrollo=Respuestas_Desarrollo()
    desarrollo.respuesta4_2=request.POST.get('pruebas')
    desarrollo.evidencia4_2=request.POST.get('evidencia_pruebas')
    desarrollo.respuesta4_5=request.POST.get('invencion')
    desarrollo.evidencia4_5=request.POST.get('evidencia_inv')
    desarrollo.respuesta4_6=request.POST.get('riesgos')
    desarrollo.evidencia4_6=request.POST.get('evidencia_riesgos')
    desarrollo.respuesta5_1=request.POST.get('prototipo')
    desarrollo.evidencia5_1=request.POST.get('evidencia_prototipo')
    desarrollo.respuesta6=request.POST.get('prototipo_sistema')
    desarrollo.evidencia6=request.POST.get('evidencia_producto_sistema')
    desarrollo.respuesta7_4=request.POST.get('producto')
    desarrollo.evidencia7_4=request.POST.get('evidencia_producto')
    desarrollo.respuesta8_2=request.POST.get('producto_comercializable')
    desarrollo.evidencia8_2=request.POST.get('evidencia_producto_comercializable')
    desarrollo.respuesta9_1=request.POST.get('produccion')
    desarrollo.evidencia9_1=request.POST.get('evidencia_produccion')
    desarrollo.respuesta9_3=request.POST.get('cambios')
    desarrollo.evidencia9_3=request.POST.get('evidencia_cambios')


    
     
    desarrollo.save()
    return redirect ('desarrollo')

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
