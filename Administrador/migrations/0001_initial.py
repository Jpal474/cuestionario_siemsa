# Generated by Django 3.2.7 on 2023-03-14 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('categoria_pregunta', models.CharField(max_length=70)),
                ('numero_res', models.IntegerField(max_length=1)),
            ],
        ),
    ]