from django.db import models
from Usuarios.models import *
from estoque.models import *

TIPO_TRANSACAO = [
    ("ENTRADA", "Entrada"),
    ("SAIDA", "Saída"),
]


class Transacao(models.Model):
    tipo_de_transacao = models.CharField(
        verbose_name="Tipo de transação:", max_length=30, choices=TIPO_TRANSACAO)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    gerente = models.ForeignKey(Gerente, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    data = models.DateField("Data da transação", auto_now_add=True)

    class Meta:
        verbose_name = "Transação"
        verbose_name_plural = "Transações"
        db_table = "transacao"

    def __str__(self):
        return self.tipo_de_transacao


class ProdutosTransacao(models.Model):
    transacao = models.ForeignKey(Transacao, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtd_de_produtos = models.FloatField(verbose_name="Quantidade de produto:")

    class Meta:
        verbose_name = "Produto de Transação"
        verbose_name_plural = "Produtos de transações"
        db_table = "produtostransacao"

    def __str__(self):
        return self.produto.nome
