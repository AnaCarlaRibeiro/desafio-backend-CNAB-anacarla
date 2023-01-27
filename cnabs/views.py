from django.shortcuts import render, redirect
from .forms import UploadFileForm
from django.http import HttpResponse
from .models import ArquivoModel

from django.core.files.storage import FileSystemStorage
import ipdb
# from .forms import Cliente
# def form_modelform(request):
#     return render(request, 'cnabs/index.html')


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file = dict(request.FILES)['file'][0]
        if form.is_valid():  
           
            dados_tratados = []
            for linha in file.readlines():
                caracter = linha.decode("utf8")
                tipo = caracter[0]
                data = caracter[1:9]
                valor = caracter[9:19]
                cpf = caracter[19:30]
                cartao = caracter[30:42]
                hora = caracter[42:48]
                dono_da_loja = caracter[48:62]
                nome_da_loja = caracter[62:81]
                dados_tratados.append({'tipo': tipo, 'data': data, 'valor': valor, 'cartao': cartao,
                                    'hora': hora, 'dono_da_loja': dono_da_loja, 'nome_da_loja': nome_da_loja, 'cpf': cpf})
            for dado in dados_tratados:
                my_model = ArquivoModel(
                    tipo=dado['tipo'],
                    data=dado['data'],
                    valor=dado['valor'],
                    cpf=dado['cpf'],
                    cartao=dado['cartao'],
                    hora=dado['hora'],
                    dono_da_loja=dado['dono_da_loja'],
                    nome_da_loja=dado['nome_da_loja']
                    )
                # print(dado)

                my_model.save()
                

            
             # ipdb.set_trace()    
        return HttpResponse("O nome do arquivo enviado é:" + str(file))
    else:
        form = UploadFileForm()
    return render(request, 'cnabs/index.html', {'form': form})

