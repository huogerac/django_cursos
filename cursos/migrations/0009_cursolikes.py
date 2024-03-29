# Generated by Django 4.0.5 on 2022-07-17 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cursos', '0008_curso_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='CursoLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('curso', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='cursos.curso')
                 ),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'curso')},
            },
        ),
    ]
