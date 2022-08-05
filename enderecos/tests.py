from django.urls import reverse
from enderecos.models import Endereco


def test_busca_endereco_por_cep_com_sucesso(client, db):
    Endereco.objects.create(
        cep='12223750',
        rua='Rua Curaçao',
        bairro='Vista Verde',
        cidade='São José dos Campos',
        estado='SP'
    )
    resposta = client.get(reverse('enderecos.detalhe', kwargs={'cep': '12223750'}))
    assert resposta.status_code == 200


def test_formato_do_endereco_com_cep_sem_ponto_ou_traco(client, db):
    Endereco.objects.create(
        cep='12223750',
        rua='Rua Curaçao',
        bairro='Vista Verde',
        cidade='São José dos Campos',
        estado='SP'
    )
    resposta = client.get(reverse('enderecos.detalhe', kwargs={'cep': '12223750'}))
    endereco_dict = resposta.json()
    assert endereco_dict == {
        'cep': '12223-750',
        'rua': 'Rua Curaçao',
        'bairro': 'Vista Verde',
        'cidade': 'São José dos Campos',
        'estado': 'SP',
    }
