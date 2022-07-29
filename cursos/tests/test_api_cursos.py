from cursos.models import Curso, Autor


def test_listar_cursos_status_code(client, db):
    resposta = client.get('/api/cursos')
    assert resposta.status_code == 200


def test_listar_cursos_sem_curso_salvo(client, db):
    resposta = client.get('/api/cursos')
    assert resposta.json() == {'cursos': []}


def test_listar_cursos_sem_autor(client, db):
    Curso.objects.create(
        nome='Curso de Django',
        descricao='Curso completo de django',
        imagem='http://imagem.com',
        ativo=True)
    resposta = client.get('/api/cursos')
    assert resposta.json() == {
        'cursos': [
            {
                'nome': 'Curso de Django',
                'descricao': 'Curso completo de django',
                'imagem': 'http://imagem.com',
                'ativo': True,
                'autor': None
            }
        ]
    }


def test_listar_cursos_com_autor(client, db):
    autor = Autor.objects.create(nome='Renzo', bio='Engenheiro')
    Curso.objects.create(
        nome='Curso de Django',
        descricao='Curso completo de django',
        imagem='http://imagem.com',
        ativo=True,
        autor=autor
    )
    resposta = client.get('/api/cursos')
    assert resposta.json() == {
        'cursos': [
            {
                'nome': 'Curso de Django',
                'descricao': 'Curso completo de django',
                'imagem': 'http://imagem.com',
                'ativo': True,
                'autor': {
                    'nome': 'Renzo',
                    'bio': 'Engenheiro',
                }
            }
        ]
    }
