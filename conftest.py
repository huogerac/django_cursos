import pytest
from django.contrib.auth import get_user_model


@pytest.fixture()
def user(db):
    print('Setup do user')
    User = get_user_model()
    yield User.objects.create(username='teste', email='teste@teste.com', password='senha')
    print('Teardown do user')


@pytest.fixture()
def client_com_usuario_logado(client, user):
    print('Setup do client_com_usuario_logado')
    client.force_login(user)
    yield client
    print('Teardown do client_com_usuario_logado')
