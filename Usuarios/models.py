from django.db import models

STATUS_GENERO = [
    ("FEMININO", "Feminino"),
    ("MASCULINO", "Masculino"),
    ("OUTRO", "Outro"),
]
ESTADO_CIVIL = [
    ("SOLTEIRO(A)", "Solteiro(a)"),
    ("CASADO(A)", "Casado(a)"),
    ("DIVORCIADO(A)", "Divorciado(a)"),
]

ESCOLARIDADE = [
    ("EFI", "Ensino fundamental incompleto"),
    ("EFC", "Ensino fundamental completo"),
    ("EMI", "Ensino médio incompleto"),
    ("EMC", "Ensino médio completo"),
    ("ESI", "Ensino superior incompleto"),
    ("ESC", "Ensino superior completo"),
]


class Pessoa(models.Model):

    nome = models.CharField(verbose_name="Nome completo:", max_length=194)
    naturalidade = models.CharField(
        verbose_name="Naturalidade", max_length=194, blank=False, null=False)
    pais = models.CharField(verbose_name="País",
                            max_length=194, blank=False, null=False)
    escolaridade = models.CharField(
        verbose_name="Escolaridade:", max_length=30, choices=ESCOLARIDADE)
    status = models.CharField(verbose_name="Genero",
                              max_length=10, choices=STATUS_GENERO)
    email = models.EmailField(verbose_name="E-mail:",
                              unique=True, blank=False, null=False)
    telefone_celular = models.CharField(
        verbose_name="Número de telefone", max_length=19, unique=False, blank=False, null=False)
    cpf = models.CharField(verbose_name="CPF:", max_length=11,
                           unique=True, blank=False, null=False)
    nascimento = models.DateField(
        verbose_name="Data de nascimento:", max_length=10)
    estado_civil = models.CharField(
        verbose_name="Estado civil:", max_length=40, choices=ESTADO_CIVIL)
    profissao = models.CharField(verbose_name="Profissão:", max_length=194)
    cep = models.CharField(verbose_name="CEP:", max_length=194)
    estado = models.CharField(verbose_name="Estado:",
                              max_length=30, blank=False, null=False)
    cidade = models.CharField(verbose_name="Cidade:",
                              max_length=194, blank=False, null=False)
    bairro = models.CharField(verbose_name="Bairro:",
                              max_length=194, blank=False, null=False)
    logradouro = models.CharField(
        verbose_name="Logradouro::", max_length=194, blank=False, null=False)
    numero = models.CharField(
        verbose_name="Número da residencia:", max_length=194, blank=False, null=False)
    telefone = models.CharField(
        verbose_name="Telefone da residencia:", max_length=194, blank=True, null=True)
    data_de_cadastro = models.DateTimeField(
        verbose_name="Data do cadastro", auto_now_add=True)

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        db_table: "pessoa"

    def __str__(self):
        return self.nome


class Gerente(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Gerente"
        verbose_name_plural = "Gerentes"
        db_table = "Gerente"

    def __str__(self):
        return self.pessoa.nome


class Empresa(models.Model):
    nome = models.CharField(verbose_name="Nome da empresa:", max_length=194)
    email = models.EmailField(verbose_name="E-mail:",
                              unique=True, blank=False, null=False)
    cep = models.CharField(verbose_name="CEP:", max_length=194)
    pais = models.CharField(verbose_name="País",
                            max_length=194, blank=False, null=False)
    estado = models.CharField(verbose_name="Estado:",
                              max_length=30, blank=False, null=False)
    cidade = models.CharField(verbose_name="Cidade:",
                              max_length=194, blank=False, null=False)
    bairro = models.CharField(verbose_name="Bairro:",
                              max_length=194, blank=False, null=False)
    logradouro = models.CharField(
        verbose_name="Logradouro:", max_length=194, blank=False, null=False)
    numero_da_casa = models.CharField(
        verbose_name="Número da residencia ou compleme:", max_length=194, blank=False, null=False)
    CNPJ = models.CharField(
        verbose_name="CNPJ da empresa:", max_length=194, unique=True)
    telefone = models.CharField(
        verbose_name="Contato da empresa:", max_length=194, blank=True, null=True)
    data_de_cadastro = models.DateTimeField(
        verbose_name="Data do cadastro",  auto_now_add=True)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        db_table = "empresa"

    def __str__(self):
        return self.nome


class Vendedor(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"
        db_table = "vendedor"

    def __str__(self):
        return self.pessoa.nome
