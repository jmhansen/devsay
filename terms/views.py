from __future__ import absolute_import

import requests

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.conf import settings
from django.views.generic import TemplateView, CreateView

from terms import models
from forvo.models import ForvoWord, ForvoPronunciation


class IndexView(TemplateView):
    template_name = 'index.html'


class TermCreateView(CreateView):
    model = models.Term
    template_name = 'terms/term_create_form.html'
    fields = ['name']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save()
        # http://apifree.forvo.com/key/551b8eddc60f432397e3b830b9073e72/format/json/action/word-pronunciations/word/cat/language/en
        r = requests.get(
            'http://apifree.forvo.com/key/{}/format/json/action/word-pronunciations/word/{}/language/en'.format(
                settings.FORVO_API_KEY, form.cleaned_data['name'])
        )
        json = r.json()

        if r.status_code == 200:

            word = ForvoWord.objects.create(
                original_word=form.cleaned_data['name'],
                num_pronunciations=json['attributes']['total']
            )

            for item in json['items']:
                ForvoPronunciation.objects.create(
                    word=word,
                    forvo_id=item['id'],
                    addtime=item['addtime'],
                    hits=item['hits'],
                    username=item['username'],
                    sex=item['sex'],
                    country=item['country'],
                    country_code=item['code'],
                    language_name=item['langname'],
                    path_mp3=item['pathmp3'],
                    path_ogg=item['pathogg'],
                    rate=item['rate'],
                    num_votes=item['num_votes'],
                    num_positive_votes=item['num_positive_votes']
                )

        return HttpResponseRedirect(self.get_success_url())
