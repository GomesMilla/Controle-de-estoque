from django.contrib import admin
from django.urls import path
from Usuarios.models import *
from Usuarios.views import *
from transacao.models import *
from transacao.views import *
from estoque.models import *
from estoque.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name="home",),

    path('cadastrar_pessoa', cadastrar_pessoa, name="cadastrar_pessoa"),

    path('Cadastrar-empresa/', cadastrar_empresa, name="cadastrar_empresa",),

    path('Cadastrar-gerente/', cadastrar_gerente, name="cadastrar_gerente",),

    path('Cadastar-vendedor/', cadastrar_vendedor, name="cadastrar_vendedor",),

    path('Listar-empresa/', listar_empresas, name="listar_empresas",),

    path('Listar-pessoas', listar_pessoas, name="listar_pessoas",),

    path('Listar-vendedor', listar_vendedor, name="listar_vendedor",),

    path('Gerente-cadastrado', listar_gerente, name="listar_gerente",),

    path('Cadastrar-produto/', cadastrar_produto, name="cadastrar_produto",),

    path('Produto-estoque/', produto_estoque, name="produto_estoque",),

    path('Listar-produto/', listar_produto, name="listar_produto",),

    path('Produtos-cadastrados/', produtos_cadastrados,
         name="produtos_cadastrados",),

    path('Transacao/', realizar_transacao, name="realizar_transacao",),

]
