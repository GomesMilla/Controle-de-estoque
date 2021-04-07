from django.shortcuts import render, redirect
from transacao.models import *
from transacao.forms import *
from estoque.models import *


def realizar_transacao(request):

    form = TransacaoForm()

    if request.method == "POST":
        form = TransacaoForm(request.POST)

        if form.is_valid():
            transacao.save()
            listProdutosTransacao = request.POST.getlist("Produto[]", None)
            listQtdMovi = request.POST.getlist("Qtd[]", None)

            for index, q in enumerate(listProdutosTransacao):

                objProdutoEstoque = ProdutoEstoque.objects.get(
                    pk=listProdutosTransacao[index])

                objProdutoMovi = ProdutosTransacao()
                objProdutoMovi.transacao = transacao
                objProdutoMovi.produto = objProdutoEstoque.produto
                objProdutoMovi.quantidade = listQtdMovi[index]
                objProdutoMovi.save()

                if Transacao.tipo_de_transacao == "ENTRADA":
                    objProdutoEstoque.qtd_de_produtos += float(
                        objProdutosTransacao.qtd_de_produtos)
                else:
                    objProdutoEstoque.qtd_de_produtos -= float(
                        objProdutoMovi.qtd_de_produtos)

                objProdutosEstoque.save()

            return redirect("index")

    context = {
        "nome_pagina": "Movimentação",
        "form": form,
        "listProdutos": listProdutos,
    }

    return render(request, "movimentacao.html", context)

    form.save()

    return redirect("realizar_transacao")

    context = {

        "nome_pagina": "Cadastrar produto",
        "form": form
    }

    return render(request, "transacao.html", context)
