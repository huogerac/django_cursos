from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from enderecos.models import Endereco


def detalhe(request, cep):
    cep_normalizado = cep.replace('.', '').replace('-', '')
    endereco=Endereco.objects.get(cep=cep_normalizado)
    cep_para_apresentacao = cep_normalizado[:5] + '-' + cep_normalizado[5:]
    return JsonResponse({
        'cep': cep_para_apresentacao,
        'rua': endereco.rua,
        'bairro': endereco.bairro,
        'cidade': endereco.cidade,
        'estado': endereco.estado,
    })
