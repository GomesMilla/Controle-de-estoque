from django.shortcuts import render, redirect
from transacao.models import *
from transacao.forms import *
from estoque.models import *


def realizar_transacao(request):

    form = TransacaoForm()
    listProdutos = ProdutoEstoque.objects.filter(quantidade__gt=0)
    if request.method == "POST":
        form = TransacaoForm(request.POST)

        if form.is_valid():
            objTransacao = form.save()
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
                if objTransacao.tipo_de_transacao == "ENTRADA":
                    objProdutoEstoque.quantidade += float(
                        objProdutoMovi.qtd_de_produtos)
                else:
                    objProdutoEstoque.quantidade -= float(
                        objProdutoMovi.qtd_de_produtos)

                objProdutoEstoque.save()

            return redirect("home")

    context = {
        "listProdutos": listProdutos,
        "nome_pagina": "Cadastrar produto",
        "form": form
    }

    return render(request, "transacao.html", context)


def venda_e_compra(request):

    form = TransacaoForm()
    listProdutos = ProdutoEstoque.objects.filter()
    if request.method == "POST":
        form = TransacaoForm(request.POST)

        if form.is_valid():
            objTransacao = form.save()
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
                if objTransacao.tipo_de_transacao == "ENTRADA":
                    objProdutoEstoque.quantidade += float(
                        objProdutoMovi.qtd_de_produtos)
                else:
                    objProdutoEstoque.quantidade -= float(
                        objProdutoMovi.qtd_de_produtos)

                objProdutoEstoque.save()

            return redirect("home")
