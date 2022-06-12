from django.views import generic
from . import models
from django.db.models.aggregates import Sum
from . import forms
from django.shortcuts import render, HttpResponseRedirect

class projetoListView(generic.ListView):
    model = models.projeto
    form_class = forms.projetoForm
    ordering = ['-created']
