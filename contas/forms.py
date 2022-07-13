from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UsuarioForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm, forms.Form):
    message_incorrect_password = "Usuário ou senha inválida"
    message_inactive = "Usuário está inativo"

    username = forms.CharField(
        max_length=76,
        widget=forms.TextInput(attrs={"placeholder": "Email or Username"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(self.message_incorrect_password)
            if not self.user_cache.is_active:
                raise forms.ValidationError(self.message_inactive)
        return self.cleaned_data
