# -*- coding: utf-8 -*-

from django.db import models

from decimal import Decimal

from .base import Pessoa

INDICADOR_IE_DEST = [
    ('1', 'Contribuinte ICMS'),
    ('2', 'Contribuinte isento de Inscrição'),
    ('9', 'Não Contribuinte'),
]


class Cliente(Pessoa):
    limite_de_credito = models.DecimalField(
    max_digits=15, decimal_places=2, default=Decimal('0.00'), null=True, blank=True)
    indicador_ie = models.CharField(
    max_length=1, choices=INDICADOR_IE_DEST, default='9')
    id_estrangeiro = models.CharField(max_length=20, null=True, blank=True)

    nome_pai = models.CharField(max_length=45,null=True, blank=True)
    nome_mae = models.CharField(max_length=45,null=True, blank=True)
    naturalidade = models.CharField(max_length=45,null=True, blank=True)
    numero_dependentes = models.IntegerField(default=0)
    tipo_residencia = models.CharField(max_length=20,null=True, blank=True)
    dt_emissao_rg = models.DateField(null=True, blank=True)
    tempo_residencia = models.CharField(max_length=20,null=True, blank=True)
    dt_admissao = models.DateTimeField(null=True, blank=True)
    cargo = models.CharField(max_length=20,null=True, blank=True)
    principal_renda = models.CharField(max_length=20,null=True, blank=True)
    outra_renda = models.CharField(max_length=20,null=True, blank=True)
    patrimonio = models.CharField(max_length=20,null=True, blank=True)
    emissor = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, null=True, blank=True)
    
    class Meta:
        verbose_name = "Cliente"
        permissions = (
            ("view_cliente", "Can view cliente"),
        )