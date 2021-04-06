# from django.shortcuts import render
# from estoque.models import *
# from estoque.forms import *


# def cadastrar_produto(request):
#     form = ProdutoForm()

#     if request.method == "POST":
#         form = ProdutoForm(request.POST)

#         if form.is_valid():

#             form.save()

#             return redirect("cadastrar_pessoa")

#     context = {

#         "nome_pagina": "Cadastrar usuário",
#         "form": form
#     }

#     return render(request, "cadastarusuario.html", context)
