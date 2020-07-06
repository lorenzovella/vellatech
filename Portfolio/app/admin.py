from django.contrib import admin
from django import forms

from . import models


class projetoAdminForm(forms.ModelForm):

    class Meta:
        model = models.projeto
        fields = "__all__"


class projetoAdmin(admin.ModelAdmin):
    form = projetoAdminForm
    list_display = [
    "nome","descricao","etapas","link","periodoexecucao"
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


admin.site.register(models.projeto, projetoAdmin)
