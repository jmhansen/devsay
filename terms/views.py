from __future__ import absolute_import

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from terms import models


class IndexView(TemplateView):
    template_name = 'index.html'


class TermCreateView(CreateView):
    model = models.Term
    template_name = 'terms/term_create_form.html'
    fields = ['name']
    success_url = reverse_lazy('home')
