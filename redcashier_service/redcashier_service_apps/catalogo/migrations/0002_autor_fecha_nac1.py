# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='fecha_nac1',
            field=models.DateField(blank=True, null=True),
        ),
    ]
