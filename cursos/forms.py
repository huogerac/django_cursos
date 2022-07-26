from django import forms

from .models import Curso, Autor


class CursoModelForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            "nome",
            "descricao",
            "imagem",
            "autor",
        ]


class CursoForm(forms.Form):
    nome = forms.CharField(max_length=128, required=True)
    descricao = forms.CharField(required=True)
    autor = forms.ModelChoiceField(queryset=Autor.objects.order_by('nome').all())
    imagem = forms.URLField(
        max_length=1024,
    )
    ativo = forms.BooleanField(required=False)
