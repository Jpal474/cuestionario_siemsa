# Generated by Django 3.2.7 on 2023-03-30 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cuestionario', '0008_respuestas_propiedad'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacion',
            name='institucion',
            field=models.CharField(default='', max_length=500),
        ),
    ]
