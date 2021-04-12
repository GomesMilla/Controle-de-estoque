from django.shortcuts import render, redirect
from transacao.models import *
from transacao.forms import *
from estoque.models import *
import datetime


def compra_de_produtos(request):
    today = datetime.date.today()

    form = TransacaoForm()
    listProdutos = Produto.objects.all()

    if request.method == "POST":
        form = TransacaoForm(request.POST)

        if form.is_valid():
            if form.is_valid():
                objTransacao = form.save(commit=False)
                objTransacao.tipo_de_transacao = 'ENTRADA'
                objTransacao.save()
                listProdutosTransacao = request.POST.getlist("Produto[]", None)
                listQtdMovi = request.POST.getlist("Qtd[]", None)
                listDataVenci = request.POST.getlist("datavalidade[]", None)

            for index, q in enumerate(listProdutosTransacao):
                objProduto = Produto.objects.get(
                    pk=listProdutosTransacao[index])

                objProdutoEstoque = ProdutoEstoque()
                objProdutoEstoque.produto = objProduto
                objProdutoEstoque.quantidade = listQtdMovi[index]
                objProdutoEstoque.data_de_validade = listDataVenci[index]
                objProdutoEstoque.save()

                objProdutoMovi = ProdutosTransacao()
                objProdutoMovi.transacao = objTransacao
                objProdutoMovi.produto = objProdutoEstoque.produto
                objProdutoMovi.qtd_de_produtos = listQtdMovi[index]
                objProdutoMovi.save()

                objProdutoEstoque.save()

            return redirect("home")

    context = {
        "listProdutos": listProdutos,
        "nome_pagina": "Compra de produtos",
        "form": form
    }

    return render(request, "comprar.html", context)


def venda_de_produtos(request):
    today = datetime.date.today()

    form = TransacaoForm()
    listProdutos = ProdutoEstoque.objects.filter(
        quantidade__gt=0, data_de_validade__gte=today)
    if request.method == "POST":
        form = TransacaoForm(request.POST)

        if form.is_valid():
            objTransacao = form.save(commit=False)
            objTransacao.tipo_de_transacao = 'SAIDA'
            objTransacao.save()
            listProdutosTransacao = request.POST.getlist("Produto[]", None)
            listQtdMovi = request.POST.getlist("Qtd[]", None)

            for index, q in enumerate(listProdutosTransacao):
                objProdutoEstoque = ProdutoEstoque.objects.get(
                    pk=listProdutosTransacao[index])

                objProdutoMovi = ProdutosTransacao()
                objProdutoMovi.transacao = objTransacao
                objProdutoMovi.produto = objProdutoEstoque.produto
                objProdutoMovi.qtd_de_produtos = listQtdMovi[index]
                objProdutoMovi.save()
                objProdutoEstoque.quantidade -= float(
                    objProdutoMovi.qtd_de_produtos)

                objProdutoEstoque.save()

            return redirect("home")

    context = {
        "listProdutos": listProdutos,
        "nome_pagina": "Venda de produto",
        "form": form
    }

    return render(request, "vender.html", context)


def relatorio_movimentacoes(request):

    listmovimentacoes = Transacao.objects.all()
    listrelatorio = []

    for aux in listmovimentacoes:
        listProdutosTransacao = ProdutosTransacao.objects.filter(
            transacao=aux)
        obj = {
            "movimentacao": aux,
            "Produtos": listProdutosTransacao
        }
        listrelatorio.append(obj)

    context = {

        "listrelatorio": listrelatorio,
    }

    return render(request, "listar_movimentacoes.html", context)
