# Generated by Django 4.0.6 on 2022-08-05 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8)),
                ('rua', models.CharField(max_length=128)),
                ('bairro', models.CharField(max_length=64)),
                ('cidade', models.CharField(max_length=64)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
    ]
