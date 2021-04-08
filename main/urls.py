from django.contrib import admin
from django.urls import path
from Usuarios.models import *
from Usuarios.views import *
from transacao.models import *
from transacao.views import *
from estoque.models import *
from estoque.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name="home",),

    path("logout/", auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),

    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),

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

    path('Compra-produtos/', compra_de_produtos, name="compra_de_produtos",),

    path('Venda-de-produtos/', venda_de_produtos, name="venda_de_produtos",),


]
