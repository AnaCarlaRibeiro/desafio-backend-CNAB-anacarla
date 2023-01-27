from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse
from .models import ArquivoForm
import ipdb
# from .forms import Cliente
# def form_modelform(request):
#     return render(request, 'cnabs/index.html')


def my_view(request):
    form = None
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        file = dict(request.FILES)['file'][0]

        if form.is_valid():
            instance = ArquivoForm(file=request.FILES['file'])
            instance.save()
            dados_tratados = []
            for linha in file.readlines():
                caracter = linha.decode("utf8")
                tipo = caracter[0]
                data = caracter[1:8]
                valor = caracter[9:18]
                cpf = caracter[19:29]
                cartao = caracter[30:41]
                hora = caracter[42:47]
                dono_da_loja = caracter[43:61]
                nome_da_loja = caracter[60:80]
                dados_tratados.append({'tipo': tipo, 'data': data, 'valor': valor, 'cartao': cartao,
                                    'hora': hora, 'dono_da_loja': dono_da_loja, 'nome_da_loja': nome_da_loja, 'cpf': cpf})

            for dado in dados_tratados:
                my_model = ArquivoForm(
                    tipo=dado['tipo'],
                    data=dado['data'],
                    valor=dado['valor'],
                    cpf=dado['cpf'],
                    cartao=dado['cartao'],
                    hora=dado['hora'],
                    dono_da_loja=dado['dono_da_loja'],
                    nome_da_loja=dado['nome_da_loja']
                    )

                my_model.save()

                # UploadFileForm.objects.create(**dados_tratados)

                return HttpResponse("O nome do arquivo enviado é:" + str(file))

    else:
        form = UploadFileForm()
    return render(request, 'cnabs/index.html', {'form': form})


# def tratar_dados(file):
#     dados_tratados = []
#     for linha in file.readlines():
#         caracter = linha.decode("utf8")
#         tipo = caracter[0]
#         data = caracter[1:8]
#         valor = caracter[9:18]
#         cpf = caracter[19:29]
#         cartao = caracter[30:41]
#         hora = caracter[42:47]
#         dono_da_loja = caracter[43:61]
#         nome_da_loja = caracter[60:80]
#         dados_tratados.append({'tipo': tipo, 'data': data, 'valor': valor, 'cartao': cartao,
#                               'hora': hora, 'dono_da_loja': dono_da_loja, 'nome_da_loja': nome_da_loja, 'cpf': cpf})
