from django.db import models
from django.urls import reverse


class projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=300)
    etapas = models.TextField(max_length=500)
    link = models.URLField(max_length=200,blank=True)
    periodoexecucao = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now_add=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)
