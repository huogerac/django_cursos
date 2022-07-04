# django_cursos

## Setup Inicial (primeira vez)

```shell
git clone git@github.com:huogerac/django_cursos.git
cd django_cursos
virtualenv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt

```

## Rodando o Projeto

```shell

1) Criar um .env com as senhas para o banco (veja .env-sample)

2) Subir um postgres com `docker-compose up`

3) Rodar o servidor do Django com `./manage.py runserver`
   ou `python3 manage.py runserver`

```
