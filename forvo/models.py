from __future__ import unicode_literals

from django.db import models


class ForvoWord(models.Model):

    original_word = models.CharField(max_length=30, unique=True)
    num_pronunciations = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.original_word


class ForvoPronunciations(models.Model):

    word = models.ForeignKey(ForvoWord, related_name='pronunciations')
    forvo_id = models.PositiveIntegerField()
    addtime = models.DateTimeField()
    hits = models.PositiveIntegerField()   # This field also works for 0
    username = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)
    country = models.CharField(max_length=50)
    country_code = models.CharField(max_length=5)
    language_name = models.CharField(max_length=50)
    path_mp3 = models.URLField()
    path_ogg = models.URLField()
    rate = models.IntegerField()
    num_votes = models.PositiveIntegerField()
    num_positive_votes = models.PositiveIntegerField()

    def __unicode__(self):
        return '{} - id:{}'.format(self.word.original_word, self.forvo_id)
