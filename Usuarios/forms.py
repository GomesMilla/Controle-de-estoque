from django import forms
from Usuarios.models import *


class PessoaForm(forms.ModelForm):
    def save(self, commit=True):
        user = super(PessoaForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = Pessoa
        fields = [
            "nome", "pais", "cpf", "estado", "cidade", "cep",
            "bairro", "logradouro", "numero", "telefone", "email", "naturalidade", "escolaridade",
            "status", "telefone", "nascimento", "estado_civil", "profissao", "telefone_celular", "estado_civil", "password"

        ]


class GerenteForm(forms.ModelForm):

    class Meta:
        model = Gerente
        fields = ('__all__')


class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = [
            "nome", "pais", "cnpj", "cep", "estado", "cidade",
            "bairro", "logradouro", "numero_da_casa", "telefone", "email",
        ]


class VendedorForm(forms.ModelForm):

    class Meta:
        model = Vendedor
        fields = ('__all__')
