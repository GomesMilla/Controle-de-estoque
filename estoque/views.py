from django.shortcuts import render, redirect
from estoque.models import *
from estoque.forms import *


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
        form = ProdutoEstoque(request.POST)

        if form.is_valid():

            form.save()

            return redirect("cadastrar_estoque")

    context = {

        "nome_pagina": "Produto estoque",
        "form": form
    }

    return render(request, "produtoestoque.html", context)


def listar_produto(request):

    allproduto = ProdutoEstoque.objects.all()

    context = {
        "listProdutoEstoque": allproduto,
    }

    return render(request, "listar_produto.html", context)


def produtos_cadastrados(request):

    allcadastro = Produto.objects.all()

    context = {
        "listProduto": allcadastro,
    }

    return render(request, "listar_produtos_cadastrados.html", context)
