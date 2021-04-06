from django import forms
from estoque.models import *


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('__all__')


class ProdutoEstoqueForm(forms.ModelForm):
    class Meta:
        model = ProdutoEstoque
        fields = ('__all__')
