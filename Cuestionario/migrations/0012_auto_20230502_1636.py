# Generated by Django 3.2.7 on 2023-05-02 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cuestionario', '0011_evaluacion_pregunta6_0'),
    ]

    operations = [
        migrations.RenameField(
            model_name='respuestas_propiedad',
            old_name='evidencia6',
            new_name='evidencia6_0',
        ),
        migrations.RenameField(
            model_name='respuestas_propiedad',
            old_name='respuesta6',
            new_name='respuesta6_0',
        ),
    ]
