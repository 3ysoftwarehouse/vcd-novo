# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from djangosige.apps.cadastro.models.bancos import BANCOS

import locale
locale.setlocale(locale.LC_ALL, '')


FORMAS_PAG_ESCOLHAS = (
    (u'01', u'Dinheiro'),
    (u'02', u'Cheque'),
    (u'03', u'Cartão de Crédito'),
    (u'04', u'Cartão de Débito'),
    (u'05', u'Crédito Loja')
)

BANDEIRAS = (
    (u'01', u'AMEX'),
    (u'02', u'MASTERCARD'),
    (u'03', u'VISA'),
)

TIPO_CARTAO = (
    (u'01', u'CREDITO'),
    (u'02', u'DEBITO'),
)


class Pagamento(models.Model):
    venda_id = models.ForeignKey(
        'vendas.Venda', related_name="parcela_pagamento", on_delete=models.CASCADE)
    indice_parcela = models.IntegerField()
    forma = models.CharField(
        max_length=2, choices=FORMAS_PAG_ESCOLHAS, default='01')
    vencimento = models.DateField()
    valor_parcela = models.DecimalField(max_digits=13, decimal_places=2, validators=[
                                        MinValueValidator(Decimal('0.00'))])
    observacao = models.TextField(max_length=1000, null=True, blank=True)
    # moeda = models.ForeignKey('financeiro.Moeda', related_name="moeda", on_delete=models.SET_NULL, null=True,
    #                           blank=True)

    @property
    def format_valor_parcela(self):
        return locale.format(u'%.2f', self.valor_parcela, 1)

    @property
    def format_vencimento(self):
        return self.vencimento.strftime('%d/%m/%Y')

class Maquineta(models.Model):
    nome = models.CharField(max_length=20)
    taxa = models.DecimalField(max_digits=5, decimal_places=4, validators=[
        MinValueValidator(Decimal('0.00'))])


class Cheque(Pagamento):
    banco = models.CharField(
        max_length=3, choices=BANCOS, null=True, blank=True)
    agencia = models.CharField(max_length=8, null=True, blank=True)
    conta = models.CharField(max_length=32, null=True, blank=True)
    digito = models.CharField(max_length=8, null=True, blank=True)
    cpf_cnpj = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.venda_id

class Cartao(Pagamento):
    numero_cartao = models.CharField(max_length=16)
    bandeira = models.CharField(
        max_length=3, choices=BANDEIRAS)
    tipo = models.CharField(
        max_length=3, choices=TIPO_CARTAO)
    qtd_parcelas = models.IntegerField(default=1)
    codigo_autorizacao = models.CharField(max_length=3)
    validade = models.DateField()
    titular = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.venda_id


class CondicaoPagamento(models.Model):
    descricao = models.CharField(max_length=255)
    forma = models.CharField(
        max_length=2, choices=FORMAS_PAG_ESCOLHAS, default='01')
    n_parcelas = models.IntegerField()
    dias_recorrencia = models.IntegerField(default=0)
    parcela_inicial = models.IntegerField(default=0)  # Dias

    class Meta:
        verbose_name = "Condição de Pagamento"
        permissions = (
            ("view_condicaopagamento", "Can view condicao pagamento"),
        )

    def __unicode__(self):
        s = u'%s' % (self.descricao)
        return s

    def __str__(self):
        s = u'%s' % (self.descricao)
        return s
