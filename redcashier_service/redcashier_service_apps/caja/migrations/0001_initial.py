# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-04 18:13
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodoContable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('codigo', models.CharField(blank=True, max_length=15, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('fechInicio', models.DateField(blank=True, null=True)),
                ('fechFin', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'PeriodoContables',
                'permissions': (('list_periodoContable', 'Can list periodoContable'), ('get_periodoContable', 'Can get periodoContable')),
                'verbose_name': 'PeriodoContable',
            },
        ),
    ]
