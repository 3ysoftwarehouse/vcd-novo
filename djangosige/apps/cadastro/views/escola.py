# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy

from djangosige.apps.cadastro.forms.escola import EscolaForm
from djangosige.apps.cadastro.models.escola import Escola

from .base import AdicionarPessoaView, PessoasListView, EditarPessoaView


class AdicionarEscolaView(AdicionarPessoaView):
    template_name = "cadastro/pessoa_add.html"
    success_url = reverse_lazy('cadastro:listaescolasview')
    success_message = "Escola <b>%(nome_razao_social)s </b>adicionada com sucesso."
    permission_codename = 'add_escola'

    def get_context_data(self, **kwargs):
        context = super(AdicionarEscolaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'CADASTRAR ESCOLA'
        context['return_url'] = reverse_lazy('cadastro:listaescolasview')
        context['tipo_pessoa'] = 'escola'
        return context

    def get(self, request, *args, **kwargs):
        form = EscolaForm(prefix='escola_form')
        return super(AdicionarEscolaView, self).get(request, form, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = EscolaForm(request.POST, request.FILES,
                           prefix='escola_form', request=request)
        return super(AdicionarEscolaView, self).post(request, form, *args, **kwargs)


class EscolasListView(PessoasListView):
    template_name = 'cadastro/pessoa_list.html'
    model = Escola
    context_object_name = 'all_escolas'
    success_url = reverse_lazy('cadastro:listaescolasview')
    permission_codename = 'view_escola'

    def get_context_data(self, **kwargs):
        context = super(EscolasListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ESCOLAS CADASTRADAS'
        context['add_url'] = reverse_lazy('cadastro:addescolaview')
        context['tipo_pessoa'] = 'escola'
        return context


class EditarEscolaView(EditarPessoaView):
    form_class = EscolaForm
    model = Escola
    template_name = "cadastro/pessoa_edit.html"
    success_url = reverse_lazy('cadastro:listaescolasview')
    success_message = "Escola <b>%(nome_razao_social)s </b>editada com sucesso."
    permission_codename = 'change_escola'

    def get_context_data(self, **kwargs):
        context = super(EditarEscolaView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('cadastro:listaescolasview')
        context['tipo_pessoa'] = 'escola'
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form_class.prefix = "escola_form"
        form = self.get_form(form_class)

        logo_file = Escola.objects.get(pk=self.object.pk).logo_file
        return super(EditarEscolaView, self).get(request, form, logo_file=logo_file, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = form_class(request.POST, request.FILES,
                          prefix='escola_form', instance=self.object, request=request)
        logo_file = Escola.objects.get(pk=self.object.pk).logo_file
        return super(EditarEscolaView, self).post(request, form, logo_file=logo_file, *args, **kwargs)
