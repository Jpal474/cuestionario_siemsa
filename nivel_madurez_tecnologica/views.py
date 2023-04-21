from asyncio.windows_events import proactor_events
from datetime import datetime
from pydoc import describe
from django.shortcuts import redirect, render
from Cuestionario.models import *
from weasyprint.css.computed_values import content
from django.template.loader import get_template
from weasyprint import HTML

def inicio(request):
    return render (request, 'inicio.html')

def guardar_registro(request):
    global fecha
    global nombre_proyecto
    global institucion
    registro=Registro()
    registro.nombre=request.POST.get('nombre')
    nombre_proyecto=registro.nombre_proyecto=request.POST.get('nombre_proyecto')
    registro.correo_electronico=request.POST.get('correo')
    institucion=registro.institucion=request.POST.get('institucion')
    registro.categoria=request.POST.get('categoria')
    fecha=registro.fecha=datetime.now()
    registro.save()
    return redirect ('investigacion')

def investigación(request):
    return render(request, 'investigacion.html')

def guardar_investigacion(request):
    nombre=Registro.objects.filter(nombre_proyecto=nombre_proyecto, fecha=fecha).values('nombre')
   # inst=Registro.objects.filter(institucion=institucion, fecha=fecha).values('institucion')
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
    evaluacion.institucion=institucion
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
    evaluacion.promedio_trl_global=round(global_trl,2)
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
        if promedio==100:
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
    iconos={
     
    }
    colores={}
    print(eval.promedio_investigacion)
    cont=0
    cont2=0
    icons=[None]*44
    icons[0]=eval.pregunta1_1
    icons[1]=eval.pregunta1_2
    icons[2]=eval.pregunta2_1 
    icons[3]=eval.pregunta2_2 
    icons[4]=eval.pregunta2_3 
    icons[5]=eval.pregunta2_4
    icons[6]=eval.pregunta2_5
    icons[7]=eval.pregunta2_6
    icons[8]=eval.pregunta3_1
    icons[9]=eval.pregunta3_2
    icons[10]=eval.pregunta3_3
    icons[11]=eval.pregunta3_4
    icons[12]=eval.pregunta3_5 
    icons[13]=eval.pregunta3_6
    icons[14]=eval.pregunta4_1
    icons[15]=eval.pregunta4_2
    icons[16]=eval.pregunta4_3
    icons[17]=eval.pregunta4_4 
    icons[18]=eval.pregunta4_5
    icons[20]=eval.pregunta4_6
    icons[19]=eval.pregunta4_7
    icons[21]=eval.pregunta4_8
    icons[22]=eval.pregunta5_1  
    icons[23]=eval.pregunta5_2 
    icons[24]=eval.pregunta5_3
    icons[25]=eval.pregunta5_4
    icons[26]=eval.pregunta6_1 
    icons[27]=eval.pregunta6_2
    icons[28]=eval.pregunta6_3 
    icons[29]=eval.pregunta6_4 
    icons[30]=eval.pregunta6_5
    icons[31]=eval.pregunta7_1 
    icons[32]=eval.pregunta7_2
    icons[33]=eval.pregunta7_3
    icons[34]=eval.pregunta7_4
    icons[35]=eval.pregunta8_1
    icons[36]=eval.pregunta8_2
    icons[37]=eval.pregunta8_3
    icons[38]=eval.pregunta8_4
    icons[39]=eval.pregunta8_5
    icons[40]=eval.pregunta9_1
    icons[41]=eval.pregunta9_2
    icons[42]=eval.pregunta9_3  
    icons[43]=eval.pregunta9_4

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
   
    return render(request,'resultados.html', {'evaluacion':evaluacion, 'estatus':estatus, 'iconos':iconos, 'colores':colores})

def prueba(request):
    eval=Evaluacion.objects.get(id=11)
    iconos={
     
    }
    colores={}
    print(eval.promedio_investigacion)
    cont=0
    cont2=0
    icons=[None]*44
    icons[0]=eval.pregunta1_1
    icons[1]=eval.pregunta1_2
    icons[2]=eval.pregunta2_1 
    icons[3]=eval.pregunta2_2 
    icons[4]=eval.pregunta2_3 
    icons[5]=eval.pregunta2_4
    icons[6]=eval.pregunta2_5
    icons[7]=eval.pregunta2_6
    icons[8]=eval.pregunta3_1
    icons[9]=eval.pregunta3_2
    icons[10]=eval.pregunta3_3
    icons[11]=eval.pregunta3_4
    icons[12]=eval.pregunta3_5 
    icons[13]=eval.pregunta3_6
    icons[14]=eval.pregunta4_1
    icons[15]=eval.pregunta4_2
    icons[16]=eval.pregunta4_3
    icons[17]=eval.pregunta4_4 
    icons[18]=eval.pregunta4_5
    icons[20]=eval.pregunta4_6
    icons[19]=eval.pregunta4_7
    icons[21]=eval.pregunta4_8
    icons[22]=eval.pregunta5_1  
    icons[23]=eval.pregunta5_2 
    icons[24]=eval.pregunta5_3
    icons[25]=eval.pregunta5_4
    icons[26]=eval.pregunta6_1 
    icons[27]=eval.pregunta6_2
    icons[28]=eval.pregunta6_3 
    icons[29]=eval.pregunta6_4 
    icons[30]=eval.pregunta6_5
    icons[31]=eval.pregunta7_1 
    icons[32]=eval.pregunta7_2
    icons[33]=eval.pregunta7_3
    icons[34]=eval.pregunta7_4
    icons[35]=eval.pregunta8_1
    icons[36]=eval.pregunta8_2
    icons[37]=eval.pregunta8_3
    icons[38]=eval.pregunta8_4
    icons[39]=eval.pregunta8_5
    icons[40]=eval.pregunta9_1
    icons[41]=eval.pregunta9_2
    icons[42]=eval.pregunta9_3  
    icons[43]=eval.pregunta9_4

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
   

    
    '''for e in eval:
        if cont > 2 and cont<5:
            if e == 0:
                iconos={cont2:"close-outline",}
                cont2+=1
            elif e==12.5:
                iconos={cont2:"notifications-outline",}
                cont2+=1 
            elif e==25:
                iconos={cont2:"alert-outline",}
                cont2+=1
            elif e==50:
                iconos={cont2:"warning-outline",}
                cont2+=1 
            else:
                iconos={cont2:"checkmark-outline",}
                cont2+=1 
           
        elif cont>5 and cont<12:

            if e == 0:
                iconos={cont2:"close-outline",}
                cont2+=1
            elif e==12.5:
                iconos={cont2:"notifications-outline",}
                cont2+=1 
            elif e==25:
                iconos={cont2:"alert-outline",}
                cont2+=1
            elif e==50:
                iconos={cont2:"warning-outline",}
                cont2+=1 
            else:
                iconos={cont2:"checkmark-outline",}
                cont2+=1 
        
        elif cont>12 and cont <19:
            if e == 0:
                iconos={cont2:"close-outline",}
                cont2+=1
            elif e==12.5:
                iconos={cont2:"notifications-outline",}
                cont2+=1 
            elif e==25:
                iconos={cont2:"alert-outline",}
                cont2+=1
            elif e==50:
                iconos={cont2:"warning-outline",}
                cont2+=1 
            else:
                iconos={cont2:"checkmark-outline",}
                cont2+=1 
        elif cont>19  and cont<33:
            if e == 0:
                iconos={cont2:"close-outline",}
                cont2+=1
            elif e==12.5:
                iconos={cont2:"notifications-outline",}
                cont2+=1 
            elif e==25:
                iconos={cont2:"alert-outline",}
                cont2+=1
            elif e==50:
                iconos={cont2:"warning-outline",}
                cont2+=1 
            else:
                iconos={cont2:"checkmark-outline",}
                cont2+=1 
        elif cont>33 and cont<39:
            if e == 0:
                iconos={cont2:"close-outline",}
                cont2+=1
            elif e==12.5:
                iconos={cont2:"notifications-outline",}
                cont2+=1 
            elif e==25:
                iconos={cont2:"alert-outline",}
                cont2+=1
            elif e==50:
                iconos={cont2:"warning-outline",}
                cont2+=1 
            else:
                iconos={cont2:"checkmark-outline",}
                cont2+=1 
        elif cont>39 and cont<44:
            if e == 0:
                iconos={cont2:"close-outline",}
                cont2+=1
            elif e==12.5:
                iconos={cont2:"notifications-outline",}
                cont2+=1 
            elif e==25:
                iconos={cont2:"alert-outline",}
                cont2+=1
            elif e==50:
                iconos={cont2:"warning-outline",}
                cont2+=1 
            else:
                iconos={cont2:"checkmark-outline",}
                cont2+=1 
        
        elif cont>44 and cont<49:
            if e == 0:
                iconos={cont2:"close-outline",}
                cont2+=1
            elif e==12.5:
                iconos={cont2:"notifications-outline",}
                cont2+=1 
            elif e==25:
                iconos={cont2:"alert-outline",}
                cont2+=1
            elif e==50:
                iconos={cont2:"warning-outline",}
                cont2+=1 
            else:
                iconos={cont2:"checkmark-outline",}
                cont2+=1 
        
        cont+=1'''

   
  
  
    return render(request, 'prueba.html', {'evaluacion':eval, 'iconos':iconos, 'colores':colores})


'''def export(request):
    template=get_template('pdf.html')
    html_template = template.render({"reservaciones":reserv, "ot":ot})
    pdf= HTML (string=html_template, base_url=request.build_absolute_uri()).write_pdf()
    return HttpResponse(pdf, content_type='application/pdf')'''
