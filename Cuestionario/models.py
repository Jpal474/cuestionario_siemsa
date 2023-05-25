from statistics import mode
from django.db import models

# Create your models here.
class Registro(models.Model):
    nombre=models.CharField(max_length=300)
    nombre_proyecto=models.CharField(max_length=500)
    correo_electronico=models.CharField(max_length=255)
    institucion=models.CharField(max_length=255)
    categoria=models.TextField(null=False)
    fecha=models.DateTimeField(null=False)

class Respuestas_Investigacion(models.Model):
    nombre_proyecto=models.CharField(max_length=500, default="", null=False)
    categoria_pregunta=models.CharField(max_length=70)
    respuesta1_1=models.CharField(max_length=10)
    evidencia1_1=models.CharField(max_length=10)
    respuesta1_2=models.CharField(max_length=10)
    evidencia1_2=models.CharField(max_length=10)
    respuesta2_1=models.CharField(max_length=10)
    evidencia2_1=models.CharField(max_length=10)

class Respuestas_Desarrollo(models.Model):
    nombre_proyecto=models.CharField(max_length=500, default="", null=False)
    categoria_pregunta=models.CharField(max_length=70)
    respuesta4_2=models.CharField(max_length=10)
    evidencia4_2=models.CharField(max_length=10)
    respuesta4_5=models.CharField(max_length=10)
    evidencia4_5=models.CharField(max_length=10)
    respuesta4_6=models.CharField(max_length=10)
    evidencia4_6=models.CharField(max_length=10)
    respuesta5_1=models.CharField(max_length=10)
    evidencia5_1=models.CharField(max_length=10)
    respuesta6=models.CharField(max_length=10)
    evidencia6=models.CharField(max_length=10)
    respuesta7_4=models.CharField(max_length=10)
    evidencia7_4=models.CharField(max_length=10)
    respuesta8_2=models.CharField(max_length=10)
    evidencia8_2=models.CharField(max_length=10)
    respuesta9_1=models.CharField(max_length=10)
    evidencia9_1=models.CharField(max_length=10)
    respuesta9_3=models.CharField(max_length=10)
    evidencia9_3=models.CharField(max_length=10)


class Respuestas_Integracion(models.Model):
    nombre_proyecto=models.CharField(max_length=500, default="", null=False)
    categoria_pregunta=models.CharField(max_length=70)
    respuesta2_5=models.CharField(max_length=10)
    evidencia2_5=models.CharField(max_length=10)
    respuesta3_1=models.CharField(max_length=10)
    evidencia3_1=models.CharField(max_length=10)
    respuesta4_1=models.CharField(max_length=10)
    evidencia4_1=models.CharField(max_length=10)
    respuesta6_2=models.CharField(max_length=10)
    evidencia6_2=models.CharField(max_length=10)


class Respuestas_Propiedad(models.Model):
    nombre_proyecto=models.CharField(max_length=500, default="", null=False)
    categoria_pregunta=models.CharField(max_length=70)
    respuesta2_2=models.CharField(max_length=10)
    evidencia2_2=models.CharField(max_length=10)
    respuesta3_3=models.CharField(max_length=10)
    evidencia3_3=models.CharField(max_length=10)
    respuesta4_7=models.CharField(max_length=10)
    evidencia4_7=models.CharField(max_length=10)
    respuesta5_4=models.CharField(max_length=10)
    evidencia5_4=models.CharField(max_length=10)
    respuesta3_4=models.CharField(max_length=10)
    evidencia3_4=models.CharField(max_length=10)
    respuesta2_6=models.CharField(max_length=10)
    evidencia2_6=models.CharField(max_length=10)
    respuesta3_6=models.CharField(max_length=10)
    evidencia3_6=models.CharField(max_length=10)
    respuesta4_8=models.CharField(max_length=10)
    evidencia4_8=models.CharField(max_length=10)
    respuesta6_0=models.CharField(max_length=10)
    evidencia6_0=models.CharField(max_length=10)
    respuesta7=models.CharField(max_length=10)
    evidencia7=models.CharField(max_length=10)
    

class Respuestas_Normatividad(models.Model):
    nombre_proyecto=models.CharField(max_length=500, default="", null=False)
    categoria_pregunta=models.CharField(max_length=70)
    respuesta3_5=models.CharField(max_length=10)
    evidencia3_5=models.CharField(max_length=10)
    respuesta5_3=models.CharField(max_length=10)
    evidencia5_3=models.CharField(max_length=10)
    respuesta6_5=models.CharField(max_length=10)
    evidencia6_5=models.CharField(max_length=10)
    respuesta8_4=models.CharField(max_length=10)
    evidencia8_4=models.CharField(max_length=10)


class Respuestas_Manufactura(models.Model):
    nombre_proyecto=models.CharField(max_length=500, default="", null=False)
    categoria_pregunta=models.CharField(max_length=70)
    respuesta2_3=models.CharField(max_length=10)
    evidencia2_3=models.CharField(max_length=10)
    respuesta4_3=models.CharField(max_length=10)
    evidencia4_3=models.CharField(max_length=10)
    respuesta5_2=models.CharField(max_length=10)
    evidencia5_2=models.CharField(max_length=10)
    respuesta6_1=models.CharField(max_length=10)
    evidencia6_1=models.CharField(max_length=10)
    respuesta7_1=models.CharField(max_length=10)
    evidencia7_1=models.CharField(max_length=10)
    respuesta8_1=models.CharField(max_length=10)
    evidencia8_1=models.CharField(max_length=10)
    respuesta9_4=models.CharField(max_length=10)
    evidencia9_4=models.CharField(max_length=10)  


class Respuestas_Usuarios(models.Model):
    nombre_proyecto=models.CharField(max_length=500, default="", null=False)
    categoria_pregunta=models.CharField(max_length=70)
    respuesta2_4=models.CharField(max_length=10)
    evidencia2_4=models.CharField(max_length=10)
    respuesta3_2=models.CharField(max_length=10)
    evidencia3_2=models.CharField(max_length=10)
    respuesta4_4=models.CharField(max_length=10)
    evidencia4_4=models.CharField(max_length=10)
    respuesta6_3=models.CharField(max_length=10)
    evidencia6_3=models.CharField(max_length=10)
    respuesta7_2=models.CharField(max_length=10)
    evidencia7_2=models.CharField(max_length=10)
    respuesta8_5=models.CharField(max_length=10)
    evidencia8_5=models.CharField(max_length=10) 


class Respuestas_Aspectos(models.Model):
    nombre_proyecto=models.CharField(max_length=500, default="", null=False)
    categoria_pregunta=models.CharField(max_length=70)
    respuesta6_4=models.CharField(max_length=10)
    evidencia6_4=models.CharField(max_length=10)
    respuesta7_3=models.CharField(max_length=10)
    evidencia7_3=models.CharField(max_length=10)
    respuesta8_3=models.CharField(max_length=10)
    evidencia8_3=models.CharField(max_length=10)
    respuesta9_2=models.CharField(max_length=10)
    evidencia9_2=models.CharField(max_length=10)
    
class Evaluacion(models.Model):
    nombre=models.CharField(max_length=300)
    nombre_proyecto=models.CharField(max_length=500)
    institucion=models.CharField(max_length=500, default='')
    pregunta1_1=models.FloatField(max_length=5, default=0)
    pregunta1_2=models.FloatField(max_length=5, default=0)
    promedio_trl1=models.FloatField(max_length=5, default=0)
    pregunta2_1=models.FloatField(max_length=5, default=0)
    pregunta2_2=models.FloatField(max_length=5, default=0)
    pregunta2_3=models.FloatField(max_length=5, default=0)
    pregunta2_4=models.FloatField(max_length=5, default=0)
    pregunta2_5=models.FloatField(max_length=5, default=0)
    pregunta2_6=models.FloatField(max_length=5, default=0)
    promedio_trl2=models.FloatField(max_length=5, default=0)
    pregunta3_1=models.FloatField(max_length=5, default=0)
    pregunta3_2=models.FloatField(max_length=5, default=0)
    pregunta3_3=models.FloatField(max_length=5, default=0)
    pregunta3_4=models.FloatField(max_length=5, default=0)
    pregunta3_5=models.FloatField(max_length=5, default=0)
    pregunta3_6=models.FloatField(max_length=5, default=0)
    promedio_trl3=models.FloatField(max_length=5, default=0)
    pregunta4_1=models.FloatField(max_length=5, default=0)
    pregunta4_2=models.FloatField(max_length=5, default=0)
    pregunta4_3=models.FloatField(max_length=5, default=0)
    pregunta4_4=models.FloatField(max_length=5, default=0)
    pregunta4_5=models.FloatField(max_length=5, default=0)
    pregunta4_6=models.FloatField(max_length=5, default=0)
    pregunta4_7=models.FloatField(max_length=5, default=0)
    pregunta4_8=models.FloatField(max_length=5, default=0)
    promedio_trl4=models.FloatField(max_length=5, default=0)
    pregunta5_1=models.FloatField(max_length=5, default=0)
    pregunta5_2=models.FloatField(max_length=5, default=0)
    pregunta5_3=models.FloatField(max_length=5, default=0)
    pregunta5_4=models.FloatField(max_length=5, default=0)
    promedio_trl5=models.FloatField(max_length=5, default=0)
    pregunta6_0=models.FloatField(max_length=5, default=0)
    pregunta6=models.FloatField(max_length=5, default=0)
    pregunta6_1=models.FloatField(max_length=5, default=0)
    pregunta6_2=models.FloatField(max_length=5, default=0)
    pregunta6_3=models.FloatField(max_length=5, default=0)
    pregunta6_4=models.FloatField(max_length=5, default=0)
    pregunta6_5=models.FloatField(max_length=5, default=0)
    promedio_trl6=models.FloatField(max_length=5, default=0)
    pregunta7=models.FloatField(max_length=5, default=0)
    pregunta7_1=models.FloatField(max_length=5, default=0)
    pregunta7_2=models.FloatField(max_length=5, default=0)
    pregunta7_3=models.FloatField(max_length=5, default=0)
    pregunta7_4=models.FloatField(max_length=5, default=0)
    promedio_trl7=models.FloatField(max_length=5, default=0)
    pregunta8_1=models.FloatField(max_length=5, default=0)
    pregunta8_2=models.FloatField(max_length=5, default=0)
    pregunta8_3=models.FloatField(max_length=5, default=0)
    pregunta8_4=models.FloatField(max_length=5, default=0)
    pregunta8_5=models.FloatField(max_length=5, default=0)
    promedio_trl8=models.FloatField(max_length=5, default=0)
    pregunta9_1=models.FloatField(max_length=5, default=0)
    pregunta9_2=models.FloatField(max_length=5, default=0)
    pregunta9_3=models.FloatField(max_length=5, default=0)
    pregunta9_4=models.FloatField(max_length=5, default=0)
    promedio_trl9=models.FloatField(max_length=5, default=0)
    promedio_trl_global=models.FloatField(max_length=5)
    promedio_investigacion=models.FloatField(max_length=5)
    promedio_desarrollo=models.FloatField(max_length=5)
    promedio_integracion=models.FloatField(max_length=5)
    promedio_propiedad=models.FloatField(max_length=5)
    promedio_normatividad=models.FloatField(max_length=5)
    promedio_manufactura=models.FloatField(max_length=5)
    promedio_usuarios=models.FloatField(max_length=5)
    promedio_aspectos=models.FloatField(max_length=5)    

    

class Estatus(models.Model):
    nombre_proyecto=models.CharField(max_length=500)
    estatus=models.TextField(null=False)

class Conclusiones(models.Model):
    nombre_proyecto=models.CharField(max_length=500)
    conclusion_investigacion=models.TextField(null=False)
    conclusion_desarrollo=models.TextField(null=False)
    conclusion_integracion=models.TextField(null=False)
    conclusion_propiedad=models.TextField(null=False)
    conclusion_normatividad=models.TextField(null=False)
    conclusion_manufactura=models.TextField(null=False)
    conclusion_usuarios=models.TextField(null=False)
    conclusion_aspectos=models.TextField(null=False)

class Recomendaciones(models.Model):
    nombre_proyecto=models.CharField(max_length=500)
    recomendacion_investigacion=models.TextField(null=False, default="")
    recomendacion_desarrollo=models.TextField(null=False, default="")
    recomendacion_integracion=models.TextField(null=False, default="")
    recomendacion_propiedad=models.TextField(null=False, default="")
    recomendacion_normatividad=models.TextField(null=False, default="")
    recomendacion_manufactura=models.TextField(null=False, default="")
    recomendacion_usuarios=models.TextField(null=False, default="")
    recomendacion_aspectos=models.TextField(null=False, default="")
    recomendacion_pregunta1_1=models.TextField(null=False, default="")
    recomendacion_pregunta1_2=models.TextField(null=False, default="")   
    recomendacion_pregunta2_1=models.TextField(null=False, default="")
    recomendacion_pregunta2_2=models.TextField(null=False, default="")
    recomendacion_pregunta2_3=models.TextField(null=False, default="")
    recomendacion_pregunta2_4=models.TextField(null=False, default="")
    recomendacion_pregunta2_5=models.TextField(null=False, default="")
    recomendacion_pregunta2_6=models.TextField(null=False, default="")
    recomendacion_pregunta3_1=models.TextField(null=False, default="")
    recomendacion_pregunta3_2=models.TextField(null=False, default="")
    recomendacion_pregunta3_3=models.TextField(null=False, default="")
    recomendacion_pregunta3_4=models.TextField(null=False, default="")
    recomendacion_pregunta3_5=models.TextField(null=False, default="")
    recomendacion_pregunta3_6=models.TextField(null=False, default="")
    recomendacion_pregunta4_1=models.TextField(null=False, default="")
    recomendacion_pregunta4_2=models.TextField(null=False, default="")
    recomendacion_pregunta4_3=models.TextField(null=False, default="")
    recomendacion_pregunta4_4=models.TextField(null=False, default="")
    recomendacion_pregunta4_5=models.TextField(null=False, default="")
    recomendacion_pregunta4_6=models.TextField(null=False, default="")
    recomendacion_pregunta4_7=models.TextField(null=False, default="")
    recomendacion_pregunta4_8=models.TextField(null=False, default="") 
    recomendacion_pregunta5_1=models.TextField(null=False, default="")
    recomendacion_pregunta5_2=models.TextField(null=False, default="")
    recomendacion_pregunta5_3=models.TextField(null=False, default="")
    recomendacion_pregunta5_4=models.TextField(null=False, default="")   
    recomendacion_pregunta6_0=models.TextField(null=False, default="")
    recomendacion_pregunta6=models.TextField(null=False, default="")
    recomendacion_pregunta6_1=models.TextField(null=False, default="")
    recomendacion_pregunta6_2=models.TextField(null=False, default="")
    recomendacion_pregunta6_3=models.TextField(null=False, default="")
    recomendacion_pregunta6_4=models.TextField(null=False, default="")
    recomendacion_pregunta6_5=models.TextField(null=False, default="")  
    recomendacion_pregunta7=models.TextField(null=False, default="")
    recomendacion_pregunta7_1=models.TextField(null=False, default="")
    recomendacion_pregunta7_2=models.TextField(null=False, default="")
    recomendacion_pregunta7_3=models.TextField(null=False, default="")
    recomendacion_pregunta7_4=models.TextField(null=False, default="")  
    recomendacion_pregunta8_1=models.TextField(null=False, default="")
    recomendacion_pregunta8_2=models.TextField(null=False, default="")
    recomendacion_pregunta8_3=models.TextField(null=False, default="")
    recomendacion_pregunta8_4=models.TextField(null=False, default="")
    recomendacion_pregunta8_5=models.TextField(null=False, default="")
    recomendacion_pregunta9_1=models.TextField(null=False, default="")
    recomendacion_pregunta9_2=models.TextField(null=False, default="")
    recomendacion_pregunta9_3=models.TextField(null=False, default="")
    recomendacion_pregunta9_4=models.TextField(null=False, default="")
