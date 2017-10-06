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
                  'limite_de_credito', 'indicador_ie', 'id_estrangeiro', 'informacoes_adicionais', 'escola',)
        widgets = {
            'nome_razao_social': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_pessoa': forms.RadioSelect(attrs={'class': 'form-control'}),
            'escola': forms.Select(attrs={'class': 'form-control'}),
            'limite_de_credito': forms.TextInput(attrs={'class': 'form-control decimal-mask'}),
            'indicador_ie': forms.Select(attrs={'class': 'form-control'}),
            'inscricao_municipal': forms.TextInput(attrs={'class': 'form-control'}),
            'id_estrangeiro': forms.TextInput(attrs={'class': 'form-control'}),
            'informacoes_adicionais': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome_razao_social': _('Razão Social'),
            'tipo_pessoa': _(''),
            'escola': _('Escola'),
            'limite_de_credito': _('Limite de Crédito'),
            'indicador_ie': _('Indicador da IE do Destinatário'),
            'inscricao_municipal': _('Inscrição Municipal'),
            'id_estrangeiro': _('Documento legal (Estrangeiro)'),
            'informacoes_adicionais': _('Informações Adicionais'),
        }

    def save(self, commit=True):
        instance = super(PassageiroForm, self).save(commit=False)
        instance.criado_por = self.request.user
        if commit:
            instance.save()
        return instance
