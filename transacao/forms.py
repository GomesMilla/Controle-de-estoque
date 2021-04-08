from django import forms
from transacao.models import *


class TransacaoForm(forms.ModelForm):

    class Meta:
        model = Transacao
        exclude = ["tipo_de_transacao"]
        fields = ('__all__')


class ProdutosTransacaoForm(forms.ModelForm):

    class Meta:
        model = ProdutosTransacao
        fields = ('__all__')
