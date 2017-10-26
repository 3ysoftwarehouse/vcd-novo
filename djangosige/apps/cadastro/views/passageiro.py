# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy

from djangosige.apps.cadastro.forms.passageiro import PassageiroForm
from djangosige.apps.cadastro.models.passageiro import Passageiro

from .base import AdicionarPessoaView, PessoasListView, EditarPessoaView


class AdicionarPassageiroView(AdicionarPessoaView):
    template_name = "cadastro/pessoa_add.html"
    success_url = reverse_lazy('cadastro:listapassageirosview')
    success_message = "Passageiro <b>%(nome_razao_social)s </b>adicionado com sucesso."
    permission_codename = 'add_passageiro'

    def get_context_data(self, **kwargs):
        context = super(AdicionarPassageiroView, self).get_context_data(**kwargs)
        context['title_complete'] = 'CADASTRAR PASSAGEIRO'
        context['return_url'] = reverse_lazy('cadastro:listapassageirosview')
        context['tipo_pessoa'] = 'passageiro'
        return context

    def get(self, request, *args, **kwargs):
        form = PassageiroForm(prefix='passageiro_form')
        return super(AdicionarPassageiroView, self).get(request, form, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.POST['passageiro_form-limite_de_credito'] = request.POST['passageiro_form-limite_de_credito'].replace(
            '.', '')
        form = PassageiroForm(request.POST, request.FILES,
                              prefix='passageiro_form', request=request)
        return super(AdicionarPassageiroView, self).post(request, form, *args, **kwargs)


class PassageirosListView(PessoasListView):
    template_name = 'cadastro/pessoa_list.html'
    model = Passageiro
    context_object_name = 'all_passageiros'
    success_url = reverse_lazy('cadastro:listapassageirosview')
    permission_codename = 'view_passageiro'

    def get_context_data(self, **kwargs):
        context = super(PassageirosListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'PASSAGEIROS CADASTRADOS'
        context['add_url'] = reverse_lazy('cadastro:addpassageiroview')
        context['tipo_pessoa'] = 'passageiro'
        return context
    
    def get_queryset(self):
        return Passageiro.objects.filter(emissor=self.request.user)


class EditarPassageiroView(EditarPessoaView):
    form_class = PassageiroForm
    model = Passageiro
    template_name = "cadastro/pessoa_edit.html"
    success_url = reverse_lazy('cadastro:listapassageirosview')
    success_message = "Passageiro <b>%(nome_razao_social)s </b>editado com sucesso."
    permission_codename = 'change_passageiro'

    def get_context_data(self, **kwargs):
        context = super(EditarPassageiroView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('cadastro:listapassageirosview')
        context['tipo_pessoa'] = 'passageiro'
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form_class.prefix = "passageiro_form"
        form = self.get_form(form_class)

        return super(EditarPassageiroView, self).get(request, form, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        request.POST['passageiro_form-limite_de_credito'] = request.POST['passageiro_form-limite_de_credito'].replace(
            '.', '')
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = form_class(request.POST, request.FILES,
                          prefix='passageiro_form', instance=self.object, request=request)
        return super(EditarPassageiroView, self).post(request, form, *args, **kwargs)
