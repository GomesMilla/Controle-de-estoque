from django.shortcuts import render, redirect
from Usuarios.models import *
from Usuarios.forms import *
from django.contrib.auth.decorators import login_required


@login_required
def home(request):

    context = {

        "home": home,
    }

    return render(request, "index.html", context)


def cadastrar_pessoa(request):

    form = PessoaForm()

    if request.method == "POST":
        form = PessoaForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("cadastrar_pessoa")

    context = {

        "nome_pagina": "Cadastrar usuário",
        "form": form
    }

    return render(request, "cadastarusuario.html", context)


@login_required
def cadastrar_gerente(request):

    form = GerenteForm()

    if request.method == "POST":
        form = GerenteForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("cadastrar_pessoa")

    context = {

        "nome_pagina": "Cadastrar gerente",
        "form": form
    }

    return render(request, "cadastrargerente.html", context)


@login_required
def cadastrar_empresa(request):

    form = EmpresaForm()

    if request.method == "POST":
        form = EmpresaForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("cadastrar_empresa")

    context = {

        "nome_pagina": "Cadastrar empresa",
        "form": form
    }

    return render(request, "cadastrarempresa.html", context)


@login_required
def cadastrar_vendedor(request):

    form = VendedorForm()

    if request.method == "POST":
        form = VendedorForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("cadastrar_empresa")

    context = {

        "nome_pagina": "Cadastrar Vendedor",
        "form": form
    }
    return render(request, "cadastrarvendedor.html", context)


@login_required
def listar_pessoas(request):
    allpessoas = Pessoa.objects.all()

    context = {
        "listPessoa": allpessoas,
    }

    return render(request, "listar_usuarios.html", context)


@login_required
def listar_empresas(request):
    allempresa = Empresa.objects.all()

    context = {
        "listempresa": allempresa,
    }

    return render(request, "listaempresa.html", context)


@login_required
def listar_vendedor(request):
    allvendedor = Vendedor.objects.all()

    context = {
        "listvendedor": allvendedor,
    }

    return render(request, "listavendedores.html", context)


@login_required
def listar_gerente(request):
    allgerente = Gerente.objects.all()

    context = {
        "listgerente": allgerente,
    }

    return render(request, "listagerente.html", context)
