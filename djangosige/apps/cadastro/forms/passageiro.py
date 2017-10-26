# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

from djangosige.apps.cadastro.models.passageiro import Passageiro


class PassageiroForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PassageiroForm, self).__init__(*args, **kwargs)
        self.fields['limite_de_credito'].localize = True

    class Meta:
        model = Passageiro
        fields = ('nome_razao_social', 'tipo_pessoa', 'inscricao_municipal',
                  'limite_de_credito', 'indicador_ie', 'id_estrangeiro', 'informacoes_adicionais', 'escola_passageiro',
                  'matricula', 'nome_pai', 'nome_mae', 'responsavel', 'telefone_responsavel' ,'natularidade',
                  'observacao', 'emissor', 'numero_passaporte', 'data_validade_passaporte')
        widgets = {
            'nome_razao_social': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_pessoa': forms.RadioSelect(attrs={'class': 'form-control'}),
            'escola_passageiro': forms.Select(attrs={'class': 'form-control'}),
            'limite_de_credito': forms.TextInput(attrs={'class': 'form-control decimal-mask'}),
            'indicador_ie': forms.Select(attrs={'class': 'form-control'}),
            'inscricao_municipal': forms.TextInput(attrs={'class': 'form-control'}),
            'id_estrangeiro': forms.TextInput(attrs={'class': 'form-control'}),
            'informacoes_adicionais': forms.Textarea(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_pai': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control'}),
            'responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone_responsavel': forms.TextInput(attrs={'class': 'form-control telefone'}),
            'natularidade': forms.TextInput(attrs={'class': 'form-control'}),
            'observacao': forms.TextInput(attrs={'class': 'form-control'}),
            'emissor': forms.Select(attrs={'class': 'form-control'}),
            'numero_passaporte': forms.TextInput(attrs={'class': 'form-control'}),
            'data_validade_passaporte': forms.TextInput(attrs={'class': 'form-control datepicker'}),
        }
        labels = {
            'nome_razao_social': _('Nome / Razão Social'),
            'tipo_pessoa': _(''),
            'escola_passageiro': _('Escola'),
            'limite_de_credito': _('Limite de Crédito'),
            'indicador_ie': _('Indicador da IE do Destinatário'),
            'inscricao_municipal': _('Inscrição Municipal'),
            'id_estrangeiro': _('Documento legal (Estrangeiro)'),
            'informacoes_adicionais': _('Informações Adicionais'),
            'matricula': _('Matricula'),
            'nome_pai': _('Nome do Pai'),
            'nome_mae': _('Nome da Mãe'),
            'responsavel': _('Responsavel'),
            'telefone_responsavel': _('Telefone do Responsavel'),
            'natularidade': _('Naturalidade'),
            'observacao': _('Observação'),
            'emissor': _('Emissor'),
            'numero_passaporte': _('Número de Passporte'),
            'data_validade_passaporte': _('Data de Validade do Passaporte'),
        }

    def save(self, commit=True):
        instance = super(PassageiroForm, self).save(commit=False)
        instance.criado_por = self.request.user
        instance.emissor = self.request.user
        if commit:
            instance.save()
        return instance
