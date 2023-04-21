from asyncio.windows_events import proactor_events
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
    global fecha
    global nombre_proyecto
    registro=Registro()
    registro.nombre=request.POST.get('nombre')
    nombre_proyecto=registro.nombre_proyecto=request.POST.get('nombre_proyecto')
    registro.correo_electronico=request.POST.get('correo')
    registro.institucion=request.POST.get('institucion')
    registro.categoria=request.POST.get('categoria')
    fecha=registro.fecha=datetime.now()
    registro.save()
    return redirect ('investigacion')

def investigación(request):
    return render(request, 'investigacion.html')

def guardar_investigacion(request):
    nombre=Registro.objects.filter(nombre_proyecto=nombre_proyecto, fecha=fecha).values('nombre')
    evaluacion=Evaluacion()
    investigacion=Respuestas_Investigacion()
    respuestas=[]
    evidencias=[]
    resultados=[0]*3
    investigacion.nombre_proyecto=nombre_proyecto
    investigacion.categoria_pregunta='investigacion'
    investigacion.respuesta1_1=request.POST.get('investigacion')
    investigacion.evidencia1_1=request.POST.get('evidencia_investigacion')
    investigacion.respuesta1_2=request.POST.get('principios')
    investigacion.evidencia1_2=request.POST.get('evidencia_principios')
    investigacion.respuesta2_1=request.POST.get('analisis')
    investigacion.evidencia2_1=request.POST.get('evidencia_analisis')
    investigacion.save()
    respuestas=[investigacion.respuesta1_1, investigacion.respuesta1_2, investigacion.respuesta2_1]
    evidencias=[investigacion.evidencia1_1, investigacion.evidencia1_2, investigacion.evidencia2_1]
    promedio_area=0
    cont=0
    
    for respuesta in respuestas:
        if respuesta=='Sí':
            resultados[cont]=100
        elif respuesta=='No sé':
            resultados[cont]=50
        else:
            resultados[cont]=0
        cont+=1
 
    cont=0
    for evidencia in evidencias:
        if evidencia=='Sí':
            resultados[cont]*=1
        elif evidencia=='No sé':
            resultados[cont]*=0.5
        else:
            resultados[cont]*=0
        cont+=1    
    cont=0
    for resultado in resultados:
        promedio_area+=resultado

    promedio_area/=len(resultados)
  
    evaluacion.nombre=nombre
    evaluacion.nombre_proyecto=nombre_proyecto
    evaluacion.pregunta1_1=resultados[0]
    evaluacion.pregunta1_2=resultados[1]
    evaluacion.pregunta2_1=resultados[2]
    evaluacion.promedio_investigacion=promedio_area
    #evaluacion.promedio_trl1=prom
    investigacion.save()
    evaluacion.save()

 

    return redirect ('desarrollo')

def desarrollo(request):
    return render(request, 'desarrollo.html')

def guardar_desarrollo(request): 
    desarrollo=Respuestas_Desarrollo()
    desarrollo.respuesta1_1=request.POST.get('desarrollo')
    desarrollo.evidencia1_1=request.POST.get('evidencia_desarrollo')
    desarrollo.respuesta1_2=request.POST.get('principios')
    desarrollo.evidencia1_2=request.POST.get('evidencia_principios')
    desarrollo.respuesta2_1=request.POST.get('analisis')
    desarrollo.evidencia2_1=request.POST.get('evidencia_analisis')
    desarrollo.nombre_proyecto=nombre_proyecto
    desarrollo.respuesta4_2=request.POST.get('pruebas')
    desarrollo.evidencia4_2=request.POST.get('evidencia_pruebas')
    desarrollo.respuesta4_5=request.POST.get('invencion')
    desarrollo.evidencia4_5=request.POST.get('evidencia_inv')
    desarrollo.respuesta4_6=request.POST.get('riesgos')
    desarrollo.evidencia4_6=request.POST.get('evidencia_riesgos')
    desarrollo.respuesta5_1=request.POST.get('prototipo')
    desarrollo.evidencia5_1=request.POST.get('evidencia_prototipo')
    desarrollo.respuesta6=request.POST.get('prototipo_sistema')
    desarrollo.evidencia6=request.POST.get('evidencia_prototipo_sistema')
    desarrollo.respuesta7_4=request.POST.get('producto')
    desarrollo.evidencia7_4=request.POST.get('evidencia_producto')
    desarrollo.respuesta8_2=request.POST.get('producto_comercializable')
    desarrollo.evidencia8_2=request.POST.get('evidencia_producto_comercializable')
    desarrollo.respuesta9_1=request.POST.get('produccion')
    desarrollo.evidencia9_1=request.POST.get('evidencia_produccion')
    desarrollo.respuesta9_3=request.POST.get('cambios')
    desarrollo.evidencia9_3=request.POST.get('evidencia_cambios')
    respuestas=[desarrollo.respuesta4_2,desarrollo.respuesta4_5, desarrollo.respuesta4_6, desarrollo.respuesta5_1, desarrollo.respuesta6, desarrollo.respuesta7_4, desarrollo.respuesta8_2, desarrollo.respuesta9_1, desarrollo.respuesta9_3]
    evidencias=[desarrollo.evidencia4_2,desarrollo.evidencia4_5, desarrollo.evidencia4_6, desarrollo.evidencia5_1, desarrollo.evidencia6, desarrollo.evidencia7_4, desarrollo.evidencia8_2, desarrollo.evidencia9_1, desarrollo.evidencia9_3]
    resultados=[0]*9
    promedio_area=0
    cont=0
    for respuesta in respuestas:
        if respuesta=='Sí':
            resultados[cont]=100
        elif respuesta=='No sé':
            resultados[cont]=50
        else:
            resultados[cont]=0
        cont+=1

    cont=0
    for evidencia in evidencias:
        if evidencia=='Sí':
            resultados[cont]*=1
        elif evidencia=='No sé':
            resultados[cont]*=0.5
        else:
            resultados[cont]*=0
        cont+=1  
    for resultado in resultados:
        promedio_area+=resultado

    promedio_area/=len(resultados) 
    desarrollo.save()
    global evaluacion
    evaluacion=Evaluacion.objects.filter(nombre_proyecto=nombre_proyecto).last()
    evaluacion.pregunta4_2=resultados[0]
    evaluacion.pregunta4_5=resultados[1]
    evaluacion.pregunta4_6=resultados[2]
    evaluacion.pregunta5_1=resultados[3]
    evaluacion.pregunta6=resultados[4]
    evaluacion.pregunta7_4=resultados[5]
    evaluacion.pregunta8_2=resultados[6]
    evaluacion.pregunta9_1=resultados[7]
    evaluacion.pregunta9_3=resultados[8]
    evaluacion.promedio_desarrollo=promedio_area
    evaluacion.save()

    return redirect ('integracion')

def integracion(request):
    return render(request, 'integracion.html')

def guardar_integracion(request):
    integracion=Respuestas_Integracion()
    integracion.nombre_proyecto=nombre_proyecto
    integracion.respuesta2_5=request.POST.get('investigacion')
    integracion.evidencia2_5=request.POST.get('evidencia_investigacion')
    integracion.respuesta3_1=request.POST.get('componentes')
    integracion.evidencia3_1=request.POST.get('evidencia_componentes')
    integracion.respuesta4_1=request.POST.get('integracion_componentes')
    integracion.evidencia4_1=request.POST.get('evidencia_integracion_componentes')
    integracion.respuesta6_2=request.POST.get('producto')
    integracion.evidencia6_2=request.POST.get('evidencia_producto')
    respuestas=[integracion.respuesta2_5, integracion.respuesta3_1, integracion.respuesta4_1, integracion.respuesta6_2]
    evidencias=[integracion.evidencia2_5, integracion.evidencia3_1, integracion.evidencia4_1, integracion.evidencia6_2]
    resultados=[0]*len(respuestas)
    cont=0
    promedio_area=0
    for respuesta in respuestas:
        if respuesta=='Sí':
            resultados[cont]=100
        elif respuesta=='No sé':
            resultados[cont]=50
        else:
            resultados[cont]=0
        cont+=1

    cont=0
    for evidencia in evidencias:
        if evidencia=='Sí':
            resultados[cont]*=1
        elif evidencia=='No sé':
            resultados[cont]*=0.5
        else:
            resultados[cont]*=0
        cont+=1
    for resultado in resultados:
        promedio_area+=resultado    
    
    promedio_area/=len(resultados) 
    integracion.save()
    evaluacion.pregunta2_5=resultados[0]
    evaluacion.pregunta3_1=resultados[1]
    evaluacion.pregunta4_1=resultados[2]
    evaluacion.pregunta6_2=resultados[3]
    evaluacion.promedio_integracion=promedio_area
    evaluacion.save()
    return redirect('normatividad')


def propiedad(request):
    return render(request, 'propiedad.html')

def guardar_propiedad(request):
    propiedad=Respuestas_Propiedad()
    propiedad.nombre_proyecto=nombre_proyecto
    propiedad.respuesta2_2=request.POST.get('busqueda')
    propiedad.evidencia2_2=request.POST.get('evidencia_busqueda')
    propiedad.respuesta3_3=request.POST.get('estudios')
    propiedad.evidencia3_3=request.POST.get('evidencia_estudios')
    propiedad.respuesta3_4=request.POST.get('')
    propiedad.evidencia3_4=request.POST.get('')
    propiedad.respuesta2_6=request.POST.get('')
    propiedad.evidencia2_6=request.POST.get('')
    propiedad.respuesta3_6=request.POST.get('')
    propiedad.evidencia3_6=request.POST.get('')
    propiedad.respuesta6=request.POST.get('')
    propiedad.evidencia6=request.POST.get('')
    propiedad.respuesta7=request.POST.get('')
    propiedad.evidencia7=request.POST.get('')
    if propiedad.respuesta3_3 == 2:
        propiedad.respuesta4_7=request.POST.get('Sí')
        propiedad.evidencia4_7=request.POST.get('evidencia_estudios')
    elif propiedad.respuesta3_3 >= 3:
        propiedad.respuesta4_7=request.POST.get('Sí')
        propiedad.evidencia4_7=request.POST.get('evidencia_estudios')
        propiedad.respuesta5_4=request.POST.get('Sí')
        propiedad.evidencia5_4=request.POST.get('evidencia_estudios')
    if propiedad.respuesta3_6 >= 2:
        propiedad.respuesta4_8=request.POST.get('Sí')
        propiedad.evidencia4_8=request.POST.get('evidencia_actualizacion')

    respuestas=[propiedad.respuesta2_5, propiedad.respuesta3_1, propiedad.respuesta4_1, propiedad.respuesta6_2]
    evidencias=[propiedad.evidencia2_5, propiedad.evidencia3_1, propiedad.evidencia4_1, propiedad.evidencia6_2]
    resultados=[0]*len(respuestas)
    cont=0
    promedio_area=0
    print('Longitud' + str(len(resultados)))
    for respuesta in respuestas:
        if respuesta=='Sí':
            resultados[cont]=100
        elif respuesta=='No sé':
            resultados[cont]=50
        else:
            resultados[cont]=0
        cont+=1

    cont=0
    for evidencia in evidencias:
        if evidencia=='Sí':
            resultados[cont]*=1
        elif evidencia=='No sé':
            resultados[cont]*=0.5
        else:
            resultados[cont]*=0
        cont+=1  
      
    for resultado in resultados:
        promedio_area+=resultado

    promedio_area/=len(resultados)  
    integracion.save()
    evaluacion.pregunta2_5=resultados[0]
    evaluacion.pregunta3_1=resultados[1]
    evaluacion.pregunta4_1=resultados[2]
    evaluacion.pregunta6_2=resultados[3]
    evaluacion.promedio_propiedad=promedio_area
    evaluacion.save()


def normatividad(request):
    return render(request, 'normatividad.html')

def guardar_normatividad(request):
    normatividad=Respuestas_Normatividad()
    normatividad.nombre_proyecto=nombre_proyecto
    normatividad.respuesta3_5=request.POST.get('estudio')
    normatividad.evidencia3_5=request.POST.get('evidencia_estudio')
    normatividad.respuesta5_3=request.POST.get('prototipo')
    normatividad.evidencia5_3=request.POST.get('evidencia_prototipo')
    normatividad.respuesta6_5=request.POST.get('proceso_registro')
    normatividad.evidencia6_5=request.POST.get('evidencia_proceso_registro')
    normatividad.respuesta8_4=request.POST.get('estandares_prototipo')
    normatividad.evidencia8_4=request.POST.get('evidencia_estandares_prototipo')

    respuestas=[normatividad.respuesta3_5, normatividad.respuesta5_3, normatividad.respuesta6_5, normatividad.respuesta8_4]
    evidencias=[normatividad.evidencia3_5, normatividad.evidencia5_3, normatividad.evidencia6_5, normatividad.evidencia8_4]
    resultados=[0]*len(respuestas)
    cont=0
    promedio_area=0
    for respuesta in respuestas:
        if respuesta=='Sí':
            resultados[cont]=100
        elif respuesta=='No sé':
            resultados[cont]=50
        else:
            resultados[cont]=0
        cont+=1

    cont=0
    for evidencia in evidencias:
        if evidencia=='Sí':
            resultados[cont]*=1
        elif evidencia=='No sé':
            resultados[cont]*=0.5
        else:
            resultados[cont]*=0
        cont+=1    
    for resultado in resultados:
        promedio_area+=resultado

    promedio_area/=len(resultados) 

    normatividad.save()
    evaluacion.pregunta3_5=resultados[0]
    evaluacion.pregunta5_3=resultados[1]
    evaluacion.pregunta6_5=resultados[2]
    evaluacion.pregunta8_4=resultados[3]
    evaluacion.promedio_normatividad=promedio_area
    evaluacion.save()
    return redirect('manufactura')

def manufactura(request):
    return render(request, 'manufactura.html')

def guardar_manufactura(request):
    manufactura=Respuestas_Manufactura()
    manufactura.nombre_proyecto=nombre_proyecto
    manufactura.respuesta2_3=request.POST.get('manufacturabilidad')
    manufactura.evidencia2_3=request.POST.get('evidencia_manufacturabilidad')
    manufactura.respuesta4_3=request.POST.get('exploracion')
    manufactura.evidencia4_3=request.POST.get('evidencia_exploracion')
    manufactura.respuesta5_2=request.POST.get('aspectos')
    manufactura.evidencia5_2=request.POST.get('evidencia_aspectos')
    manufactura.respuesta6_1=request.POST.get('piloto')
    manufactura.evidencia6_1=request.POST.get('evidencia_piloto')
    manufactura.respuesta7_1=request.POST.get('producto')
    manufactura.evidencia7_1=request.POST.get('evidencia_producto')
    manufactura.respuesta8_1=request.POST.get('version')
    manufactura.evidencia8_1=request.POST.get('evidencia_version')
    manufactura.respuesta9_4=request.POST.get('procesos')
    manufactura.evidencia9_4=request.POST.get('evidencia_procesos') 
    
    respuestas=[manufactura.respuesta2_3, manufactura.respuesta4_3, manufactura.respuesta5_2, manufactura.respuesta6_1,manufactura.respuesta7_1, manufactura.respuesta8_1, manufactura.respuesta9_4]
    evidencias=[manufactura.evidencia2_3, manufactura.evidencia4_3, manufactura.evidencia5_2, manufactura.evidencia6_1, manufactura.evidencia7_1, manufactura.evidencia8_1, manufactura.evidencia9_4]
    resultados=[0]*len(respuestas)
    cont=0
    promedio_area=0
    print('Longitud' + str(len(resultados)))
    for respuesta in respuestas:
        if respuesta=='Sí':
            resultados[cont]=100
        elif respuesta=='No sé':
            resultados[cont]=50
        else:
            resultados[cont]=0
        cont+=1

    cont=0
    for evidencia in evidencias:
        if evidencia=='Sí':
            resultados[cont]*=1
        elif evidencia=='No sé':
            resultados[cont]*=0.5
        else:
            resultados[cont]*=0
        cont+=1 

    for resultado in resultados:
        promedio_area+=resultado 

    promedio_area/=len(resultados)   
    manufactura.save()

    evaluacion.pregunta2_3=resultados[0]
    evaluacion.pregunta4_3=resultados[1]
    evaluacion.pregunta5_2=resultados[2]
    evaluacion.pregunta6_1=resultados[3]
    evaluacion.pregunta7_1=resultados[4]
    evaluacion.pregunta8_1=resultados[5]
    evaluacion.pregunta9_4=resultados[6]
    evaluacion.promedio_manufactura=promedio_area
    evaluacion.save()
    return redirect('usuarios')
    
def usuarios_producto(request):
    return render(request, 'usuarios_producto.html')

def guardar_usuarios_producto(request):
    usuarios_producto=Respuestas_Usuarios()
    usuarios_producto.nombre_proyecto=nombre_proyecto
    usuarios_producto.respuesta2_4=request.POST.get('usuarios')
    usuarios_producto.evidencia2_4=request.POST.get('evidencia_usuarios')
    usuarios_producto.respuesta3_2=request.POST.get('proceso_validacion')
    usuarios_producto.evidencia3_2=request.POST.get('evidencia_proceso_validacion')
    usuarios_producto.respuesta4_4=request.POST.get('validacion_mercado')
    usuarios_producto.evidencia4_4=request.POST.get('evidencia_validacion_mercado')
    usuarios_producto.respuesta6_3=request.POST.get('usuarios_potenciales')
    usuarios_producto.evidencia6_3=request.POST.get('evidencia_usuarios_potenciales')
    usuarios_producto.respuesta7_2=request.POST.get('version_final')
    usuarios_producto.evidencia7_2=request.POST.get('evidencia_version_final')
    usuarios_producto.respuesta8_5=request.POST.get('documentos')
    usuarios_producto.evidencia8_5=request.POST.get('evidencia_documentos')
    
    respuestas=[usuarios_producto.respuesta2_4, usuarios_producto.respuesta3_2, usuarios_producto.respuesta4_4, usuarios_producto.respuesta6_3,usuarios_producto.respuesta7_2, usuarios_producto.respuesta8_5]
    evidencias=[usuarios_producto.evidencia2_4, usuarios_producto.evidencia3_2, usuarios_producto.evidencia4_4, usuarios_producto.evidencia6_3, usuarios_producto.evidencia7_2, usuarios_producto.evidencia8_5]
    resultados=[0]*len(respuestas)
    cont=0
    promedio_area=0
    print('Longitud' + str(len(resultados)))
    for respuesta in respuestas:
        if respuesta=='Sí':
            resultados[cont]=100
        elif respuesta=='No sé':
            resultados[cont]=50
        else:
            resultados[cont]=0
        cont+=1

    cont=0
    for evidencia in evidencias:
        if evidencia=='Sí':
            resultados[cont]*=1
        elif evidencia=='No sé':
            resultados[cont]*=0.5
        else:
            resultados[cont]*=0
        cont+=1    
    
    for resultado in resultados:
        promedio_area+=resultado 
    
    promedio_area/=len(resultados) 
    usuarios_producto.save()
    evaluacion.pregunta2_4=resultados[0]
    evaluacion.pregunta3_2=resultados[1]
    evaluacion.pregunta4_4=resultados[2]
    evaluacion.pregunta6_3=resultados[3]
    evaluacion.pregunta7_2=resultados[4]
    evaluacion.pregunta8_5=resultados[5]
    evaluacion.promedio_usuarios=promedio_area
    evaluacion.save()
    return redirect('aspectos')

def aspectos(request):
    return render(request, 'aspectos.html')

def guardar_aspectos(request):
    aspectos=Respuestas_Aspectos()
    aspectos.nombre_proyecto=nombre_proyecto
    aspectos.respuesta6_4=request.POST.get('organizacion')
    aspectos.evidencia6_4=request.POST.get('evidencia_organizacion')
    aspectos.respuesta7_3=request.POST.get('estructura')
    aspectos.evidencia7_3=request.POST.get('evidencia_estructura')
    aspectos.respuesta8_3=request.POST.get('operativa')
    aspectos.evidencia8_3=request.POST.get('evidencia_operativa')
    aspectos.respuesta9_2=request.POST.get('producto')
    aspectos.evidencia9_2=request.POST.get('evidencia_producto')
    
    
    respuestas=[aspectos.respuesta6_4, aspectos.respuesta7_3, aspectos.respuesta8_3, aspectos.respuesta9_2]
    evidencias=[aspectos.evidencia6_4, aspectos.evidencia7_3, aspectos.evidencia8_3, aspectos.evidencia9_2]
    resultados=[0]*len(respuestas)
    cont=0
    promedio_area=0
    print('Longitud' + str(len(resultados)))
    for respuesta in respuestas:
        if respuesta=='Sí':
            resultados[cont]=100
        elif respuesta=='No sé':
            resultados[cont]=50
        else:
            resultados[cont]=0
        cont+=1

    cont=0
    for evidencia in evidencias:
        if evidencia=='Sí':
            resultados[cont]*=1
        elif evidencia=='No sé':
            resultados[cont]*=0.5
        else:
            resultados[cont]*=0
        cont+=1   

    for resultado in resultados:
        promedio_area+=resultado 

    promedio_area/=len(resultados) 
    aspectos.save()
    evaluacion.pregunta6_4=resultados[0]
    evaluacion.pregunta7_3=resultados[1]
    evaluacion.pregunta8_3=resultados[2]
    evaluacion.pregunta9_2=resultados[3]
    evaluacion.promedio_aspectos=promedio_area
    evaluacion.save()
    return redirect('resultados')

def resultados(request):
    estatus=Estatus()
    conclusiones=Conclusiones()
    evaluacion.promedio_trl1=(evaluacion.pregunta1_1 + evaluacion.pregunta1_2)/2
    evaluacion.promedio_trl2=(evaluacion.pregunta2_1  + evaluacion.pregunta2_2 + evaluacion.pregunta2_3 + evaluacion.pregunta2_4 + evaluacion.pregunta2_5 + evaluacion.pregunta2_6)/6
    evaluacion.promedio_trl3=(evaluacion.pregunta3_1  + evaluacion.pregunta3_2 + evaluacion.pregunta3_3 + evaluacion.pregunta3_4 + evaluacion.pregunta3_5 + evaluacion.pregunta3_6)/6
    evaluacion.promedio_trl4=(evaluacion.pregunta4_1  + evaluacion.pregunta4_2 + evaluacion.pregunta4_3 + evaluacion.pregunta4_4 + evaluacion.pregunta4_5  + evaluacion.pregunta4_6 + evaluacion.pregunta4_7+ evaluacion.pregunta4_8)/8
    evaluacion.promedio_trl5=(evaluacion.pregunta5_1  + evaluacion.pregunta5_2 + evaluacion.pregunta5_3 + evaluacion.pregunta5_4)/4
    evaluacion.promedio_trl6=(evaluacion.pregunta6_1  + evaluacion.pregunta6_2 + evaluacion.pregunta6_3 + evaluacion.pregunta6_4 + evaluacion.pregunta6_5)/5
    evaluacion.promedio_trl7=(evaluacion.pregunta7_1  + evaluacion.pregunta7_2 + evaluacion.pregunta7_3 + evaluacion.pregunta7_4)/4
    evaluacion.promedio_trl8=(evaluacion.pregunta8_1  + evaluacion.pregunta8_2 + evaluacion.pregunta8_3 + evaluacion.pregunta8_4 + evaluacion.pregunta8_5)/5
    evaluacion.promedio_trl9=(evaluacion.pregunta9_1  + evaluacion.pregunta9_2 + evaluacion.pregunta9_3 + evaluacion.pregunta9_4)/4
    
    promedios=evaluacion.promedio_trl1+evaluacion.promedio_trl2+evaluacion.promedio_trl3+evaluacion.promedio_trl4+evaluacion.promedio_trl5+evaluacion.promedio_trl6+evaluacion.promedio_trl7+evaluacion.promedio_trl8+evaluacion.promedio_trl9
    promedios2=[evaluacion.promedio_investigacion,evaluacion.promedio_desarrollo,evaluacion.promedio_integracion,evaluacion.promedio_propiedad,evaluacion.promedio_normatividad,evaluacion.promedio_manufactura,evaluacion.promedio_usuarios,evaluacion.promedio_aspectos]
    promedios/=9
    global_trl=(promedios/9)*0.09
    evaluacion.promedio_trl_global=global_trl
    evaluacion.save()
    if global_trl >= 9:
        estatus.estatus="Tu invención es un Producto terminado.Pruebas con éxito en entorno real. Despliegue.Tecnología disponible en el mercado. Aplicación comercial."
    elif global_trl>=8:
        estatus.estatus="Tu invención se encuentra en Desarrollo de Producto.Sistema completo y evaluado Manufacturabilidad probada y validada para ambiente real.Sistema completo y certificado. Producto o servicio comercializable. Resultados de las pruebas del sistema en su configuración final."
    elif global_trl>=7:
        estatus.estatus="Tu invención se encuentra en  Desarrollo de Producto.Demostración de prototipo a nivel sistema en un ambiente operativo real (sistema real).Producción a baja escala para demostración en ambiente operativo real."
    elif global_trl>=6:
        estatus.estatus="Tu invención se encuentra en  Demostración tecnológica.Tecnología demostrada en un ambiente relevante.Pre-producción de un producto, incluyendo pruebas en un ambiente real."
    elif global_trl>=5:
        estatus.estatus="Tu invención se encuentra en Desarrollo Tecnológico.Tecnología validada en laboratorio pero en condiciones de un entorno relevante (condiciones que simulan condiciones existentes en un entorno real).La integración de los componentes empieza a ser de alta confiabilidad."
    elif global_trl>=4:
        estatus.estatus="Tu invención se encuentra en Desarrollo Tecnológico.Validación tecnológica a nivel laboratorio.Validación de un prototipo inicial con componentes integrados en laboratorio con baja confiabilidad de comportamiento."
    elif global_trl>=3:
        estatus.estatus="Tu invención se encuentra en Investigación de Laboratorio.Prueba experimental de concepto. Primera evaluación de la factibilidad del concepto y su tecnología."
    elif global_trl>=2:
        estatus.estatus="Tu invención se encuentra en Investigación de Laboratorio.Concepto tecnológico y/o aplicación tecnológica formulada. Investigación aplicada."
    elif global_trl>=1:
        estatus.estatus="Tu invención se cuentra en Investigación básica. Principios básicos observados y reportados.Tu invención se encuentra en un nivel muy temprano, es necesario comenzar con la investigación básica que ayude a sustentar y formular la idea."

    conclusion=[None]*8
    cont=0
    for promedio in promedios2:
        if promedio==1:
            conclusion[cont]='El tópico INVESTIGACIÓN se encuentra cubierto en su TOTALIDAD. Se han realizado satisfactoriamente todas las actividades correspondientes.'
        elif promedio==0:
            conclusion[cont]="No ha iniciado con actividades relacionadas al tópico INVESTIGACIÓN, es necesario identificar una problemática a resolver, investigar principios de investigación básica que pudieran transformarse en principios básicos para aplicarse a nuevas tecnologías."
        elif promedio<=25:
            conclusion[cont]="El tópico INVESTIGACIÓN se encuentra en fase CRÍTICA, este tópico aún no se ha completado, debido a que faltan considerablemente actividades para concluirlo. Revisa cuidadosamente las recomendaciones para identificar las actividades faltantes"
        elif promedio<=50:
            conclusion[cont]="El tópico INVESTIGACIÓN se encuentra en fase INICIAL, este tópico aún no se encuentra completo, debido a que faltan considerablemente actividades para concluirlo. Revisa cuidadosamente las recomendaciones para identificar las actividades faltantes"
        elif promedio<=75:
            conclusion[cont]="El tópico INVESTIGACIÓN se encuentra en fase INTERMEDIA, este tópico aún no se encuentra completo, debido a que faltan diversas actividades para concluirlo. Revisa cuidadosamente las recomendaciones para identificar las actividades faltantes"
        elif promedio <=100:
            conclusion[cont]="El tópico INVESTIGACIÓN se encuentra en fase AVANZADA, este tópico aún no se encuentra completo, sin embargo, falta muy poco para concluirlo. Revisa cuidadosamente las recomendaciones para identificar las actividades faltantes"
        cont+=1
    conclusiones.conclusion_investigacion=conclusion[0]
    conclusiones.conclusion_desarrollo=conclusion[1]
    conclusiones.conclusion_integracion=conclusion[2]
    conclusiones.conclusion_propiedad=conclusion[3]
    conclusiones.conclusion_normatividad=conclusion[4]
    conclusiones.conclusion_manufactura=conclusion[5]
    conclusiones.conclusion_usuarios=conclusion[6]
    conclusiones.conclusion_aspectos=conclusion[7]

    conclusiones.nombre_proyecto=estatus.nombre_proyecto=nombre_proyecto

    if evaluacion.pregunta1_1==100:
        reco="Cuenta con un GRUPO DE INVESTIGACIÓN Y DESARROLLO adecuado y acorde a las características técnicas, administrativas y operativas que demanda el proyecto, además ha documentado satisfactoriamente toda la información necesaria y anexos que validan el perfil y experiencia de cada miembro del GRUPO DE INVESTIGACIÓN Y DESARROLLO."
    elif evaluacion.pregunta1_1==0:
        reco="No ha iniciado con la INVESTIGACIÓN BÁSICA DE SU IDEA, es necesario identificar una problemática a resolver, investigar principios de investigación básica que pudieran transformarse en principios básicos para aplicarse a nuevas tecnologías."
    elif evaluacion.pregunta1_1<=13:
        reco="No está seguro de haber iniciado con la INVESTIGACIÓN BÁSICA DE SU IDEA, sin embargo, es muy probable que no tenga plenamente identificada la problemática a resolver, por lo que también es probable que no haya investigado principios de investigación básica que pudieran transformarse en principios básicos para aplicarse a nuevas tecnologías, así como la correcta documentación del proceso. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta1_1<=25:
        reco="Ya ha iniciado con la INVESTIGACIÓN BÁSICA DE SU IDEA, sin embargo, es necesario documentar el proceso realizado; tanto la identificación de la problemática a resolver, como la investigación de los principios de investigación básica que pudieran transformarse en principios básicos para aplicarse a nuevas tecnologías. Asegure realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta1_1<=50:
        reco="Ya ha iniciado con la INVESTIGACIÓN BÁSICA DE SU IDEA, ya tiene identificada la problemática a resolver, ha investigado los principios de investigación básica que pudieran trasnformarse en principios básicos para aplicarse a nuevas tecnologías, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."




    if evaluacion.pregunta1_2==100:
        reco1="La IDENTIFICACIÓN DE PRINCIPIOS DE INVESTIGACIÓN BÁSICA de su idea se ha completado y documentado satisfactoriamente."
    elif evaluacion.pregunta1_2==0:
        reco1="No ha iniciado con la IDENTIFICACIÓN DE PRINCIPIOS DE INVESTIGACIÓN BÁSICA, es necesario identificar estos principios que pudieran transformarse en principios básicos para aplicarse a nuevas tecnologías."
    elif evaluacion.pregunta1_2<=13:
        reco1="No está seguro de haber iniciado con la IDENTIFICACIÓN DE PRINCIPIOS DE INVESTIGACIÓN BÁSICA, sin embargo, es muy probable que que no tenga plenamente identificados estos principios que pudieran transformarse en principios básicos para aplicarse a nuevas tecnologías, así como la correcta documentación del proceso. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta1_2<=25:
        reco1="Ya ha iniciado con la IDENTIFICACIÓN DE PRINCIPIOS DE INVESTIGACIÓN BÁSICA, sin embargo, es necesario documentar el proceso realizado; tanto los principios de investigación básica identificados, así como la identificación de los principios básicos para aplicarse a nuevas tecnologías. Asegure realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta1_1<=50:
        reco1="Ya ha iniciado con la IDENTIFICACIÓN DE PRINCIPIOS DE INVESTIGACIÓN BÁSICA, ya ha identificado los principios de investigación básica que pudieran trasnformarse en principios básicos para aplicarse a nuevas tecnologías, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."




    if evaluacion.pregunta2_1==100:
        reco2="El ESTUDIO DEL ESTADO DE LA TÉCNICA que respalda la aplicación de la idea en algún área tecnológica se ha completado y documentado satisfactoriamente."
    elif evaluacion.pregunta2_1==0:
        reco2="No ha iniciado con el ESTUDIO DEL ESTADO DE LA TÉCNICA que respalda la aplicación de la idea en algún área tecnológica, es necesario realizar estudios del estado de la técnica, proponer alternativas de solución y documentar el proceso"
    elif evaluacion.pregunta1_1<=13:
        reco2="No está seguro de haber iniciado con el ESTUDIO DEL ESTADO DE LA TÉCNICA, sin embargo, es muy probable que no tenga plenamente identificada la aplicación de la idea en un área tecnológica con el objetivo de resolver la problemática identificada, asegurese de haber realizado estudios del estado de la técnica y de de haber propuesto alternativas de solución, así como la correcta documentación del proceso. Revise cuidadosamente la información y documentación disponible."
    elif evaluacion.pregunta1_1<=25:
        reco2="Ya ha iniciado con el ESTUDIO DEL ESTADO DE LA TÉCNICA que respalda la aplicación de la idea en algún área tecnológica, sin embargo, es necesario documentar el proceso realizado; tanto los estudios del estado de la técnica, así como las alternativas de solución propuestas a la problemática identificada. Asegure realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta1_1<=50:
        reco2="Ya ha iniciado con el ESTUDIO DEL ESTADO DE LA TÉCNICA que respalda la aplicación de la idea en algún área tecnológica, ya tiene identificada la problemática a resolver, ha realizado estudios del estado de la técnica y ha propuesto alternativas de solución, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."




    if evaluacion.pregunta4_2==100:
        reco3="Las PRUEBAS A NIVEL LABORATORIO para validar la efectividad de su invención a nivel laboratorio y en condiciones controladas se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta4_2==0:
        reco3="No ha iniciado con las PRUEBAS A NIVEL LABORATORIO para validar la efectividad de su invención a nivel laboratorio y en condiciones controladas, es necesario iniciar con pruebas de baja confiabilidad para validar la efectividad de su invención."
    elif evaluacion.pregunta4_2<=13:
        reco3="No está seguro de haber iniciado con las PRUEBAS A NIVEL LABORATORIO para validar la efectividad de su invención a nivel laboratorio y en condiciones controladas, sin embargo, es muy probable que no haya realizado pruebas de baja confiabilidad para validar la efectividad de su invenición. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta4_2<=25:
        reco3="Ya ha iniciado con las PRUEBAS A NIVEL LABORATORIO para validar la efectividad de su invención a nivel laboratorio y en condiciones controladas, sin embargo, es necesario documentar el proceso realizado; deben ser pruebas de baja confiabilidad. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta4_2<=50:
        reco3="Ya ha iniciado con las PRUEBAS A NIVEL LABORATORIO para validar la efectividad de su invención a nivel laboratorio y en condiciones controladas, ha realizado pruebas de baja confiabilidad, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."




    if evaluacion.pregunta4_5==100:
        reco4="Las PRUEBAS A NIVEL LABORATORIO para validar la funcionalidad de su invención a nivel laboratorio y en condiciones controladas se ha completado y documentado satisfactoriamente."
    elif evaluacion.pregunta4_5==0:
        reco4="No ha realizado PRUEBAS A NIVEL LABORATORIO para validar la funcionalidad de su invención a nivel laboratorio y en condiciones controladas, es necesario realizar pruebas de baja confiabilidad para validar la funcionalidad de su invención."
    elif evaluacion.pregunta4_5<=13:
        reco4="No está seguro de haber realizado PRUEBAS A NIVEL LABORATORIO que validen la funcionalidad de su invención a nivel laboratorio y en condiciones controladas, sin embargo, es muy probable que no haya realizado pruebas de baja confiabilidad para validar la funcionalidad de su invenicin. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta4_5<=25:
        reco4="Ya ha iniciado con las PRUEBAS A NIVEL LABORATORIO para validar la funcionalidad de su invención a nivel laboratorio y en condiciones controladas, sin embargo, es necesario documentar el proceso realizado; deben ser pruebas de baja confiabilidad. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta4_5<=50:
        reco4="Ya ha iniciado con las PRUEBAS A NIVEL LABORATORIO para validar la funcionalidad de su invención a nivel laboratorio y en condiciones controladas, ha realizado pruebas de baja confiabilidad, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."
    
    


    if evaluacion.pregunta5_1==100:
        reco5="Las PRUEBAS EN ENTORNO RELEVANTE para validar la efectividad de su invención a nivel laboratorio pero en condiciones que simulan un entorno real se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta5_1==0:
        reco5="No ha iniciado con las PRUEBAS EN ENTORNO RELEVANTE para validar la efectividad de su invensión a nivel laboratorio pero en condiciones que simulan un entorno real, es necesario iniciar con pruebas de baja confiabilidad para validar la efectividad de su invensión."
    elif evaluacion.pregunta5_1<=13:
        reco5="No está seguro de haber iniciado con las PRUEBAS EN ENTORNO RELEVANTE para validar la efectividad de su invensión a nivel laboratorio pero en condiciones que simulan un entorno real, sin embargo, es muy probable que no haya realizado pruebas donde la integración de los componentes comience a ser de mayor confiabilidad para validar la efectividad de su invenisón. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta5_1<=25:
        reco5="Ya ha iniciado con las PRUEBAS EN ENTORNO RELEVANTE para validar la efectividad de su invensión a nivel laboratorio pero en condiciones que simulan un entorno real, sin embargo, es necesario documentar el proceso realizado; deben ser pruebas donde la integración de los componentes comience a ser de mayor confiabilidad. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta5_1<=50:
        reco5="Ya ha iniciado con las PRUEBAS EN ENTORNO RELEVANTE para validar la efectividad de su invensión a nivel laboratorio pero en condiciones que simulan un entorno real, ha realizado pruebas donde la integración de los componentes ha comenzado a ser de mayor confiabilidad, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."
    



    
    if evaluacion.pregunta6_0==100:
        reco6="Las PRUEBAS DE SISTEMA EN ENTORNO RELEVANTE para validar la efectividad de su invensión en condiciones que simulan un entorno real y en condiciones reales se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta6_0==0:
        reco6="No ha iniciado con las PRUEBAS DE SISTEMA EN ENTORNO RELEVANTE para validar la efectividad de su invensión en condiciones que simulan un entorno real y en condiciones reales, es necesaria la integración completa de componentes y realizar pruebas de alta confiabilidad para validar la efectividad de su invensión."
    elif evaluacion.pregunta6_0<=13:
        reco6="No está seguro de haber iniciado con las PRUEBAS DE SISTEMA EN ENTORNO RELEVANTE para validar la efectividad de su invensión en condiciones que simulan un entorno real y en condiciones reales, sin embargo, es muy probable que no haya realizado pruebas donde la integración de los componentes esté completa y sean de alta confiabilidad para validar la efectividad de su invenisón. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta6_0<=25:
        reco6="Ya ha iniciado con las PRUEBAS DE SISTEMA EN ENTORNO RELEVANTE para validar la efectividad de su invensión en condiciones que simulan un entorno real y en condiciones reales, sin embargo, es necesario documentar el proceso realizado; deben ser pruebas donde la integración de los componentes esté completa y de alta confiabilidad. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta6_0<=50:
        reco6="Ya ha iniciado con las PRUEBAS DE SISTEMA EN ENTORNO RELEVANTE para validar la efectividad de su invensión en condiciones que simulan un entorno real y en condiciones reales, ha realizado pruebas donde la integración de los componentes es completa y de alta confiabilidad, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."




    
    if evaluacion.pregunta7_4==100:
        reco7="Las PRUEBAS DE PRODUCTO TERMINADO para validación de primeros clientes para demostración de efectividad del prototipo a nivel sistema en un ambiente operativo real, así como producción a baja escala se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta7_4==0:
        reco7="No ha iniciado con las PRUEBAS DE PRODUCTO TERMINADO para validación de primeros clientes para demostración de efectividad del prototipo a nivel sistema en un ambiente operativo real, es necesaria la integración completa de componentes y realizar pruebas de alto grado de confiabilidad, así como producción en baja escala."
    elif evaluacion.pregunta7_4<=13:
        reco7="No está seguro de haber iniciado con las PRUEBAS DE PRODUCTO TERMINADO para validación de primeros clientes para demostración de efectividad del prototipo a nivel sistema en un ambiente operativo real, sin embargo, es muy probable que no haya realizado pruebas donde la integración de los componentes esté completa y sean de alto grado de confiabilidad, así como tampoco una producción a baja escala. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta7_4<=25:
        reco7="Ya ha iniciado con las PRUEBAS DE PRODUCTO TERMINADO para validación de primeros clientes para demostración de efectividad del prototipo a nivel sistema en un ambiente operativo real, así como producción a baja escala, sin embargo, es necesario documentar el proceso realizado; deben ser pruebas donde la integración de los componentes esté completa y de alto grado de confiabilidad. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta7_4<=50:
        reco7="Ya ha iniciado con las PRUEBAS DE PRODUCTO TERMINADO para validación de primeros clientes para demostración de efectividad del prototipo a nivel sistema en un ambiente operativo real, ha realizado pruebas donde la integración de los componentes es completa y de alto grado de confiabilidad, así como una producción a baja escala, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."




  
    if evaluacion.pregunta8_2==100:
        reco8="Las PRUEBAS DE PRODUCTO COMERCIALIZABLE en su configuración final para demostración, evaluación y certificación del sistema completo en un ambiente operativo real, así como manufacturabilidad probada se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta8_2==0:
        reco8="No ha iniciado con las PRUEBAS DE PRODUCTO COMERCIALIZABLE en su configuración final, es necesaria la realizacón de pruebas para la demostración, evaluación y certificación del sistema completo en un ambiente operativo real, así como probar su manufacturabilidad."
    elif evaluacion.pregunta8_2<=13:
        reco8="No está seguro de haber iniciado con las PRUEBAS DE PRODUCTO COMERCIALIZABLE en su configuración final, sin embargo, es muy probable que no haya realizado pruebas para la demostración, evaluación y certificación del sistema completo en un ambiente operativo real, así como probar su manufacturabilidad. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta8_2<=25:
        reco8="Ya ha iniciado con las PRUEBAS DE PRODUCTO COMERCIALIZABLE en su configuración final para demostración, evaluación y certificación del sistema completo, así como manufacturabilidad probada, sin embargo, es necesario documentar el proceso realizado; deben ser pruebas en un ambiente operativo real. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta8_2<=50:
        reco8="Ya ha iniciado con las PRUEBAS DE PRODUCTO COMERCIALIZABLE en su configuración final para demostración, evaluación y certificación del sistema completo, ha realizado pruebas en un ambiente operativo real, así como manufacturabilidad probada, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."




    if evaluacion.pregunta9_1==100:
        reco9="Se realiza la PRODUCCIÓN SOSTENIDA del producto terminado, se han realizado pruebas exitosas en entornos reales y la tecnología se encuentra disponible en el mercado, los procesos de producción y pruebas se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta9_1==0:
        reco9="No se realiza la PRODUCCIÓN SOSTENIDA del producto terminado, tampoco se han realizado pruebas exitosas en entornos reales y la tecnología no se encuentra disponible en el mercado."
    elif evaluacion.pregunta9_1<=13:
        reco9="No está seguro de haber con la PRODUCCIÓN SOSTENIDA del producto terminado, sin embargo, es muy probable que no se hayan realizado pruebas exitosas en entornos reales, así como tampoco que la tecnología se encuentra disponible en el mercado. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta9_1<=25:
        reco9="Ya ha iniciado con la PRODUCCIÓN SOSTENIDA del producto terminado, la tecnología aún no se encuentra disponible en el mercado, sin embargo, es necesario documentar los procesos de producción y pruebas; deben ser pruebas exitosas en entornos reales. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta9_1<=50:
        reco9="Ya ha iniciado con la PRODUCCIÓN SOSTENIDA del producto terminado, ha realizado pruebas en un ambiente operativo real, la tecnología aun no se encuentra disponible en el mercado, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."

    if evaluacion.pregunta9_3==100:
        reco10="Se realizan CAMBIOS INCREMENTALES del producto terminado, en la búsqueda de la mejora continua que lleven a crear nuevas versiones del producto, el proceso de mejora continua se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta9_3==0:
        reco10="No se realizan CAMBIOS INCREMENTALES del producto terminado que lleven a la mejora continua y permitan crear nuevas versiones del producto."
    elif evaluacion.pregunta9_3<=13:
        reco10="No se está seguro de realizar CAMBIOS INCREMENTALES del producto terminado, sin embargo, es muy probable que no se realicen acciones de mejora continua que lleven a crear nuevas versiones del producto. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta9_3<=25:
        reco10="Ya ha iniciado a realizar CAMBIOS INCREMENTALES del producto terminado, en la búsqueda de la mejora continua que lleven a crear nuevas versiones del producto, sin embargo, es necesario documentar el proceso. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta9_3<=50:
        reco10="Ya ha iniciado a realizar CAMBIOS INCREMENTALES del producto terminado que lleven a la mejora continua y permitan crear nuevas versiones del producto, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."



    if evaluacion.pregunta2_5==100:
        reco11="Cuenta con un GRUPO DE INVESTIGACIÓN Y DESARROLLO adecuado y acorde a las características técnicas, administrativas y operativas que demanda el proyecto, además ha documentado satisfactoriamente toda la información necesaria y anexos que validan el perfil y experiencia de cada miembro del GRUPO DE INVESTIGACIÓN Y DESARROLLO."
    elif evaluacion.pregunta2_5==0:
        reco11="No cuenta con un GRUPO DE INVESTIGACIÓN Y DESARROLLO adecuado y acorde a las características técnicas, administrativas y operativas que demanda el proyecto."   
    elif evaluacion.pregunta2_5<=13:
        reco11="No está seguro de contar con un GRUPO DE INVESTIGACIÓN Y DESARROLLO adecuado y acorde a las características técnicas, administrativas y operativas que demanda el proyecto, sin embargo, es muy probable que no tenga documentada satisfactoriamente toda la información necesaria y anexos que validan el perfil y experiencia de cada miembro del GRUPO DE INVESTIGACIÓN Y DESARROLLO. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta2_5<=25:
        reco11="Ya cuenta con un GRUPO DE INVESTIGACIÓN Y DESARROLLO adecuado y acorde a las características técnicas, administrativas y operativas que demanda el proyecto, sin embargo, es necesario documentar satisfactoriamente toda la información necesaria y anexos que validan el perfil y experiencia de cada miembro del GRUPO DE INVESTIGACIÓN Y DESARROLLO. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta2_5<=50:
        reco11="Ya cuenta con un GRUPO DE INVESTIGACIÓN Y DESARROLLO adecuado y acorde a las características técnicas, administrativas y operativas que demanda el proyecto, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso. Recuerde que la documentación, información y anexos necesarios deben validar el perfil y experiencia de cada miembro del GRUPO DE INVESTIGACIÓN Y DESARROLLO"



       
    if evaluacion.pregunta3_1==100:
        reco12="La IDENTIFICACIÓN DE LOS COMPONENTES de su invensión tecnológica, como análisis de requisitos, diseño de arquitectura de ingeniería, diagramas de bloques, diagramas de flujo, mapas mentales, etcétera; se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta3_1==0:
        reco12="No ha iniciado con la IDENTIFICACIÓN DE LOS COMPONENTES de su invensión tecnológica, es necesario revisar y analizar detalladamente la información obtenida en el tópico Investigación para posteriormente realizar análisis de requisitos, diseño de arquitectura de ingeniería, diagramas de bloques, diagramas de flujo, mapas mentales, etcétera."
    elif evaluacion.pregunta3_1<=13:
        reco12="No está seguro de haber iniciado con la IDENTIFICACIÓN DE LOS COMPONENTES de su invensión tecnológica, sin embargo, es muy probable que no cuente con análisis de requisitos, diseño de arquitectura de ingeniería, diagramas de bloques, diagramas de flujo, mapas mentales, etcétera. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta3_1<=25:
        reco12="Ya ha iniciado con la IDENTIFICACIÓN DE LOS COMPONENTES de su invensión tecnológica, sin embargo, es necesario documentar el proceso realizado; debe contar con análisis de requisitos, diseño de arquitectura de ingeniería, diagramas de bloques, diagramas de flujo, mapas mentales, etcétera. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta3_1<=50:
        reco12="Ya ha iniciado con la IDENTIFICACIÓN DE LOS COMPONENTES de su invensión tecnológica, ha realizado análisis de requisitos, diseño de arquitectura de ingeniería, diagramas de bloques, diagramas de flujo o mapas mentales, etcétera, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."



       
    if evaluacion.pregunta4_1==100:
        reco13="La INTEGRACIÓN DE LOS COMPONENTES de su invensión tecnológica, como Síntesis de Diseño, Matriz de Asignación Física/Funcional, Hoja de Descripción de Concepto, Diagramas Esquemáticos de Bloques, Hoja de Asignación de requisitos, etcétera; se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta4_1==0:
        reco13="No ha iniciado con la INTEGRACIÓN DE LOS COMPONENTES de su invensión tecnológica, es necesario realizar la Identificación de Componentes para posteriormente realizar Síntesis de Diseño, Matriz de Asignación Física/Funcional, Hoja de Descripción de Concepto, Diagramas Esquemáticos de Bloques, Hoja de Asignación de requisitos, etcétera."
    elif evaluacion.pregunta4_1<=13:
        reco13="No está seguro de haber iniciado con la INTEGRACIÓN DE LOS COMPONENTES de su invensión tecnológica, sin embargo, es muy probable que no cuente con Síntesis de Diseño, Matriz de Asignación Física/Funcional, Hoja de Descripción de Concepto, Diagramas Esquemáticos de Bloques, Hoja de Asignación de requisitos, etcétera. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta4_1<=25:
        reco13="Ya ha iniciado con la INTEGRACIÓN DE LOS COMPONENTES de su invensión tecnológica, sin embargo, es necesario documentar el proceso realizado; debe contar con Síntesis de Diseño, Matriz de Asignación Física/Funcional, Hoja de Descripción de Concepto, Diagramas Esquemáticos de Bloques, Hoja de Asignación de requisitos, etcétera. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta4_1<=50:
        reco13="Ya ha iniciado con la INTEGRACIÓN DE LOS COMPONENTES de su invensión tecnológica, ha realizado Síntesis de Diseño, Matriz de Asignación Física/Funcional, Hoja de Descripción de Concepto, Diagramas Esquemáticos de Bloques, Hoja de Asignación de requisitos, etcétera, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."


    if evaluacion.pregunta2_2==100:
        reco14="El BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, incluidos, análisis de patentabilidad y estudios de no infracción indicaron que no existe un desarrollo igual o similar a su invensión; dicho proceso e información se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta2_2==0:
        reco14="No ha iniciado con el BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, es necesario realizar un análisis de patentabilidad y estudios de no infracción que arrojen como resultado que no existe un desarrollo igual o similar a su invensión."
    elif evaluacion.pregunta2_2<=13:
        reco14="No está seguro de haber iniciado el BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, sin embargo, es muy probable que no cuente con análisis de patentabilidad y estudios de no infracción que arrojen como resultado que no existe un desarrollo igual o similar a su invensión. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta2_2<=25:
        reco14="Ya ha iniciado con el BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, sin embargo, es necesario documentar el proceso realizado; debe contar con análisis de patentabilidad y estudios de no infracción que arrojen como resultado que no existe un desarrollo igual o similar a su invensión. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta2_2<=50:
        reco14="Ya ha iniciado con el BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, ha realizado análisis de patentabilidad o estudios de no infracción indicaron que no existe un desarrollo igual o similar a su invensión, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."


    if evaluacion.pregunta3_3==100:
        reco15="La 1ER ACTUALIZACIÓN DEL BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, incluidos, análisis de patentabilidad y estudios de no infracción indicaron que no existe un desarrollo igual o similar a su invensión; dicho proceso e información se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta3_3==0:
        reco15="No ha iniciado con la 1ER ACTUALIZACIÓN BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, es necesario realizar un análisis de patentabilidad y estudios de no infracción que arrojen como resultado que no existe un desarrollo igual o similar a su invensión."
    elif evaluacion.pregunta3_3<=13:
        reco15="No está seguro de haber iniciado la 1ER ACTUALIZACIÓN BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, sin embargo, es muy probable que no cuente con análisis de patentabilidad y estudios de no infracción que arrojen como resultado que no existe un desarrollo igual o similar a su invensión. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta3_3<=25:
        reco15="Ya ha iniciado con la 1ER ACTUALIZACIÓN BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, sin embargo, es necesario documentar el proceso realizado; debe contar con análisis de patentabilidad y estudios de no infracción que arrojen como resultado que no existe un desarrollo igual o similar a su invensión. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta3_3<=50:
        reco15="Ya ha iniciado con la 1ER ACTUALIZACIÓN BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, ha realizado análisis de patentabilidad o estudios de no infracción indicaron que no existe un desarrollo igual o similar a su invensión, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."

        

    if evaluacion.pregunta4_7==100:
        reco16="La 2DA ACTUALIZACIÓN DEL BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, incluidos, análisis de patentabilidad y estudios de no infracción indicaron que no existe un desarrollo igual o similar a su invensión; dicho proceso e información se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta4_7==0:
        reco16="No ha iniciado con la 2DA ACTUALIZACIÓN DEL BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, es necesario realizar un análisis de patentabilidad y estudios de no infracción que arrojen como resultado que no existe un desarrollo igual o similar a su invensión."
    elif evaluacion.pregunta4_7<=13:
        reco16="No está seguro de haber iniciado la 2DA ACTUALIZACIÓN DEL BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, sin embargo, es muy probable que no cuente con análisis de patentabilidad y estudios de no infracción que arrojen como resultado que no existe un desarrollo igual o similar a su invensión. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta4_7<=25:
        reco16="Ya ha iniciado con la 2DA ACTUALIZACIÓN DEL BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, sin embargo, es necesario documentar el proceso realizado; debe contar con análisis de patentabilidad y estudios de no infracción que arrojen como resultado que no existe un desarrollo igual o similar a su invensión. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta4_7<=50:
        reco16="Ya ha iniciado con la 2DA ACTUALIZACIÓN DEL BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, ha realizado análisis de patentabilidad o estudios de no infracción indicaron que no existe un desarrollo igual o similar a su invensión, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."
        

    if evaluacion.pregunta5_4==100:
        reco17="La 3ER Y ÚLTIMA ACTUALIZACIÓN DEL BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, incluidos, análisis de patentabilidad y estudios de no infracción indicaron que no existe un desarrollo igual o similar a su invensión; dicho proceso e información se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta5_4==0:
        reco17="No ha iniciado con la 3ER Y ÚLTIMA ACTUALIZACIÓN DEL BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, es necesario realizar un análisis de patentabilidad y estudios de no infracción que arrojen como resultado que no existe un desarrollo igual o similar a su invensión."
    elif evaluacion.pregunta5_4<=13:
        reco17="No está seguro de haber iniciado la 3ER Y ÚLTIMA ACTUALIZACIÓN DEL BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, sin embargo, es muy probable que no cuente con análisis de patentabilidad y estudios de no infracción que arrojen como resultado que no existe un desarrollo igual o similar a su invensión. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta5_4<=25:
        reco17="Ya ha iniciado con la 3ER Y ÚLTIMA ACTUALIZACIÓN DEL BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, sin embargo, es necesario documentar el proceso realizado; debe contar con análisis de patentabilidad y estudios de no infracción que arrojen como resultado que no existe un desarrollo igual o similar a su invensión. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta5_4<=50:
        reco17="Ya ha iniciado con la 3ER Y ÚLTIMA ACTUALIZACIÓN DEL BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, ha realizado análisis de patentabilidad o estudios de no infracción indicaron que no existe un desarrollo igual o similar a su invensión, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."
        

    if evaluacion.pregunta3_4==100:
        reco18="Los RESULTADOS DEL BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, incluidos, análisis de patentabilidad y estudios de no infracción indicaron que el desarrollo puede ser protegido por algún mecanismo de PROPIEDAD INTELECTUAL; dicho proceso e información se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta3_4==0:
        reco18="No cuenta con los RESULTADOS DEL BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, los cuales arrojan como resultado cual es el mejor mecanismo de PROPIEDAD INTELECTUAL por el cual se puede proteger el desarrollo."
    elif evaluacion.pregunta3_4<=13:
        reco18="No está seguro de contar con los RESULTADOS DEL BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, sin embargo, es muy probable que no cuente con análisis de patentabilidad y estudios de no infracción que hayan arrojado como resultado que el desarrollo puede ser protegido por algún mecanismo de PROPIEDAD INTELECTUAL. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta3_4<=25:
        reco18="Ya cuenta con los RESULTADOS DEL BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, sin embargo, es necesario documentar el proceso realizado; debe contar con nálisis de patentabilidad y estudios de no infracción que hayan arrojado como resultado que el desarrollo puede ser protegido por algún mecanismo de PROPIEDAD INTELECTUAL. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta3_4<=50:
        reco18="Ya cuenta con los RESULTADOS DEL BENCHMARKING TECNOLÓGICO nacional e internacional de su invensión, ha realizado análisis de patentabilidad o estudios de no infracción indicaron que el desarrollo puede ser protegido por algún mecanismo de PROPIEDAD INTELECTUAL, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."
        

    if evaluacion.pregunta2_6==100:
        reco19="Se ha contemplado un PLAN DE LICENCIAMIENTO de tecnología a terceros, mediante un plan estrategico de transferencia tecnológica; dicho proceso e información se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta2_6==0:
        reco19="No se ha contemplado un PLAN DE LICENCIAMIENTO de tecnología a terceros, es necesario realizar un plan estrategico de transferencia tecnológica."
    elif evaluacion.pregunta2_6<=13:
        reco19="No está seguro de haber contemplado un PLAN DE LICENCIAMIENTO de tecnología a terceros, sin embargo, es muy probable que no cuente con un plan estrategico de transferencia tecnológica. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta2_6<=25:
        reco19="Ya ha contemplado un PLAN DE LICENCIAMIENTO de tecnología a terceros, sin embargo, es necesario documentar el proceso realizado; debe contar con un plan estrategico de transferencia tecnológica. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta2_6<=50:
        reco19="Ya ha contemplado un PLAN DE LICENCIAMIENTO de tecnología a terceros, ha realizado un plan estrategico de transferencia tecnológica, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."
        

    if evaluacion.pregunta3_6==100:
        reco20="Se ha ACTUALIZADO EL PLAN DE LICENCIAMIENTO de tecnología a terceros, mediante un plan estrategico de transferencia tecnológica; dicho proceso e información se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta3_6==0:
        reco20="No ha ACTUALIZADO EL PLAN DE LICENCIAMIENTO de tecnología a terceros, es necesario realizar un plan estrategico de transferencia tecnológica."
    elif evaluacion.pregunta3_6<=13:
        reco20="No está seguro de haber ACTUALIZADO EL PLAN DE LICENCIAMIENTO de tecnología a terceros, sin embargo, es muy probable que no cuente con un plan estrategico de transferencia tecnológica. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta3_6<=25:
        reco20="Ya ha ACTUALIZADO EL PLAN DE LICENCIAMIENTO de tecnología a terceros, sin embargo, es necesario documentar el proceso realizado; debe contar con un plan estrategico de transferencia tecnológica. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta3_36<=50:
        reco20="Ya ha ACTUALIZADO EL PLAN DE LICENCIAMIENTO de tecnología a terceros, ha realizado un plan estrategico de transferencia tecnológica, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."
        

    if evaluacion.pregunta4_8==100:
        reco21="Se ha realizado una 2DA ACTUALIZACIÓN DEL PLAN DE LICENCIAMIENTO de tecnología a terceros, mediante un plan estrategico de transferencia tecnológica; dicho proceso e información se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta4_8==0:
        reco21="No se ha realizado una 2DA ACTUALIZACIÓN DEL PLAN DE LICENCIAMIENTO de tecnología a terceros, es necesario realizar un plan estrategico de transferencia tecnológica."
    elif evaluacion.pregunta4_8<=13:
        reco21="No está seguro de haber realizado una 2DA ACTUALIZACIÓN DEL PLAN DE LICENCIAMIENTO de tecnología a terceros, sin embargo, es muy probable que no cuente con un plan estrategico de transferencia tecnológica. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta4_8<=25:
        reco21="Ya ha realizado una 2DA ACTUALIZACIÓN DEL PLAN DE LICENCIAMIENTO de tecnología a terceros, sin embargo, es necesario documentar el proceso realizado; debe contar con un plan estrategico de transferencia tecnológica. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta4_8<=50:
        reco21="Ya se ha realizado una 2DA ACTUALIZACIÓN DEL PLAN DE LICENCIAMIENTO de tecnología a terceros, ha realizado un plan estrategico de transferencia tecnológica, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."
        

    if evaluacion.pregunta6_0==100:
        reco22="La ESTRATEGIA DE PROTECCIÓN INTELECTUAL ha sido identificada y definida, la cual contempla tiempos, redacción de solicitud, componentes a proteger, mecanismo de protección, etcétera; dicho proceso e información se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta6_0==0:
        reco22="No cuenta con una ESTRATEGIA DE PROTECCIÓN INTELECTUAL identificada y definida, la cual contemple tiempos, redacción de solicitud, componentes a proteger, mecanismo de protección, etcétera."
    elif evaluacion.pregunta6_0<=13:
        reco22="No está seguro de contar con una ESTRATEGIA DE PROTECCIÓN INTELECTUAL identificada y definida, sin embargo, es muy probable que no tenga contemplado tiempos, redacción de solicitud, componentes a proteger, mecanismo de protección, etcétera. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta6_0<=25:
        reco22="Ya cuenta con una ESTRATEGIA DE PROTECCIÓN INTELECTUAL identificada y definida, sin embargo, es necesario documentar el proceso realizado; debe contemplar tiempos, redacción de solicitud, componentes a proteger, mecanismo de protección, etcétera. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta6_0<=50:
        reco22="Ya cuenta con una ESTRATEGIA DE PROTECCIÓN INTELECTUAL identificada y definida, ha contemplado tiempos, redacción de solicitud, componentes a proteger o mecanismo de protección, etcétera, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."
        

    if evaluacion.pregunta7_0==100:
        reco23="La EJECUCIÓN DE LA ESTRATEGIA DE PROTECCIÓN INTELECTUAL, la cual contempla solicitudes, folios, etcétera, se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta7_0==0:
        reco23="No ha realizado la EJECUCIÓN DE LA ESTRATEGIA DE PROTECCIÓN INTELECTUAL, la cual contempla solicitudes, folios, etcétera."
    elif evaluacion.pregunta7_0<=13:
        reco23="No está seguro de haber realizado la EJECUCIÓN DE LA ESTRATEGIA DE PROTECCIÓN INTELECTUAL, sin embargo, es muy probable que no cuente con solicitudes, folios, etcétera. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta7_0<=25:
        reco23="Ya ha realizado la EJECUCIÓN DE LA ESTRATEGIA DE PROTECCIÓN INTELECTUAL, sin embargo, es necesario documentar el proceso realizado; debe contemplar solicitudes, folios, etcétera. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta7_0<=50:
        reco23="Ya ha realizado la EJECUCIÓN DE LA ESTRATEGIA DE PROTECCIÓN INTELECTUAL, ha contemplado solicitudes, folios, etcétera, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."






    if evaluacion.pregunta3_5==100:
        reco24="El estudio sobre ASPECTOS REGULATORIOS que son requeridos para su invensión tecnológica, incluidos, análisis de comités de ética, normas, ISOs y certificaciones; dicho proceso se ha completado y documentado satisfactoriamente."
    elif evaluacion.pregunta3_5==0:
        reco24="No ha iniciado con el estudio sobre ASPECTOS REGULATORIOS que son requeridos para su invensión tecnológica, es necesario realizar un análisis de comités de ética, normas, ISOs y certificaciones."
    elif evaluacion.pregunta3_5<=13:
        reco24="No está seguro de haber iniciado el estudio sobre ASPECTOS REGULATORIOS que son requeridos para su invensión tecnológica, sin embargo, es muy probable que no cuente con análisis de comités de ética, normas, ISOs y certificaciones. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta3_5<=25:
        reco24="Ya ha iniciado con el estudio sobre ASPECTOS REGULATORIOS que son requeridos para su invensión tecnológica, sin embargo, es necesario documentar el proceso realizado; debe contar con análisis de comités de ética, normas, ISOs o certificaciones. Asegure realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta3_5<=50:
        reco24="Ya ha iniciado con el estudio sobre ASPECTOS REGULATORIOS que son requeridos para su invensión tecnológica, ha realizado análisis de comités de ética, normas, ISOs y certificaciones, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."
        
    
    
    
    if evaluacion.pregunta5_3==100:
        reco25="Los resultados experimentales del prototipo a escala se alinean a los ASPECTOS REGULATORIOS que son requeridos para su invensión tecnológica, incluidos, comités de ética, normas, ISOs, certificaciones, previsiones legales o del medio ambiente del sector; dicho proceso se ha completado y documentado satisfactoriamente."
    elif evaluacion.pregunta5_3==0:
        reco25="Los resultados experimentales del prototipo a escala NO se alinean a los ASPECTOS REGULATORIOS que son requeridos para su invensión tecnológica, es necesario realizar un análisis de comités de ética, normas, ISOs, certificaciones, previsiones legales o del medio ambiente del sector."
    elif evaluacion.pregunta5_5<=13:
        reco25="No está seguro de que los resultados experimentales del prototipo a escala se encuentren alineados a ASPECTOS REGULATORIOS que son requeridos para su invensión tecnológica, sin embargo, es muy probable que no cuente con análisis de comités de ética, normas, ISOs, certificaciones, previsiones legales o del medio ambiente del sector. Revisar cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta5_3<=25:
        reco25="Los resultados experimentales del prototipo a escala se alinean a algunos ASPECTOS REGULATORIOS que son requeridos para su invensión tecnológica, sin embargo, es necesario documentar el proceso realizado; debe contar con análisis de comités de ética, normas, ISOs, certificaciones, previsiones legales o del medio ambiente del sector. Asegure realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta5_3<=50:
        reco25="Los resultados experimentales del prototipo a escala se alinean a algunos ASPECTOS REGULATORIOS que son requeridos para su invensión tecnológica, incluyendo comités de ética, normas, ISOs, certificaciones, previsiones legales o del medio ambiente del sector, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."
    
    
    
    if evaluacion.pregunta6_5==100:
        reco26="Inició el proceso de registro sobre CERTIFICACIONES GUBERNAMENTALES para la producción y despliegue del prototipo, cuenta con documentación oficial que da constancia del inicio de trámites; dicho proceso se ha completado y documentado satisfactoriamente."
    elif evaluacion.pregunta6_5==0:
        reco26="No ha iniciado con el proceso de registro sobre CERTIFICACIONES GUBERNAMENTALES para la producción y despliegue del prototipo, es necesario contar con documentación oficial que de constancia del inicio de trámites."
    elif evaluacion.pregunta6_5<=13:
        reco26="No está seguro de haber iniciado el proceso de registro sobre CERTIFICACIONES GUBERNAMENTALES para la producción y despliegue del prototipo, sin embargo, es muy probable que no cuente documentación oficial que de constancia de dichos trámites. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta6_5<=25:
        reco26="Ya ha iniciado con el proceso de registro sobre CERTIFICACIONES GUBERNAMENTALES para la producción y despliegue del prototipo, sin embargo, es necesario documentar el proceso realizado; debe contar con documentación oficial que de constancia del inicio de trámites. Asegure realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta6_5<=50:
        reco26="Ya ha iniciado con el proceso de registro sobre CERTIFICACIONES GUBERNAMENTALES para la producción y despliegue del prototipo, aparentemente cuenta con documentación oficial que da constancia del inicio de trámites o quizá no ha seleccionado correctamente los ASPECTOS REGULATORIOS que son requeridos para su prototipo, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."



    if evaluacion.pregunta8_4==100:
        reco27="El prototipo CUMPLE con los ESTÁNDARES Y CERTIFICACIONES GUBERNAMENTALES que son requeridos por la industria en cuestión, cuenta con documentación oficial que da constancia del cumplimiento; dicho proceso se ha completado y documentado satisfactoriamente."
    elif evaluacion.pregunta8_4==0:
        reco27="El prototipo NO CUMPLE con los ESTÁNDARES Y CERTIFICACIONES GUBERNAMENTALES que son requeridos por la industria en cuestión, es necesario contar con documentación oficial que de constancia del cumplimiento."
    elif evaluacion.pregunta8_4<=13:
        reco27="No está seguro de que el prototipo cumpla con los ESTÁNDARES Y CERTIFICACIONES GUBERNAMENTALES que son requeridos por la industria en cuestión, sin embargo, es muy probable que no cuente con documentación oficial que de constancia del cumplimiento. Revisar cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta8_4<=25:
        reco27="El prototipo a escala CUMPLE con algunos ESTÁNDARES Y CERTIFICACIONES GUBERNAMENTALES que son requeridos por la industria en cuestión, sin embargo, es necesario contar con documentación oficial que de constancia del cumplimiento. Asegure realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta8_4<=50:
        reco27="El prototipo a escala CUMPLE con algunos ESTÁNDARES Y CERTIFICACIONES GUBERNAMENTALES que son requeridos por la industria en cuestión, aparentemente cuenta con documentación oficial que da constancia del cumplimiento o quizá los resultados del trámite no han sido favorables, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."








    if evaluacion.pregunta2_3==100:
        reco28="Ha explorado principios básicos de MANUFACTURABILIDAD que son requeridos para su invensión tecnológica, incluidos, identificación, estudios en papel y análisis de enfoques de materiales y procesos; dicho proceso se ha completado y documentado satisfactoriamente."
    elif evaluacion.pregunta2_3==0:
        reco28="No ha explorado principios básicos de MANUFACTURABILIDAD que son requeridos para su invensión tecnológica, es necesario realizar la identificación, estudios en papel y análisis de enfoques de materiales y procesos."
    elif evaluacion.pregunta2_3<=13:
        reco28="No está seguro de haber iniciado la exploración de principios básicos de MANUFACTURABILIDAD que son requeridos para su invensión tecnológica, sin embargo, es muy probable que no cuente la identificación, estudios en papel y análisis de enfoques de materiales y procesos. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta2_3<=25:
        reco28="Ya ha explorado principios básicos de MANUFACTURABILIDAD que son requeridos para su invensión tecnológica, sin embargo, es necesario documentar el proceso realizado; debe contar con una identificación, estudios en papel o análisis de enfoques de materiales y procesos. Asegure realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta2_3<=50:
        reco28="Ya ha explorado principios básicos de MANUFACTURABILIDAD que son requeridos para su invensión tecnológica, ha realizado la identificación, estudios en papel y análisis de enfoques de materiales y procesos, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."


    if evaluacion.pregunta4_3==100:
        reco29="Ha explorado con mayor profundidad los principios de MANUFACTURABILIDAD que son requeridos para su invensión tecnológica, se cuenta con capacidad para producir la tecnología en un entorno de laboratorio, incluidos, la identificación de riesgos de fabricación para la construcción de prototipos y elaboración de planes de mitigación; dicho proceso se ha completado y documentado satisfactoriamente."
    elif evaluacion.pregunta4_3==0:
        reco29="No ha explorado a profundidad los principios de MANUFACTURABILIDAD que son requeridos para su invensión tecnológica, no cuenta con capacidad para producir la tecnología en un entorno de laboratorio; es necesario realizar la identificación de riesgos de fabricación para la construcción de prototipos y elaboración de planes de mitigación."
    elif evaluacion.pregunta4_3<=13:
        reco29="No está seguro de haber iniciado la exploración a mayor profundidad de los principios de MANUFACTURABILIDAD que son requeridos para su invensión tecnológica, desconoce si cuenta con capacidad para producir la tecnología en un entorno de laboratorio, sin embargo, es muy probable que no cuente la identificación de riesgos de fabricación para la construcción de prototipos y elaboración de planes de mitigación. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta4_3<=25:
        reco29="Ya ha explorado con mayor profundidad los principios de MANUFACTURABILIDAD que son requeridos para su invensión tecnológica, se cuenta con capacidad para producir la tecnología en un entorno de laboratorio, sin embargo, es necesario documentar el proceso realizado; debe contar con una identificación de riesgos de fabricación para la construcción de prototipos o elaboración de planes de mitigación. Asegure realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta4_3<=50:
        reco29="Ya ha explorado con mayor profundidad los principios de MANUFACTURABILIDAD que son requeridos para su invensión tecnológica, ha realizado la identificación de riesgos de fabricación para la construcción de prototipos y elaboración de planes de mitigación, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."


    if evaluacion.pregunta5_2==100:
        reco30="Ha identificado y considerado plenamente aspectos de MANUFACTURABILIDAD del futuro producto, cuenta con capacidad para producir prototipos en un entorno relevante, incluidos, la evaluación de la base industrial para identificar posibles fuentes de fabricación. Se ha perfeccionado e integrado una estrategia de fabricación con el plan de gestión de riesgos; dicho proceso se ha completado y documentado satisfactoriamente."
    elif evaluacion.pregunta5_2==0:
        reco30="No ha identificado y considerado plenamente aspectos de MANUFACTURABILIDAD del futuro producto, no cuenta con capacidad para producir prototipos en un entorno relevante; es necesario realizar la evaluación de la base industrial para identificar posibles fuentes de fabricación. Perfeccionar e integrar una estrategia de fabricación con el plan de gestión de riesgos."
    elif evaluacion.pregunta5_2<=13:
        reco30="No está seguro de haber considerado e identificado plenamente aspectos de MANUFACTURABILIDAD del futuro producto, desconoce si cuenta con capacidad para producir prototipos en un entorno relevante, sin embargo, es muy probable que no cuente la evaluación de la base industrial para identificar posibles fuentes de fabricación. Y tampoco perfeccionado e integrado una estrategia de fabricación con el plan de gestión de riesgos. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta5_2<=25:
        reco30="Ya ha identificado y considerado plenamente aspectos de MANUFACTURABILIDAD del futuro producto, cuenta con capacidad limitada para producir prototipos en un entorno relevante, sin embargo, es necesario documentar el proceso realizado; debe contar con una evaluación de la base industrial para identificar posibles fuentes de fabricación. Así como haber perfeccionado e integrado una estrategia de fabricación con el plan de gestión de riesgosn. Asegure realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta5_2<=50:
        reco30="Ya ha identificado y considerado plenamente aspectos de MANUFACTURABILIDAD del futuro producto, cuenta con capacidad limitada para producir prototipos en un entorno relevante, ha realizado la evaluación de la base industrial para identificar posibles fuentes de fabricación. Ha perfeccionado e integrado una estrategia de fabricación con el plan de gestión de riesgos, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."



    if evaluacion.pregunta6_1==100:
        reco31="Ha integrado LAS TECNOLOGÍAS DE PRODUCTO Y DE MANUFACTURA en una planta piloto, considerando, un proceso de definición y caracterización de la mayoría de los procesos de fabricación; este proceso se ha completado y documentado satisfactoriamente."
    elif evaluacion.pregunta6_1==0:
        reco31="No ha integrado LAS TECNOLOGÍAS DE PRODUCTO Y DE MANUFACTURA en una planta piloto; es necesario definir y caracterizar la mayoría de los procesos de fabricación."  
    elif evaluacion.pregunta6_1<=13:
        reco31="No está seguro de haber integrado LAS TECNOLOGÍAS DE PRODUCTO Y DE MANUFACTURA en una planta piloto, sin embargo, es muy probable que no cuente con un proceso de definición y caracterización de la mayoría de los procesos de fabricación. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta6_1<=25:
        reco31="Ya ha integrado LAS TECNOLOGÍAS DE PRODUCTO Y DE MANUFACTURA en una planta piloto, sin embargo, es necesario documentar con un proceso de definición y caracterización de la mayoría de los procesos de fabricación. Asegure realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta6_1<=50:
        reco31="Ya ha integrado LAS TECNOLOGÍAS DE PRODUCTO Y DE MANUFACTURA en una planta piloto, ha realizado procesos de definición y caracterización de la mayoría de los procesos de fabricación, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."


    if evaluacion.pregunta6_2==100:
        reco32="Tiene alineado el nuevo producto con las TECNOLOGÍAS DE PRODUCCIÓN, considerando, procesos de aceptación de un diseño de producto preliminar y enfoque de fabricación inicial, así como evaluaciones de manufacturabilidad y estudios comerciales de tecnologías y componentes clave; dicho proceso se ha completado y documentado satisfactoriamente."
    elif evaluacion.pregunta6_2==0:
        reco32="No tiene alineado el nuevo producto con las TECNOLOGÍAS DE PRODUCCIÓN; es necesario realizar procesos de aceptación de un diseño de producto preliminar y enfoque de fabricación inicial, así como evaluaciones de manufacturabilidad y estudios comerciales de tecnologías y componentes clave."
    elif evaluacion.pregunta6_2<=13:
        reco32="No está seguro tener alineado el nuevo producto con las TECNOLOGÍAS DE PRODUCCIÓN, sin embargo, es muy probable que no cuente con procesos de aceptación de un diseño de producto preliminar, enfoque de fabricación inicial, así como tampoco evaluaciones de manufacturabilidad y estudios comerciales de tecnologías y componentes clave. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta6_2<=25:
        reco32="Ya tiene alineado el nuevo producto con las TECNOLOGÍAS DE PRODUCCIÓN, sin embargo, es necesario documentar el proceso realizado; debe contar con procesos de aceptación de un diseño de producto preliminar y enfoque de fabricación inicial, así como evaluaciones de manufacturabilidad y estudios comerciales de tecnologías y componentes clave. Asegure realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta6_2<=50:
        reco32="Ya tiene alineado el nuevo producto con las TECNOLOGÍAS DE PRODUCCIÓN, ha realizado procesos de aceptación de un diseño de producto preliminar, enfoque de fabricación inicial y/o evaluaciones de manufacturabilidad y estudios comerciales de tecnologías y componentes clave, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."


    if evaluacion.pregunta7_1==100:
        reco33="Cuenta con un proceso operacional de MANUFACTURA EN BAJA ESCALA con capacidad para producir productos comerciales en un entorno representativo de producción; incluidas, actividades de diseño detallado del producto semi-terminado. También ha probado las especificaciones y disponibilidad de los materiales para cumplir con el cronograma de MANUFACTURA EN BAJA ESCALA; dichos procesos se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta7_1==0:
        reco33="No cuenta con un proceso operacional de MANUFACTURA EN BAJA ESCALA, no cuenta con capacidad para producir productos comerciales en un entorno representativo de producción; es necesario realizar actividades de diseño detallado del producto semi-terminado. Así como probar las especificaciones y disponibilidad de los materiales para cumplir con el cronograma de MANUFACTURA EN BAJA ESCALA."   
    elif evaluacion.pregunta7_1<=13:
        reco33="No está seguro de contar con un proceso operacional de MANUFACTURA EN BAJA ESCALA, con capacidad para producir productos comerciales en un entorno representativo de producción, sin embargo, es muy probable que no haya realizado actividades de diseño detallado del producto semi-terminado. Así como también es probable que no haya probado las especificaciones y disponibilidad de los materiales para cumplir con el cronograma de construcción de MANUFACTURA EN BAJA ESCALA. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta7_1<=25:
        reco33="Ya cuenta con un proceso operacional de MANUFACTURA EN BAJA ESCALA con capacidad para producir productos comerciales en un entorno representativo de producción, sin embargo, es necesario documentar el proceso realizado; debe haber realizado actividades de diseño detallado del producto semi-terminado. También debe haber probado las especificaciones y disponibilidad de los materiales para cumplir con el cronograma de MANUFACTURA EN BAJA ESCALA. Asegure realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta7_1<=50:
        reco33="Ya cuenta con un proceso operacional de MANUFACTURA EN BAJA ESCALA con capacidad para producir productos comerciales en un entorno representativo de producción, ha realizado actividades de diseño detallado del producto semi-terminado. También debe haber probado las especificaciones y disponibilidad de los materiales para cumplir con el cronograma de MANUFACTURA EN BAJA ESCALA, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."


    if evaluacion.pregunta8_1==100:
        reco34="Se encuentra MANUFACTURANDO el producto en su versión final, capacidad establecida para comenzar la producción a velocidad completa; incluidos, el cumplimiento de todos los requisitos de ingeniería-diseño del producto de manera que haya cambios mínimos en el mismo. Se ha asegurado mediante pruebas y evaluaciones que las principales características de diseño del producto son estables. Y finalmente, se ha asegurado que los materiales, las piezas, la mano de obra, las herramientas, los equipos de prueba y las instalaciones están disponibles para cumplir con los programas de MANUFACTURA a velocidad planificada; dichos procesos se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta8_1==0:
        reco34="No se encuentra MANUFACTURANDO el producto en su versión final, no cuenta con capacidad establecida para comenzar la producción a velocidad completa; es necesario realizar actividades que aseguren el cumplimiento de todos los requisitos de ingeniería-diseño del producto de manera que haya cambios mínimos en el mismo. No se ha asegurado mediante pruebas y evaluaciones que las principales características de diseño del producto son estables. Y finalmente, tampoco se ha asegurado que los materiales, las piezas, la mano de obra, las herramientas, los equipos de prueba y las instalaciones están disponibles para cumplir con los programas de MANUFACTURA a velocidad planificada."
    elif evaluacion.pregunta8_1<=13:
        reco34="No está seguro de encontrarse MANUFACTURANDO el producto en su versión final, por lo que tampoco cuenta con certeza de contar con capacidad establecida para comenzar la producción a velocidad completa, sin embargo, es muy probable que no haya realizado actividades que aseguren el cumplimiento de todos los requisitos de ingeniería-diseño del producto de manera que haya cambios mínimos en el mismo. Por lo que tampoco se asegura que las principales características de diseño del producto sean estables. Y finalmente, no se ha asegurado que los materiales, las piezas, la mano de obra, las herramientas, los equipos de prueba y las instalaciones están disponibles para cumplir con los programas de MANUFACTURA a velocidad planificada. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta8_1<=25:
        reco34="Ya se encuentra MANUFACTURANDO el producto en su versión final, con capacidad establecida para comenzar la producción a velocidad completa, sin embargo, es necesario documentar el proceso realizado; debe haber realizado actividades que aseguren el cumplimiento de todos los requisitos de ingeniería-diseño del producto de manera que haya cambios mínimos en el mismo. Debe asegurar mediante pruebas y evaluaciones que las principales características de diseño del producto son estables. Y finalmente, debe asegurar que los materiales, las piezas, la mano de obra, las herramientas, los equipos de prueba y las instalaciones están disponibles para cumplir con los programas de MANUFACTURA a velocidad planificada. Asegure realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta8_1<=50:
        reco34="Ya se encuentra MANUFACTURANDO el producto en su versión final, con capacidad establecida para comenzar la producción a velocidad completa, ha realizado actividades que aseguren el cumplimiento de todos los requisitos de ingeniería-diseño del producto de manera que haya cambios mínimos en el mismo. Se ha asegurado mediante pruebas y evaluaciones que las principales características de diseño del producto son estables. Y finalmente, se ha asegurado que los materiales, las piezas, la mano de obra, las herramientas, los equipos de prueba y las instalaciones están disponibles para cumplir con los programas de MANUFACTURA a velocidad planificada, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."



    if evaluacion.pregunta9_4==100:
        reco35="Los PROCESOS DE MANUFACTURA Y PRODUCCIÓN son optimizados a través de innovaciones incrementales, la producción es sostenida y demostrada; incluso, los cambios de ingeniería-diseño son pocos y generalmente se limitan a mejoras de calidad y costos. El producto, los componentes o los elementos están en plena producción y cumplen con todos los requisitos de ingeniería, rendimiento, calidad y confiabilidad; dichos procesos se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta9_4==0:
        reco35="No se cuenta con PROCESOS DE MANUFACTURA Y PRODUCCIÓN optimizados a través de innovaciones incrementales, la producción no es sostenida ni demostrada; es necesario realizar actividades que aseguren pocos cambios de ingeniería-diseño y que únicamente se limiten a mejoras de calidad y costos. El producto, los componentes o los elementos no están en plena producción y no cumplen con todos los requisitos de ingeniería, rendimiento, calidad y confiabilidad."
    elif evaluacion.pregunta9_4<=13:
        reco35="No está seguro de contar PROCESOS DE MANUFACTURA Y PRODUCCIÓN optimizados a través de innovaciones incrementales, la producción puede no ser sostenida ni demostrada, sin embargo, es muy probable que no haya realizado actividades que aseguren pocos cambios de ingeniería-diseño y que se limiten a mejoras de calidad y costo. Es muy probable que el producto, los componentes o los elementos no estén en plena producción y no cumplan con todos los requisitos de ingeniería, rendimiento, calidad y confiabilidad. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta9_4<=25:
        reco35="Ya se cuenta con PROCESOS DE MANUFACTURA Y PRODUCCIÓN optimizados a través de innovaciones incrementales, la producción probablemente es sostenida y demostrada, sin embargo, es necesario documentar el proceso realizado; debe haber realizado actividades que aseguren pocos cambios de ingeniería-diseño y que se limiten a mejoras de calidad y costo. El producto, los componentes o los elementos quizá están en plena producción y cumplen con todos los requisitos de ingeniería, rendimiento, calidad y confiabilidad. Asegure realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta9_4<=50:
        reco35="Ya se cuenta con PROCESOS DE MANUFACTURA Y PRODUCCIÓN optimizados a través de innovaciones incrementales, la producción es sostenida y demostrada, ha realizado actividades que aseguren poco cambios de ingeniería-diseño y que se limiten a mejoras de calidad y costo. El producto, los componentes o los elementos están en plena producción y cumplen con todos los requisitos de ingeniería, rendimiento, calidad y confiabilidad, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."






    if evaluacion.pregunta2_4==100:
        reco36="Ha explorado POSIBLES USUARIOS/MERCADO de su invensión, mediante estudios básicos de mercado e identificación de la problemática a resolver, que le indiquen target potencial, tamaño, localización y características generales; dicho proceso e información se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta2_4==0:
        reco36="No ha explorado POSIBLES USUARIOS/MERCADO de su invensión, es necesario realizar estudios básicos de mercado e identificación de la problemática a resolver, que le indiquen target potencial, tamaño, localización y características generales."
    elif evaluacion.pregunta2_4<=13:
        reco36="No está seguro de haber explorado POSIBLES USUARIOS/MERCADO de su invensión, sin embargo, es muy probable que no cuente con estudios básicos de mercado e identificación de la problemática a resolver, que le indiquen target potencial, tamaño, localización y características generales. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta2_4<=25:
        reco36="Ya ha explorado POSIBLES USUARIOS/MERCADO de su invensión, sin embargo, es necesario documentar el proceso realizado; debe contar con estudios básicos de mercado e identificación de la problemática a resolver, que le indiquen target potencial, tamaño, localización y características generales. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta2_4<=50:
        reco36="Ya ha explorado POSIBLES USUARIOS/MERCADO de su invensión, ha realizado estudios básicos de mercado e identificación de la problemática a resolver, que le indiquen target potencial, tamaño, localización y características generales, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."


    if evaluacion.pregunta3_2==100:
        reco37="Ha realizado algún proceso de VALIDACIÓN DE MERCADO de su invensión, mediante una actualización de los estudios de mercado y primeras pláticas y/o reuniones con posibles usuarios, cuenta con actas de reunión y/o cartas de interés de su invensión tecnológica; dicho proceso e información se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta3_2==0:
        reco37="No ha realizado ningún proceso de VALIDACIÓN DE MERCADO de su invensión, es necesario realizar una actualización de los estudios de mercado y primeras pláticas y/o reuniones con posibles usuarios, no cuenta con actas de reunión ni cartas de interés de su invensión tecnológica."
    elif evaluacion.pregunta3_2<=13:
        reco37="No está seguro de haber realizado algún proceso de VALIDACIÓN DE MERCADO de su invensión, sin embargo, es muy probable que no cuente con una actualización de los estudios de mercado y primeras pláticas y/o reuniones con posibles usuarios, así como también es probable que no cuente con actas de reunión y/o cartas de interés de su invensión tecnológica. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta3_2<=25:
        reco37="Ya ha realizado algún proceso de VALIDACIÓN DE MERCADO de su invensión, sin embargo, es necesario documentar el proceso realizado; debe contar una actualización de los estudios de mercado y primeras pláticas y/o reuniones con posibles usuarios, además de actas de reunión y/o cartas de interés de su invensión tecnológica. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta3_2<=50:
        reco37="Ya ha realizado algún proceso de VALIDACIÓN DE MERCADO de su invensión, ha realizado una actualización de los estudios de mercado y primeras pláticas y/o reuniones con posibles usuarios, cuenta con actas de reunión y/o cartas de interés de su invensión tecnológica, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."


    if evaluacion.pregunta4_4==100:
        reco38="HA ACTUALIZADO LA VALIDACIÓN DE MERCADO de su invensión tecnológica, mediante una 2da actualización de los estudios de mercado y más pláticas, reuniones y/o entrevistas con usuarios potenciales, cuenta con actas de reunión y/o cartas de interés de su invensión tecnológica; dicho proceso e información se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta4_4==0:
        reco38="No ha ACTUALIZADO LA VALIDACIÓN DE MERCADO de su invensión tecnológica, es necesario realizar una 2da actualización de los estudios de mercado y más pláticas, reuniones y/o entrevistas con usuarios potenciales, no cuenta con actas de reunión y/o cartas de interés de su invensión tecnológica."
    elif evaluacion.pregunta4_4<=13:
        reco38="No está seguro de haber ACTUALIZADO LA VALIDACIÓN DE MERCADO de su invensión tecnológica, sin embargo, es muy probable que no cuente con una 2da actualización de los estudios de mercado y más pláticas, reuniones y/o entrevistas con usuarios potenciales, así como también es probable que no cuente con actas de reunión y/o cartas de interés de su invensión tecnológica. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta4_4<=25:
        reco38="Ya ha ACTUALIZADO LA VALIDACIÓN DE MERCADO de su invensión tecnológica, sin embargo, es necesario documentar el proceso realizado; debe contar una 2da actualización de los estudios de mercado y más pláticas, reuniones y/o entrevistas con usuarios potenciales, además de actas de reunión y/o cartas de interés de su invensión tecnológica. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta4_4<=50:
        reco38="Ya ha ACTUALIZADO LA VALIDACIÓN DE MERCADO de su invensión tecnológica, ha realizado una 2da actualización de los estudios de mercado y más pláticas, reuniones y/o entrevistas con usuarios potenciales, cuenta con actas de reunión y/o cartas de interés de su invensión tecnológica, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."


    if evaluacion.pregunta6_3==100:
        reco39="Cuenta con usuarios potenciales que PRUEBEN LA PRODUCCIÓN A BAJA ESCALA de su producto, ha realizado más pláticas, reuniones y/o entrevistas con los usuarios potenciales, también cuenta con actas de reunión y/o cartas de interés en las pruebas de su producto; dicho proceso e información se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta6_3==0:
        reco39="No cuenta con usuarios potenciales que PRUEBEN LA PRODUCCIÓN A BAJA ESCALA de su producto, es necesario realizar más pláticas, reuniones y/o entrevistas con los usuarios potenciales, tampoco cuenta con actas de reunión y/o cartas de interés en las pruebas de su producto."
    elif evaluacion.pregunta6_3<=13:
        reco39="No está seguro de contar con usuarios potenciales que PRUEBEN LA PRODUCCIÓN A BAJA ESCALA de su producto, sin embargo, es muy probable que no haya realizado más pláticas, reuniones y/o entrevistas con los usuarios potenciales, así como también es probable que no cuente con actas de reunión y/o cartas de interés en las pruebas de su producto. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta6_3<=25:
        reco39="Ya cuenta con usuarios potenciales que PRUEBEN LA PRODUCCIÓN A BAJA ESCALA de su producto, sin embargo, es necesario documentar el proceso realizado; debe contar más pláticas, reuniones y/o entrevistas con usuarios potenciales, además de actas de reunión y/o cartas de interés en las pruebas de su producto. Asegúrese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta6_3<=50:
        reco39="Ya cuenta con usuarios potenciales que PRUEBEN LA PRODUCCIÓN A BAJA ESCALA de su producto, ha realizado más pláticas, reuniones y/o entrevistas con usuarios potenciales, cuenta con actas de reunión y/o cartas de interés en las pruebas de su producto, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."


    if evaluacion.pregunta7_2==100:
        reco40="Cuenta con usuarios potenciales que PRUEBEN LA VERSIÓN FINAL de su producto, ha realizado más pláticas, reuniones y/o entrevistas con los usuarios potenciales, también cuenta con actas de reunión y/o cartas de interés en la versión final de su producto; dicho proceso e información se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta7_2==0:
        reco40="No cuenta con usuarios potenciales que PRUEBEN LA VERSIÓN FINAL de su producto, es necesario realizar más pláticas, reuniones y/o entrevistas con los usuarios potenciales, tampoco cuenta con actas de reunión y/o cartas de interés en la versión final de su producto."
    elif evaluacion.pregunta7_2<=13:
        reco40="No está seguro de contar con usuarios potenciales que PRUEBEN LA VERSIÓN FINAL de su producto, sin embargo, es muy probable que no haya realizado más pláticas, reuniones y/o entrevistas con los usuarios potenciales, así como también es probable que no cuente con actas de reunión y/o cartas de interés en la versión final de su producto. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta7_2<=25:
        reco40="Ya cuenta con usuarios potenciales que PRUEBEN LA VERSIÓN FINAL de su producto, sin embargo, es necesario documentar el proceso realizado; debe contar más pláticas, reuniones y/o entrevistas con usuarios potenciales, además de actas de reunión y/o cartas de interés en la versión final de su producto. Asegúrese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta7_2<=50:
        reco40="Ya cuenta con usuarios potenciales que PRUEBEN LA VERSIÓN FINAL de su producto, ha realizado más pláticas, reuniones y/o entrevistas con usuarios potenciales, cuenta con actas de reunión y/o cartas de interés en la versión final de su producto, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."


    if evaluacion.pregunta8_5==100:
        reco41="Elaboró el respectivo MANUAL DE USUARIO, SOPORTE TÉCNICO Y MANTENIMIENTO de la versión final de su producto, mediante la elaboración de un manual de instrucciones uso; dicho proceso e información se han completado y documentado satisfactoriamente."
    elif evaluacion.pregunta8_5==0:
        reco41="No elaboró el respectivo MANUAL DE USUARIO, SOPORTE TÉCNICO Y MANTENIMIENTO de la versión final de su producto, es necesario realizar un manual de instrucciones de uso."
    elif evaluacion.pregunta8_5<=13:
        reco41="No está seguro de contar con un MANUAL DE USUARIO, SOPORTE TÉCNICO Y MANTENIMIENTO de la versión final de su producto, sin embargo, es muy probable que no haya realizado un manual de instrucciones de uso. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta8_5<=25:
        reco41="Ya cuenta con un MANUAL DE USUARIO, SOPORTE TÉCNICO Y MANTENIMIENTO de la versión final de su producto, sin embargo, es necesario documentar el proceso realizado; debe contar un manual de instrucciones de uso. Asegúrese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta8_5<=50:
        reco41="Ya cuenta con un MANUAL DE USUARIO, SOPORTE TÉCNICO Y MANTENIMIENTO de la versión final de su producto, ha elaborado algún tipo de manual de instrucciones de uso, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."





    if evaluacion.pregunta4_6==100:
        reco42="La IDENTIFICACIÓN DE RIESGOS TECNOLÓGICOS de mercado y financieros de su invensión se ha completado y documentado satisfactoriamente."
    elif evaluacion.pregunta4_6==0:
        reco42="No ha realizado la IDENTIFICACIÓN DE RIESGOS TECNOLÓGICOS de mercado y financieros de su invensión, es necesario realizar estudios básicos-preliminares de riesgos tecnológicos de mercado y financieros. Busque apoyo de un especialista"
    elif evaluacion.pregunta4_6<=13:
        reco42="No está seguro de haber realizado la IDENTIFICACIÓN DE RIESGOS TECNOLÓGICOS de mercado y financieros de su invensión, sin embargo, es muy probable que no haya realizado estudios básicos-preliminares de riesgos. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta4_6<=25:
        reco42="Ya ha iniciado con la IDENTIFICACIÓN DE RIESGOS TECNOLÓGICOS de mercado y financieros de su invensión, sin embargo, es necesario documentar el proceso realizado; deben ser estudios básicos-preliminares. Busque apoyo de un especialista. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta4_6<=50:
        reco42="Ya ha iniciado con la IDENTIFICACIÓN DE RIESGOS TECNOLÓGICOS de mercado y financieros de su invensión, ha realizado estudios básicos-preliminares de riesgos, sin embargo, es necesario revisar cuidadosamente la información disponible  y la documentación realizada durante el proceso."



    if evaluacion.pregunta6_4==100:
        reco43="Cuenta con una ORGANIZACIÓN OPERATIVA acorde a las necesidades de operación de la producción; considerando aspectos como mercadotecnia, logística, producción y otros, documentado en un brochure y/o perfil de la organización, todo este proceso e información se ha completado y documentado satisfactoriamente."
    elif evaluacion.pregunta6_4==0:
        reco43="No cuenta con una ORGANIZACIÓN OPERATIVA acorde a las necesidades de operación de la producción; considerando aspectos como mercadotecnia, logística, producción y otros; no cuenta con un brochure y/o perfil de la organización."
    elif evaluacion.pregunta6_4<=13:
        reco43="No está seguro de contar con una ORGANIZACIÓN OPERATIVA acorde a las necesidades de operación de la producción, sin embargo, es muy probable que no haya considerado aspectos como mercadotecnia, logística, producción y otros, realizado un brochure y/o perfil de la organización. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta6_4<=25:
        reco43="Ya cuenta con una ORGANIZACIÓN OPERATIVA acorde a las necesidades de operación de la producción, sin embargo, es necesario documentar el proceso realizado; deben considerarse aspectos como mercadotecnia, logística, producción y otros, documentado en un brochure y/o perfil de la organización. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta6_4<=50:
        reco43="Ya cuenta con una ORGANIZACIÓN OPERATIVA acorde a las necesidades de operación de la producción, ha considerado aspectos como mercadotecnia, logística, producción y otros, documentado en un brochure y/o perfil de la organización, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."



    if evaluacion.pregunta7_3==100:
        reco44="Cuenta con una ESTRUCTURA ORGANIZACIONAL adecuada para la implementación; considerando organigrama, acta constitutiva, plan de negocios, cédula fiscal y otros similares; todo este proceso e información se ha completado y documentado satisfactoriamente."
    elif evaluacion.pregunta7_3==0:
        reco44="No cuenta con una ESTRUCTURA ORGANIZACIONAL adecuada para la implementación; no ha considerado aspectos como organigrama, acta constitutiva, plan de negocios, cédula fiscal y otros similares."
    elif evaluacion.pregunta7_3<=13:
        reco44="No está seguro de contar con una ESTRUCTURA ORGANIZACIONAL adecuada para la implementación, sin embargo, es muy probable que no haya considerado aspectos como organigrama, acta constitutiva, plan de negocios, cédula fiscal y otros similares. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta7_3<=25:
        reco44="Ya cuenta con una ESTRUCTURA ORGANIZACIONAL adecuada para la implementación, sin embargo, es necesario documentar el proceso realizado; deben considerarse aspectos como organigrama, acta constitutiva, plan de negocios, cédula fiscal y otros similares. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta7_3<=50:
        reco44="Ya cuenta con una ESTRUCTURA ORGANIZACIONAL adecuada para la implementación, ha considerado aspectos organigrama, acta constitutiva, plan de negocios, cédula fiscal y otros similares, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."



    if evaluacion.pregunta8_3==100:
        reco45="Cuenta con una organización OPERATIVA AL 100%, realiza declaraciones fiscales, contratos, pago de nómina, pago de impuestos y otros similares; todo este proceso e información se ha completado y documentado satisfactoriamente."
    elif evaluacion.pregunta8_3==0:
        reco45="No cuenta con una organización OPERATIVA AL 100%, no realiza declaraciones fiscales, contratos, pago de nómina, pago de impuestos y otros similares."
    elif evaluacion.pregunta8_3<=13:
        reco45="No está seguro de contar con una organización OPERATIVA AL 100%, sin embargo, es muy probable que no realice declaraciones fiscales, contratos, pago de nómina, pago de impuestos y otros similares. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta8_3<=25:
        reco45="Ya cuenta con una organización OPERATIVA AL 100%, sin embargo, es necesario documentar el proceso realizado; debe realizar declaraciones fiscales, contratos, pago de nómina, pago de impuestos y otros similares. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta8_3<=50:
        reco45="Ya cuenta con una organización OPERATIVA AL 100%, es muy probable que realice declaraciones fiscales, contratos, pago de nómina, pago de impuestos u otros similares, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."



    if evaluacion.pregunta9_2==100:
        reco46="Cuenta con un producto con CRECIMIENTO DE MERCADO, realiza ventas sostenidas y producción a gran volumen, cuenta con reportes de venta y proyecciones de mercado; todo este proceso e información se ha completado y documentado satisfactoriamente."
    elif evaluacion.pregunta9_2==0:
        reco46="No cuenta con un producto con CRECIMIENTO DE MERCADO, no realiza ventas sostenidas y tampoco producción a gran volumen, no cuenta con reportes de venta ni proyecciones de mercado."
    elif evaluacion.pregunta9_2<=13:
        reco46="No está seguro de contar con un producto con CRECIMIENTO DE MERCADO, sin embargo, es muy probable que no realice ventas sostenidas ni producción a gran volumen, también es probable que no cuente con reportes de ventas y proyecciones de mercado. Revise cuidadosamente la información disponible y documentación realizada."
    elif evaluacion.pregunta9_2<=25:
        reco46="Ya cuenta con un producto con CRECIMIENTO DE MERCADO, sin embargo, es necesario documentar el proceso realizado; debe realizar ventas sostenidas y producción a gran volumen, además debe contar con reportes de venta y proyecciones de mercado. Asegurese de realizar correctamente la documentación respectiva."
    elif evaluacion.pegunta9_2<=50:
        reco46="Ya cuenta con un producto con CRECIMIENTO DE MERCADO, es muy probable que realice ventas sostenidas y producción a gran volumen, además de contar con reportes de venta y proyecciones de mercado, sin embargo, es necesario revisar cuidadosamente la información disponible y la documentación realizada durante el proceso."



        



    return render(request,'resultados.html', {'evaluacion':evaluacion, 'estatus':estatus})
