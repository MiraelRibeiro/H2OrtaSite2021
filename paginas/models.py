from django.db import models

class TabelasDadosUsuario(models.Model):
    id_user = models.OneToOneField('auth.User', on_delete=models.PROTECT, null=True)
    id_usuario = models.AutoField(primary_key=True)  
    nome = models.CharField(max_length=100, blank=True, null=False)
    email = models.CharField(max_length=50, blank=True, null=False)
    telefone = models.CharField(max_length=11, blank=True, null=False)
    cpf = models.CharField(max_length=11, blank=True, null=False)
    cidade = models.CharField(max_length=255, blank=True, null=False)
    estado = models.CharField(max_length=255, blank=True, null=False)
    pais = models.CharField(max_length=50, blank=True, null=False)
    cep = models.CharField(max_length=10, blank=True, null=False)

    class Meta:
        db_table = 'dados_usuario'


class DadosEstufa(models.Model):
    id_dados_estufa = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=10, blank=True, null=False)
    modelo = models.CharField(max_length=50, blank=True, null=False)
    estrutura = models.CharField(max_length=15, blank=True, null=False)
    valor = models.CharField(max_length=50, blank=True, null=False)
    slots = models.CharField(max_length=2, blank=True)
    fileiras = models.CharField(max_length=2, blank=True)
    itensInclusos = models.CharField(max_length=255, blank=True)
    altura_cm = models.CharField(max_length=10, blank=True)
    largura_cm = models.CharField(max_length=20, blank=True)
    comprimento_cm = models.CharField(max_length=20, blank=True)
    imagem = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = 'dados_estufa'

   

class EnderecosDeEntrega(models.Model):
    id_user = models.ForeignKey('auth.User', models.DO_NOTHING)
    id_endereco_entrega = models.AutoField(primary_key=True)    
    nome = models.CharField(max_length=255, blank=True, null=False)
    rua = models.CharField(max_length=255, blank=True)
    casa = models.CharField(max_length=10, blank=True)
    cep = models.CharField(max_length=12, blank=True)
    bairro = models.CharField(max_length=255, blank=True)    
    cidade = models.CharField(max_length=255, blank=True, null=False)
    estado = models.CharField(max_length=255, blank=True, null=False)
    pais = models.CharField(max_length=255, blank=True, null=False)

    class Meta:
        db_table = 'dados_entrega'


class TabelasDadosCompra(models.Model):
    id_compra = models.AutoField(primary_key=True) 
    id_user = models.ForeignKey('auth.User', models.DO_NOTHING, null=True)
    id_produto = models.ForeignKey(DadosEstufa, models.DO_NOTHING)
    id_entrega = models.ForeignKey(EnderecosDeEntrega, models.DO_NOTHING)
    data_hora = models.DateField(auto_now=True)
    forma_pagamento = models.CharField(max_length=255, blank=True, null=False)

    class Meta:
        db_table = 'dados_compra'