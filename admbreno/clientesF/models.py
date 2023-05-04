from django.db import models

# Create your models here.
class Cliente(models.Model):
    data_cadastro = models.DateField(auto_now = True)
    hora_cadastro = models.TimeField(auto_now = True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length = 14)
    data_nascimento = models.DateField ()
    profissao = models.CharField(max_length=100)
    telefone = models.CharField(max_length = 15)
    celular = models.CharField(max_length = 15)
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length = 100)
    uf = models.CharField(max_length = 2)
    email = models.EmailField()

    def __str__(self):
        return self.nome
    

class Veiculo(models.Model):
    data_cadastro = models.DateField(auto_now = True)
    hora_cadastro = models.TimeField(auto_now = True)
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, related_name = 'veiculos')
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    placa = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return self.placa
    
class Servico(models.Model):
    data_cadastro = models.DateField(auto_now = True)
    hora_cadastro = models.TimeField(auto_now = True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_entrega = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='servicos')
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='servicos')
    descricao = models.CharField(max_length = 200)
    detalhes = models.TextField(blank=True, null=True)
    
    
class Fornecedor(models.Model):
    RAZAO_SOCIAL_MAX_LENGTH = 200
    NOME_FANTASIA_MAX_LENGTH = 200
    SEGMENTO_MAX_LENGTH = 100
    CONTATO_MAX_LENGTH = 200
    TELEFONE_MAX_LENGTH = 20
    CEP_MAX_LENGTH = 9
    ENDERECO_MAX_LENGTH = 250
    CIDADE_MAX_LENGTH = 80
    ESTADO_MAX_LENGTH = 80
    UF_MAX_LENGTH = 2
    EMAIL_MAX_LENGTH = 250
    SITE_MAX_LENGTH = 250

    data_cadastro = models.DateField(auto_now = True)
    hora_cadastro = models.TimeField(auto_now = True)
    razao_social = models.CharField(max_length=RAZAO_SOCIAL_MAX_LENGTH)
    nome_fantasia = models.CharField(max_length = NOME_FANTASIA_MAX_LENGTH)
    cnpj = models.CharField(max_length=18)
    segmento = models.CharField(max_length=SEGMENTO_MAX_LENGTH)
    contato = models.CharField(max_length=CONTATO_MAX_LENGTH)
    telefone = models.CharField(max_length=TELEFONE_MAX_LENGTH)
    celular = models.CharField(max_length = 20, blank = True, null = True)
    cep = models.CharField(max_length=CEP_MAX_LENGTH)
    endereco = models.CharField(max_length=ENDERECO_MAX_LENGTH)
    cidade = models.CharField(max_length=CIDADE_MAX_LENGTH)
    estado = models.CharField(max_length=ESTADO_MAX_LENGTH)
    uf = models.CharField(max_length=UF_MAX_LENGTH)
    email = models.EmailField(max_length=EMAIL_MAX_LENGTH)
    site = models.URLField(max_length=SITE_MAX_LENGTH, blank=True, null=True)

    def __str__(self):
        return self.razao_social
