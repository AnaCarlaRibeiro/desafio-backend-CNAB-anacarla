from django.db import models
from django import forms


    
class ArquivoModel(models.Model):  
    tipo=models.CharField(max_length=1)
    data=models.DateField()
    valor=models.FloatField()
    cpf=models.IntegerField()
    cartao=models.CharField(max_length=12)
    hora =models.TimeField()
    dono_da_loja=models.CharField(max_length=14)
    nome_da_loja=models.CharField(max_length=19)
    
    