from django.db import models
from django import forms


# class Cliente(models.Model):
#     tipo=models.CharField(max_length=1)
#     data=models.DateField(max_length=8)
#     valor=models.FloatField(max_length=10)
#     cpd=models.IntegerField(max_length=11)
#     cartão=models.IntegerField(max_length=12)
#     hora =models.TimeField(max_length=6)
#     dono_da_loja=models.CharField(max_length=14)
#     nome_daloja=models.CharField(max_length=19)
    
class ArquivoForm(models.Model):
    # title = forms.CharField(max_length=50)
    # file = forms.FileField()
    title = models.CharField(max_length=50)
    file = models.FileField()
    tipo=models.CharField(max_length=1)
    data=models.DateField()
    valor=models.FloatField()
    cpd=models.IntegerField()
    cartao=models.IntegerField()
    hora =models.TimeField()
    dono_da_loja=models.CharField(max_length=14)
    nome_da_loja=models.CharField(max_length=19)
    
    