# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
from djangosige.apps.cadastro.views.passageiro import AdicionarPassageiroView, PassageirosListView, EditarPassageiroView
from djangosige.apps.cadastro.views.escola import AdicionarEscolaView, EditarEscolaView, EscolasListView

app_name = 'cadastro'
urlpatterns = [
    # Passageiro
    # /cadastro/passageiro/adicionar/
    url(r'passageiro/adicionar/$', AdicionarPassageiroView.as_view(), name='addpassageiroview'),
    # /cadastro/passageiro/listaclientes
    url(r'passageiro/listapassageiros/$', PassageirosListView.as_view(), name='listapassageirosview'),
    # /cadastro/passageiro/editar/
    url(r'passageiro/editar/(?P<pk>[0-9]+)/$', EditarPassageiroView.as_view(), name='editarpassageiroview'),

    # Escola
    #/cadastro/escola/adicionar/
    url(r'escola/adicionar/$', AdicionarEscolaView.as_view(), name='addescolaview'),
    #/cadastro/escola/listaempresas
    url(r'escola/listaescolas/$', EscolasListView.as_view(), name='listaescolasview'),
    #/cadastro/escola/editar/
    url(r'escola/editar/(?P<pk>[0-9]+)/$', EditarEscolaView.as_view(), name='editarescolaview'),

    # Empresa
    #/cadastro/empresa/adicionar/
    url(r'empresa/adicionar/$',
        views.AdicionarEmpresaView.as_view(), name='addempresaview'),
    #/cadastro/empresa/listaempresas
    url(r'empresa/listaempresas/$',
        views.EmpresasListView.as_view(), name='listaempresasview'),
    #/cadastro/empresa/editar/
    url(r'empresa/editar/(?P<pk>[0-9]+)/$',
        views.EditarEmpresaView.as_view(), name='editarempresaview'),

    # Cliente
    #/cadastro/cliente/adicionar/
    url(r'cliente/adicionar/$',
        views.AdicionarClienteView.as_view(), name='addclienteview'),
    #/cadastro/cliente/listaclientes
    url(r'cliente/listaclientes/$',
        views.ClientesListView.as_view(), name='listaclientesview'),
    #/cadastro/cliente/editar/
    url(r'cliente/editar/(?P<pk>[0-9]+)/$',
        views.EditarClienteView.as_view(), name='editarclienteview'),

    # Fornecedor
    #/cadastro/fornecedor/adicionar/
    url(r'fornecedor/adicionar/$',
        views.AdicionarFornecedorView.as_view(), name='addfornecedorview'),
    #/cadastro/fornecedor/listafornecedores
    url(r'fornecedor/listafornecedores/$',
        views.FornecedoresListView.as_view(), name='listafornecedoresview'),
    #/cadastro/fornecedor/editar/
    url(r'fornecedor/editar/(?P<pk>[0-9]+)/$',
        views.EditarFornecedorView.as_view(), name='editarfornecedorview'),

    # Transportadora
    #/cadastro/transportadora/adicionar/
    url(r'transportadora/adicionar/$',
        views.AdicionarTransportadoraView.as_view(), name='addtransportadoraview'),
    #/cadastro/transportadora/listatransportadoras
    url(r'transportadora/listatransportadoras/$',
        views.TransportadorasListView.as_view(), name='listatransportadorasview'),
    #/cadastro/transportadora/editar/
    url(r'transportadora/editar/(?P<pk>[0-9]+)/$',
        views.EditarTransportadoraView.as_view(), name='editartransportadoraview'),

    # Produto
    #/cadastro/produto/adicionar/
    url(r'produto/adicionar/$',
        views.AdicionarProdutoView.as_view(), name='addprodutoview'),
    #/cadastro/produto/listaprodutos
    url(r'produto/listaprodutos/$',
        views.ProdutosListView.as_view(), name='listaprodutosview'),
    #/cadastro/produto/listaprodutos/baixoestoque
    url(r'produto/listaprodutos/baixoestoque/$',
        views.ProdutosBaixoEstoqueListView.as_view(), name='listaprodutosbaixoestoqueview'),
    #/cadastro/produto/editar/
    url(r'produto/editar/(?P<pk>[0-9]+)/$',
        views.EditarProdutoView.as_view(), name='editarprodutoview'),

    # Outros
    # Categorias
    #/cadastro/outros/adicionarcategoria/
    url(r'outros/adicionarcategoria/$',
        views.AdicionarCategoriaView.as_view(), name='addcategoriaview'),
    #/cadastro/outros/listacategorias/
    url(r'outros/listacategorias/$',
        views.CategoriasListView.as_view(), name='listacategoriasview'),
    #/cadastro/outros/editarcategoria/
    url(r'outros/editarcategoria/(?P<pk>[0-9]+)/$',
        views.EditarCategoriaView.as_view(), name='editarcategoriaview'),

    # Unidades
    #/cadastro/outros/adicionarunidade/
    url(r'outros/adicionarunidade/$',
        views.AdicionarUnidadeView.as_view(), name='addunidadeview'),
    #/cadastro/outros/listaunidades/
    url(r'outros/listaunidades/$',
        views.UnidadesListView.as_view(), name='listaunidadesview'),
    #/cadastro/outros/editarcunidade/
    url(r'outros/editarunidade/(?P<pk>[0-9]+)/$',
        views.EditarUnidadeView.as_view(), name='editarunidadeview'),

    # Marcas
    #/cadastro/outros/adicionarmarca/
    url(r'outros/adicionarmarca/$',
        views.AdicionarMarcaView.as_view(), name='addmarcaview'),
    #/cadastro/outros/listamarcas/
    url(r'outros/listamarcas/$',
        views.MarcasListView.as_view(), name='listamarcasview'),
    #/cadastro/outros/editarmarca/
    url(r'outros/editarmarca/(?P<pk>[0-9]+)/$',
        views.EditarMarcaView.as_view(), name='editarmarcaview'),

    # Cidades
    #/cadastro/outros/adicionarcidade/
    url(r'outros/adicionarcidade/$',
        views.AdicionarCidadeView.as_view(), name='addcidadeview'),
    #/cadastro/outros/listacidades/
    url(r'outros/listacidades/$',
        views.CidadesListView.as_view(), name='listacidadesview'),
    #/cadastro/outros/editarcidade/
    url(r'outros/editarcidade/(?P<pk>[0-9]+)/$',
        views.EditarCidadeView.as_view(), name='editarcidadeview'),

    # Opcionais
    #/cadastro/outros/adicionarcidade/
    url(r'outros/adicionaropcional/$',
        views.AdicionarOpcionalView.as_view(), name='addopcionalview'),
    #/cadastro/outros/listacidades/
    url(r'outros/listaopcional/$',
        views.OpcionalListView.as_view(), name='listaopcionalview'),
    #/cadastro/outros/editarcidade/
    url(r'outros/editaropcional/(?P<pk>[0-9]+)/$',
        views.EditarOpcionalView.as_view(), name='editaropcionalview'),

    # Acomodações
    # /cadastro/outros/adicionaracomodacao/
    url(r'outros/adicionaracomodacao/$',
        views.AdicionarAcomodacaoView.as_view(), name='addacomodacaoview'),
    # /cadastro/outros/listaacomodacao/
    url(r'outros/listaacomodacao/$',
        views.AcomodacaoListView.as_view(), name='listaacomodacaoview'),
    # /cadastro/outros/editaracomodacao/
    url(r'outros/editaracomodacao/(?P<pk>[0-9]+)/$',
        views.EditarAcomodacaoView.as_view(), name='editaracomodacaoview'),

    # Informacoes de dada empresa (Ajax request)
    url(r'infoempresa/$', views.InfoEmpresa.as_view(), name='infoempresa'),
    url(r'infofornecedor/$', views.InfoFornecedor.as_view(), name='infofornecedor'),
    url(r'infocliente/$', views.InfoCliente.as_view(), name='infocliente'),
    url(r'infotransportadora/$', views.InfoTransportadora.as_view(),
        name='infotransportadora'),
    url(r'infoproduto/$', views.InfoProduto.as_view(), name='infoproduto'),

]
