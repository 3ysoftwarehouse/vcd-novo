# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_produto_day_by_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='codigo',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
