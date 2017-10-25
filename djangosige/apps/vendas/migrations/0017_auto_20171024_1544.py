# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 17:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0016_auto_20171024_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contatoprospect',
            name='prospect',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prospect', to='vendas.Prospect'),
        ),
    ]