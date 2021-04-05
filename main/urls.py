"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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

    path('Cadastrar-pessoa/', cadastrar_pessoa, name = "cadastrar_pessoa",),

    path('Cadastrar-empresa/', cadastrar_empresa, name = "cadastrar_empresa",),

    path('Cadastrar-gerente/', cadastrar_gerente, name = "cadastrar_gerente",),

    path('Cadastar-vendedor/', cadastrar_vendedor, name = "cadastrar_vendedor",),
    



]
