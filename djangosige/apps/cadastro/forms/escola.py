# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

from djangosige.apps.cadastro.models.escola import Escola, MinhaEscola


class EscolaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(EscolaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Escola
        fields = ('nome_razao_social', 'inscricao_municipal', 'cnae',
                  'logo_file', 'iest', 'informacoes_adicionais',)

        widgets = {
            'nome_razao_social': forms.TextInput(attrs={'class': 'form-control'}),
            'cnae': forms.TextInput(attrs={'class': 'form-control'}),
            'inscricao_municipal': forms.TextInput(attrs={'class': 'form-control'}),
            'logo_file': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'iest': forms.TextInput(attrs={'class': 'form-control'}),
            'informacoes_adicionais': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome_razao_social': _('Nome / Razão Social'),
            'cnae': _('CNAE'),
            'inscricao_municipal': _('Inscrição Municipal'),
            'logo_file': _('Logo'),
            'iest': _('IE do substituto tributário'),
            'informacoes_adicionais': _('Informações Adicionais'),
        }

    def save(self, commit=True):
        instance = super(EscolaForm, self).save(commit=False)
        instance.tipo_pessoa = 'PJ'
        instance.criado_por = self.request.user
        if 'escola_form-logo_file' in self.request.FILES:
            instance.logo_file = self.request.FILES['escola_form-logo_file']
        if commit:
            instance.save()
        return instance


class MinhaEscolaForm(forms.ModelForm):

    class Meta:
        model = MinhaEscola
        fields = ('m_escola',)

        widgets = {
            'm_escola': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'm_escola': _('Minha Escola'),
        }
