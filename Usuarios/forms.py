from django import forms
from Usuarios.models import *


class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = [
            "nome" , "naturalidade", "pais", "escolaridade","status","email","telefone_celular",
            "cpf", "nascimento","estado_civil","profissao","cep","estado", "cidade","bairro",
            "logradouro","numero","telefone", 
        ]

class GerenteForm(forms.ModelForm):

    class Meta:
        model = Gerente
        fields = ('__all__')

class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = [
            "nome" , "pais", "CNPJ","cep","estado", "cidade",
            "bairro", "logradouro","numero_da_casa","telefone", 
        ]

class VendedorForm(forms.ModelForm):

    class Meta: 
        model = Vendedor
        fields = ('__all__')
            

