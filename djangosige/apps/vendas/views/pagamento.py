# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from django.http import HttpResponse
from django.core import serializers

from djangosige.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView

from djangosige.apps.vendas.forms import CondicaoPagamentoForm, PagamentoForm
from djangosige.apps.vendas.models import CondicaoPagamento, Pagamento, Venda

from django.http import JsonResponse


class AdicionarCondicaoPagamentoView(CustomCreateView):
    form_class = CondicaoPagamentoForm
    template_name = "vendas/pagamento/condicao_pagamento_add.html"
    success_url = reverse_lazy('vendas:listacondicaopagamentoview')
    success_message = "Condição de pagamento <b>%(descricao)s </b>adicionada com sucesso."
    permission_codename = 'add_condicaopagamento'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=self.object.descricao)

    def get_context_data(self, **kwargs):
        context = super(AdicionarCondicaoPagamentoView,
                        self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR CONDIÇÃO DE PAGAMENTO'
        context['return_url'] = reverse_lazy(
            'vendas:listacondicaopagamentoview')
        return context


class CondicaoPagamentoListView(CustomListView):
    template_name = 'vendas/pagamento/condicao_pagamento_list.html'
    model = CondicaoPagamento
    context_object_name = 'all_cond_pagamento'
    success_url = reverse_lazy('vendas:listacondicaopagamentoview')
    permission_codename = 'view_condicaopagamento'

    def get_context_data(self, **kwargs):
        context = super(CondicaoPagamentoListView,
                        self).get_context_data(**kwargs)
        context['title_complete'] = 'CONDIÇÕES DE PAGAMENTO CADASTRADAS'
        context['add_url'] = reverse_lazy('vendas:addcondicaopagamentoview')
        return context


class EditarCondicaoPagamentoView(CustomUpdateView):
    form_class = CondicaoPagamentoForm
    model = CondicaoPagamento
    template_name = "vendas/pagamento/condicao_pagamento_edit.html"
    success_url = reverse_lazy('vendas:listacondicaopagamentoview')
    success_message = "Condição de pagamento <b>%(descricao)s </b>editada com sucesso."
    permission_codename = 'change_condicaopagamento'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=self.object.descricao)

    def get_context_data(self, **kwargs):
        context = super(EditarCondicaoPagamentoView,
                        self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy(
            'vendas:listacondicaopagamentoview')
        return context


class InfoCondicaoPagamento(View):

    def post(self, request, *args, **kwargs):
        pag = CondicaoPagamento.objects.get(pk=request.POST['pagamentoId'])
        data = serializers.serialize('json', [pag, ], fields=(
            'n_parcelas', 'parcela_inicial', 'dias_recorrencia'))
        return HttpResponse(data, content_type='application/json')


class AdicionarPagamento(View):

    def post(self, request, pk=None, *args, **kwargs):
        data = {}
        
        form = PagamentoForm(request.POST)
        if form.is_valid():
            try:
                venda = Venda.objects.get(pk=pk)

                pagamento = form.save(commit=False)
                pagamento.venda_id = venda
                pagamento.save()

                data['status'] = 200
                data['message'] = 'success'
                data['venda'] = venda.valor_total - pagamento.valor_parcela
                data['pagamento'] = {
                    'indice_parcela':pagamento.indice_parcela, 
                    'forma':pagamento.forma, 
                    'vencimento':pagamento.vencimento, 
                    'valor_parcela':pagamento.valor_parcela, 
                    'observacao':pagamento.observacao, 
                    'id':pagamento.id
                }
                    
            except:
                data['status'] = 500
                data['message'] = 'error'
        else:
            data['status'] = 501
            data['message'] = 'Formulário inválido'

        return JsonResponse(data)


class RemoverPagamento(View):

    def get(self, request, pk=None, *args, **kwargs):
        data = {}

        try:
            pagamento = Pagamento.objects.get(pk=pk)
            pagamento.delete()

            data['status'] = 200
            data['message'] = 'success'
        except:
            data['status'] = 500
            data['message'] = 'error'
        
        return JsonResponse(data)