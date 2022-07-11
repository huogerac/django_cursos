from django.db import models
from django.template.defaultfilters import slugify


class Autor(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    bio = models.TextField()

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=256, unique=True, null=True, blank=True)
    descricao = models.TextField()
    autor = models.ForeignKey("Autor", on_delete=models.SET_NULL, null=True, blank=True, related_name="cursos")
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        # na primeira vez
        if not self.id:
            self.slug = slugify(self.nome)
        super(Curso, self).save(*args, **kwargs)


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