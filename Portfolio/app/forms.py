from django import forms
from . import models


class projetoForm(forms.ModelForm):
    class Meta:
        model = models.projeto
        fields = ["nome","descricao","etapas","link","periodoexecucao"]
