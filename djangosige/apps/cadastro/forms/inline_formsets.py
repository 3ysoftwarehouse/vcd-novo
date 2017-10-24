# -*- coding: utf-8 -*-

from django import forms
from django.forms import inlineformset_factory
from django.utils.translation import ugettext_lazy as _
from decimal import Decimal

from django.forms import modelformset_factory
from djangosige.apps.cadastro.models import Pessoa, Endereco, Telefone, Email, Site, Banco, Documento, Produto, ProdutoCidade, ProdutoAcomodacao, Cidade, Acomodacao, DocumentoProduto


class DocumentoProdutoForm(forms.ModelForm):
    class Meta:
        model = DocumentoProduto
        fields = '__all__'
        widgets = {
            'arquivo': forms.FileInput(attrs={'class': 'form-control'})
        }
        labels = {
            'arquivo': _('Anexe um arquivo'),
        }


class EnderecoForm(forms.ModelForm):

    class Meta:
        model = Endereco
        fields = ('tipo_endereco', 'logradouro', 'numero', 'bairro',
                  'complemento', 'pais', 'cpais', 'uf', 'cep', 'municipio', 'cmun',)

        labels = {
            'tipo_endereco': _('Tipo'),
            'logradouro': _("Logradouro"),
            'numero': _("Número"),
            'bairro': _("Bairro"),
            'complemento': _("Complemento"),
            'pais': _("País"),
            'cpais': _("Código do País"),
            'municipio': _("Município (sem acentuação)"),
            'cmun': _("Código do município"),
            'cep': _("CEP (Apenas dígitos)"),
            'uf': _("UF"),
        }
        widgets = {
            'tipo_endereco': forms.Select(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'cpais': forms.TextInput(attrs={'class': 'form-control'}),
            'municipio': forms.Select(attrs={'class': 'form-control'}),
            'cmun': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.Select(attrs={'class': 'form-control'}),
        }


class TelefoneForm(forms.ModelForm):

    class Meta:
        model = Telefone
        fields = ('tipo_telefone', 'telefone',)
        labels = {
            'tipo_telefone': _("Telefone"),
            'telefone': _(''),
        }
        widgets = {
            'tipo_telefone': forms.Select(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EmailForm(forms.ModelForm):

    class Meta:
        model = Email
        fields = ('email',)
        labels = {
            'email': _('Email')
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class SiteForm(forms.ModelForm):

    class Meta:
        model = Site
        fields = ('site',)
        labels = {
            'site': _('Site'),
        }
        widgets = {
            'site': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BancoForm(forms.ModelForm):

    class Meta:
        model = Banco
        fields = ('banco', 'agencia', 'conta', 'digito',)
        labels = {
            'banco': _('Banco'),
            'agencia': _('Agência'),
            'conta': _('Conta'),
            'digito': _('Dígito'),
        }
        widgets = {
            'banco': forms.Select(attrs={'class': 'form-control'}),
            'agencia': forms.TextInput(attrs={'class': 'form-control'}),
            'conta': forms.TextInput(attrs={'class': 'form-control'}),
            'digito': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DocumentoForm(forms.ModelForm):

    class Meta:
        model = Documento
        fields = ('tipo', 'documento',)
        labels = {
            'tipo': _('Tipo'),
            'documento': _('Documento'),
        }
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProdutoCidadeForm(forms.ModelForm):
    quantidade = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control number'}), initial=1, label='Quantidade',required=False)

    class Meta:
        model = ProdutoCidade
        fields = ('cidade','quantidade',)
        labels = {
            'cidade': _('Cidade'),
        }
        widgets = {
            'cidade': forms.Select(attrs={'class': 'form-control'}),
        }


class ProdutoAcomodacaoForm(forms.ModelForm):
    preco = forms.DecimalField(max_digits=16, decimal_places=2, localize=True, widget=forms.TextInput(
        attrs={'class': 'form-control decimal-mask', 'placeholder': 'R$ 0,00'}), initial=Decimal('0.00'), label='Preço',
                               required=False)

    class Meta:
        model = ProdutoAcomodacao
        fields = ('acomodacao','preco',)
        labels = {
            'acomodacao': _('Acomodação'),
        }
        widgets = {
            'acomodacao': forms.Select(attrs={'class': 'form-control'}),
        }

ProdutoAcomodacaoFormSet = inlineformset_factory(
    Produto, ProdutoAcomodacao, form=ProdutoAcomodacaoForm, extra=1, can_delete=True)
ProdutoCidadeFormSet = inlineformset_factory(
    Produto, ProdutoCidade, form=ProdutoCidadeForm, extra=1, can_delete=True)
EnderecoFormSet = inlineformset_factory(
    Pessoa, Endereco, form=EnderecoForm, extra=1, can_delete=True)
TelefoneFormSet = inlineformset_factory(
    Pessoa, Telefone, form=TelefoneForm, extra=1, can_delete=True)
EmailFormSet = inlineformset_factory(
    Pessoa, Email, form=EmailForm, extra=1, can_delete=True)
SiteFormSet = inlineformset_factory(
    Pessoa, Site, form=SiteForm, extra=1, can_delete=True)
BancoFormSet = inlineformset_factory(
    Pessoa, Banco, form=BancoForm, extra=1, can_delete=True)
DocumentoFormSet = inlineformset_factory(
    Pessoa, Documento, form=DocumentoForm, extra=1, can_delete=True)
DocumentoProdutoFormSet = modelformset_factory(DocumentoProduto, 
    form=DocumentoProdutoForm, extra=1, can_delete=True)