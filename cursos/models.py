from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Autor(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    bio = models.TextField()

    def json_dict(self):
        return {
            'nome': self.nome,
            'bio': self.bio,
        }

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=256, unique=True, null=True, blank=True)
    descricao = models.TextField()
    autor = models.ForeignKey("Autor", on_delete=models.SET_NULL, null=True, blank=True, related_name="cursos")
    imagem = models.URLField(
        max_length=1024,
    )
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        # na primeira vez
        if not self.id:
            self.slug = slugify(self.nome)
        super(Curso, self).save(*args, **kwargs)

    def json_dict(self):
        """
        Transforma dados do modelo curso em formato serializável pelo json
        """
        autor = self.autor
        autor_json = None
        if autor is not None:
            autor_json = autor.json_dict()
        return {
            'nome': self.nome,
            'descricao': self.descricao,
            'imagem': self.imagem,
            'ativo': self.ativo,
            'autor': autor_json
        }


class Aula(models.Model):
    curso = models.ForeignKey("Curso", on_delete=models.CASCADE, related_name="aulas")
    nome = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=256, unique=True, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nome)
        super(Aula, self).save(*args, **kwargs)


class CursoLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="likes")
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['user', 'curso']]
