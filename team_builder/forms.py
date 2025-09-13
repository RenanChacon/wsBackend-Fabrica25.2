from django import forms
from .models import Time, Pokemon

class TimeForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = ["nome_time", "nome_jogo", "ano_criacao"]
        labels = {
            "nome_time": "Nome do Time",
            "nome_jogo": "Nome do Jogo",
            "ano_criacao": "Ano de Criação",
        }
        widgets = {
            "nome_time": forms.TextInput(attrs={"class": "form-control"}),
            "nome_jogo": forms.TextInput(attrs={"class": "form-control"}),
            "ano_criacao": forms.NumberInput(attrs={"class": "form-control"}),
        }

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ["nome", "apelido", "nivel"]
        labels = {
            "nome": "Nome do pokemon",
            "apelido": "Apelido (opcional)",
            "nivel": "Nível",
        }
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "apelido": forms.TextInput(attrs={"class": "form-control"}),
            "nivel": forms.NumberInput(attrs={"class": "form-control", "min": 1, "max": 100}),
        }