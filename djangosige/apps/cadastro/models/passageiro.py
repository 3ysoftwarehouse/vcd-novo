# -*- coding: utf-8 -*-

from django.db import models

from decimal import Decimal

from .base import Pessoa

from djangosige.apps.cadastro.models.escola import Escola


INDICADOR_IE_DEST = [
    ('1', 'Contribuinte ICMS'),
    ('2', 'Contribuinte isento de Inscrição'),
    ('9', 'Não Contribuinte'),
]


class Passageiro(Pessoa):
    escola_passageiro = models.ForeignKey(Escola, related_name="escola_passageiro", on_delete=models.CASCADE, null=True, blank=True)
    nome_pai = models.CharField(max_length=500, null=True, blank=True)
    nome_mae = models.CharField(max_length=500, null=True, blank=True)
    matricula = models.IntegerField(null=True, blank=True)
    responsavel = models.CharField(max_length=500, null=True, blank=True)
    telefone_responsavel = models.CharField(max_length=12, null=True, blank=True)
    natularidade = models.CharField(max_length=30,null=True, blank=True)
    observacao = models.CharField(max_length=250,null=True, blank=True)
    emissor = models.ForeignKey('auth.User', null=True, blank=True)
    numero_passaporte = models.CharField(max_length=10,null=True, blank=True)
    data_validade_passaporte = models.DateField(null=True, blank=True)
    limite_de_credito = models.DecimalField(
        max_digits=15, decimal_places=2, default=Decimal('0.00'), null=True, blank=True)
    indicador_ie = models.CharField(
        max_length=1, choices=INDICADOR_IE_DEST, default='9')
    id_estrangeiro = models.CharField(max_length=20, null=True, blank=True)


    class Meta:
        verbose_name = "Passageiro"
        permissions = (
            ("view_passageiro", "Can view passageiro"),
        )
