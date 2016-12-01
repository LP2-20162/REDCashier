# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 01:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('fecha_nac', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'permissions': (('list_autor', 'Can list autor'), ('get_autor', 'Can get autor')),
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('codigo', models.CharField(blank=True, max_length=15, null=True)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'permissions': (('list_categoria', 'Can list categoria'), ('get_categoria', 'Can get categoria')),
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Ejemplar',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'permissions': (('list_ejemplar', 'Can list ejemplar'), ('get_ejemplar', 'Can get ejemplar')),
                'verbose_name': 'Ejemplar',
                'verbose_name_plural': 'Ejemplares',
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('FISICO', 'Fisico'), ('VIRTUAL', 'Virtual'), ('FIS_VIR', 'FisicoVirtual')], default='FISICO', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('autors', models.ManyToManyField(blank=True, to='catalogo.Autor')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Categoria')),
            ],
            options={
                'permissions': (('list_libro', 'Can list libro'), ('get_libro', 'Can get libro')),
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
        migrations.AddField(
            model_name='ejemplar',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Libro'),
        ),
    ]
