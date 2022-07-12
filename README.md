# django_cursos

## GUIA DETALHADO PARA INICIAR O PROJETO

- 1. NAVEGUE ATÉ UMA PASTA PARA ORGANIZAR SEUS ESTUDOS

```
cd ~/workspace/django-pratica
```

- 2. BAIXAR CÓDIGO

```
git clone https://github.com/huogerac/django_cursos.git django_cursos_aula8
cd django_cursos_aula8
```

Você pode mudar o final de aula8 para aula9 ou aula20

- 3. SUBIR BANCO LOCAL usando containers

```
cp .env-sample .env
--> VEJA o arquivo .env e os dados de conexão com banco/PORTA!
docker-compose up --build
--> CTRL+C para parar
docker-compose up -d
--> Faça docker ps para ver se tem um container postgres rodando
--> ERRO comum nesta etapa, o Docker utilizar cache das camadas, faça:
    docker system prune --volumes
    tente novamente o build
```

- 4. INSTALAR DEPENDENCIAS DO DJANGO

```
virtualenv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
--> Erro comum nesta etapa, nao conseguir instalar o psycopg2, veja o PDF da Aula 07
```

- 5. Criar o banco com as migrações existentes

```
./manage.py migrate
# Crie um usuário para logar no Admin
./manage.py createsuperuser
```

- 6. Rode o projeto do django_cursos

```
# Finalmente, rode o Django (em modo desenvolvimento)
./manage.py runserver

# Se você quiser acessar seu django do mobile ou qualquer outro pc na mesma rede:
./manage.py runserver 0.0.0.0:8000
```

**FIM DO SETUP** Neste ponto o setup do projeto está completo! Parabéns!

## GUIA PARA TESTAR

- 1. Você pode acessar o admin e criar via web Usuários para login, Autores, Cursos e Aulas

- 2. Também é possível criar registros (INSERTS, UPDATES) na base via terminal

Rodar o ./manage.py shell

```
❯ ./manage.py shell
Python 3.8.10 (default, Mar 15 2022, 12:22:08)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
```

Depois utilizar os comandos abaixo, alterando para os dados que quiser...

```
>>> from cursos.models import Autor, Curso, Aula
>>> novo_autor = Autor.objects.create(nome='John Doe', bio='')
>>> Curso.objects.create(nome='Javascript', descricao='', autor=novo_autor)
<Curso: Javascript>
```
