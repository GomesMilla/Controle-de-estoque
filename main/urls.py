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

    path('', home, name = "home",),

    path('cadastrar_pessoa', cadastrar_pessoa, name = "cadastrar_pessoa"),

    path('Cadastrar-empresa/', cadastrar_empresa, name = "cadastrar_empresa",),

    path('Cadastrar-gerente/', cadastrar_gerente, name = "cadastrar_gerente",),

    path('Cadastar-vendedor/', cadastrar_vendedor, name = "cadastrar_vendedor",),
    



]
