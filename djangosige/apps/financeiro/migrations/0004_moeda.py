# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0003_auto_20170820_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moeda',
            fields=[
                ('id_moeda', models.AutoField(primary_key=True, serialize=False)),
                ('moeda_desc', models.CharField(max_length=15, unique=True)),
                ('moeda_cambio', models.DecimalField(decimal_places=3, max_digits=4)),
                ('moeda_ultimaatualizacao', models.DateTimeField(auto_now_add=True)),
                ('moeda_simbolo', models.CharField(max_length=4)),
            ],
        ),
    ]