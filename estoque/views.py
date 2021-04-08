from django.shortcuts import render, redirect
from estoque.models import *
from estoque.forms import *
import datetime


def cadastrar_produto(request):
    form = ProdutoForm()

    if request.method == "POST":
        form = ProdutoForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("cadastrar_produto")

    context = {

        "nome_pagina": "Cadastrar produto",
        "form": form
    }

    return render(request, "cadastrar_produto.html", context)


def produto_estoque(request):
    form = ProdutoEstoqueForm()

    if request.method == "POST":
        form = ProdutoEstoqueForm(request.POST)
        print(form)

        if form.is_valid():

            form.save()

            return redirect("produto_estoque")

    context = {

        "nome_pagina": "Produto estoque",
        "form": form
    }

    return render(request, "produtoestoque.html", context)


def listar_produto(request):
    today = datetime.date.today()
    allproduto = ProdutoEstoque.objects.all()
    listProdutoEstoque = []
    for q in allproduto:
        if q.data_de_validade >= today:
            diasVenc = q.data_de_validade - today
            diasVenc = diasVenc.days
        else:
            diasVenc = 0
        obj = {
            'Produto': q,
            "DiasVenc": diasVenc,
        }
        listProdutoEstoque.append(obj)
    context = {
        "listProdutoEstoque": listProdutoEstoque,
    }

    return render(request, "listar_produto.html", context)


def produtos_cadastrados(request):

    allcadastro = Produto.objects.all()

    context = {
        "listProduto": allcadastro,
    }

    return render(request, "listar_produtos_cadastrados.html", context)
