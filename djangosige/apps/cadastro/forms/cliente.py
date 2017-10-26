# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

from djangosige.apps.cadastro.models import Cliente


class ClienteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['limite_de_credito'].localize = True

    class Meta:
        model = Cliente
        fields = ('nome_razao_social', 'tipo_pessoa', 'inscricao_municipal',
                  'limite_de_credito', 'indicador_ie', 'id_estrangeiro', 'informacoes_adicionais', 
                  'nome_pai', 'nome_mae', 'naturalidade', 'numero_dependentes',
                  'tipo_residencia', 'dt_emissao_rg', 'tempo_residencia',
                  'dt_admissao', 'cargo', 'principal_renda',
                  'outra_renda', 'patrimonio')
        widgets = {
            'nome_razao_social': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_pessoa': forms.RadioSelect(attrs={'class': 'form-control'}),
            'limite_de_credito': forms.TextInput(attrs={'class': 'form-control decimal-mask'}),
            'indicador_ie': forms.Select(attrs={'class': 'form-control'}),
            'inscricao_municipal': forms.TextInput(attrs={'class': 'form-control'}),
            'id_estrangeiro': forms.TextInput(attrs={'class': 'form-control'}),
            'informacoes_adicionais': forms.Textarea(attrs={'class': 'form-control'}),
            'nome_pai': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control'}),
            'naturalidade': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_dependentes': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_residencia': forms.TextInput(attrs={'class': 'form-control'}),
            'dt_emissao_rg': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'tempo_residencia': forms.TextInput(attrs={'class': 'form-control'}),
            'dt_admissao': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'principal_renda': forms.TextInput(attrs={'class': 'form-control decimal-mask'}),
            'outra_renda': forms.TextInput(attrs={'class': 'form-control decimal-mask'}),
            'patrimonio': forms.TextInput(attrs={'class': 'form-control decimal-mask'}),
        }
        labels = {
            'nome_razao_social': _('Nome / Razão Social'),
            'tipo_pessoa': _(''),
            'limite_de_credito': _('Limite de Crédito'),
            'indicador_ie': _('Indicador da IE do Destinatário'),
            'inscricao_municipal': _('Inscrição Municipal'),
            'id_estrangeiro': _('Documento legal (Estrangeiro)'),
            'nome_pai': _('Nome do Pai'),
            'nome_mae': _('Nome da Mãe'),
            'naturalidade': _('Naturalidade'),
            'numero_dependentes': _('Numero de dependentes'),
            'tipo_residencia': _('Tipo de Residência'),
            'dt_emissao_rg': _('Data de Emissão'),
            'tempo_residencia': _('Tempo de Residência'),
            'dt_admissao': _('Data de Admissão'),
            'cargo': _('Cargo'),
            'principal_renda': _('Principal Renda'),
            'outra_renda': _('Outra Renda'),
            'patrimonio': _('Patrimônio'),
        }

    def save(self, commit=True):
        instance = super(ClienteForm, self).save(commit=False)
        instance.criado_por = self.request.user
        instance.emissor = self.request.user
        if commit:
            instance.save()
        return instance