# Generated by Django 4.2.1 on 2023-05-27 19:32

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlantasModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Nombre')),
                ('desciption', ckeditor.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': 'Clase de Planta',
                'verbose_name_plural': 'Clase de Plantas',
            },
        ),
        migrations.CreateModel(
            name='PlantaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Nombre')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, null=0, verbose_name='Precio')),
                ('plantas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.plantasmodels')),
            ],
            options={
                'verbose_name': 'Planta',
                'verbose_name_plural': 'Plantas',
            },
        ),
    ]
