# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0011_auto_20171023_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contatoprospect',
            name='observacao',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]