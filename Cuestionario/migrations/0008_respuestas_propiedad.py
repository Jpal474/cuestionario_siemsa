# Generated by Django 3.2.7 on 2023-03-24 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cuestionario', '0007_evaluacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respuestas_Propiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proyecto', models.CharField(default='', max_length=500)),
                ('categoria_pregunta', models.CharField(max_length=70)),
                ('respuesta2_2', models.CharField(max_length=10)),
                ('evidencia2_2', models.CharField(max_length=10)),
                ('respuesta3_3', models.CharField(max_length=10)),
                ('evidencia3_3', models.CharField(max_length=10)),
                ('respuesta4_7', models.CharField(max_length=10)),
                ('evidencia4_7', models.CharField(max_length=10)),
                ('respuesta5_4', models.CharField(max_length=10)),
                ('evidencia5_4', models.CharField(max_length=10)),
                ('respuesta3_4', models.CharField(max_length=10)),
                ('evidencia3_4', models.CharField(max_length=10)),
                ('respuesta2_6', models.CharField(max_length=10)),
                ('evidencia2_6', models.CharField(max_length=10)),
                ('respuesta3_6', models.CharField(max_length=10)),
                ('evidencia3_6', models.CharField(max_length=10)),
                ('respuesta4_8', models.CharField(max_length=10)),
                ('evidencia4_8', models.CharField(max_length=10)),
                ('respuesta6', models.CharField(max_length=10)),
                ('evidencia6', models.CharField(max_length=10)),
                ('respuesta7', models.CharField(max_length=10)),
                ('evidencia7', models.CharField(max_length=10)),
            ],
        ),
    ]