from django.shortcuts import render
from Usuarios.models import *
from Usuarios.forms import *

def home(request):

    context = {

        "home": home
    }

    return render (request,"index.html", context)


def cadastrar_pessoa(request):
    
    form = PessoaForm()

    if request.method == "POST":
        form = PessoaForm(request.POST)

        if form.is_valid():
            
            form.save()
            
            return redirect("cadastrar_pessoa")
            
    context={
        
        "nome_pagina":"Cadastrar usuário",
        "form":form
    }

    return render(request,"cadastarusuario.html", context)

def cadastrar_gerente(request):
    
    form = PessoaForm()

    if request.method == "POST":
        form = PessoaForm(request.POST)

        if form.is_valid():
            
            form.save()
            
            return redirect("cadastrar_pessoa")
            
    context={
        
        "nome_pagina":"Cadastrar gerente",
        "form":form
    }

    return render (request,"cadastrargerente.html", context)


def cadastrar_empresa(request):
    
    form = PessoaForm()

    if request.method == "POST":
        form = PessoaForm(request.POST)

        if form.is_valid():
            
            form.save()
            
            return redirect("cadastrar_empresa")
            
    context={
        
        "nome_pagina":"Cadastrar empresa",
        "form":form
    }

    return render (request,"cadastrarempresa.html", context)

def cadastrar_vendedor(request):
    
    form = PessoaForm()

    if request.method == "POST":
        form = PessoaForm(request.POST)

        if form.is_valid():
            
            form.save()
            
            return redirect("cadastrar_empresa")
            
    context={
        
        "nome_pagina":"Cadastrar empresa",
        "form":form
    }
    return render (request,"cadastrarempresa.html", context)


