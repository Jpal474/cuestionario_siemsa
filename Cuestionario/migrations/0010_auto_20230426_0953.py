# Generated by Django 3.2.7 on 2023-04-26 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cuestionario', '0009_evaluacion_institucion'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacion',
            name='pregunta6',
            field=models.FloatField(default=0, max_length=5),
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='pregunta7',
            field=models.FloatField(default=0, max_length=5),
        ),
    ]