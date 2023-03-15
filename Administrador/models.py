from django.db import models

# Create your models here.
class Pregunta(models.Model):
    texto=models.TextField(null=False)
    categoria_pregunta=models.CharField(max_length=70)
    numero_res=models.IntegerField()