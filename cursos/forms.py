from django import forms

from .models import Curso


class CursoModelForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            "nome",
            "descricao",
            "imagem",
            "autor",
        ]
