from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed, assertContains, assertRedirects

from cursos.models import Curso, Autor
from django.contrib.auth import get_user_model


def test_formulario_de_curso_status_ok(client, db):
    resposta = client.get(reverse('cursos.form'))
    assert resposta.status_code == 200


def test_template_novo_curso(client, db):
    resposta = client.get(reverse('cursos.form'))
    assertTemplateUsed(resposta, 'cursos/cursos_form.html')


def test_tag_form_novo_curso_presente(client, db):
    resposta = client.get(reverse('cursos.form'))
    assertContains(resposta, '<form')


def test_salvar_curso(client, db):
    autor = Autor.objects.create()
    dados = {
        'nome': 'Curso de Django',
        'descricao': 'Curso completo de django',
        'imagem': 'http://imagem.com',
        'ativo': 'on',
        'autor': str(autor.id)
    }
    client.post(
        reverse('cursos.form'),
        dados
    )
    assert Curso.objects.count() == 1
    curso = Curso.objects.first()
    assert curso.nome == 'Curso de Django'
    assert curso.descricao == 'Curso completo de django'
    assert curso.imagem == 'http://imagem.com'
    assert curso.ativo
    assert curso.autor_id == autor.id


def test_listar_cursos_apos_salvamento(client, db):
    User = get_user_model()
    user = User.objects.create(username='teste', email='teste@teste.com', password='senha')
    client.force_login(user)
    dados = {
        'nome': 'Curso de Django',
        'descricao': 'Curso completo de django',
        'imagem': 'http://imagem.com',
        'ativo': 'on',
    }
    resposta = client.post(
        reverse('cursos.form'),
        dados
    )
    assertRedirects(resposta, reverse('cursos.listar.tudo'))
