from django import forms
from Usuarios.models import *


class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = ('__all__')


class GerenteForm(forms.ModelForm):

    class Meta:
        model = Gerente
        fields = ('__all__')


class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = [
            "nome", "pais", "CNPJ", "cep", "estado", "cidade",
            "bairro", "logradouro", "numero_da_casa", "telefone", "email",
        ]


class VendedorForm(forms.ModelForm):

    class Meta:
        model = Vendedor
        fields = ('__all__')
