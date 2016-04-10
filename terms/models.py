from __future__ import unicode_literals

from django.db import models


class CustomBaseModel(models.Model):
    """
    Fields to apply to all models
    """
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Term(CustomBaseModel):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    query_count = models.IntegerField(default=0, blank=True)
    # TODO: handle synonymns and related terms, possibly through foreign key to self

    def __unicode__(self):
        return self.name


def audio_upload_path(instance, filename):
    return 'pronunciations/{}/{}'.format(instance.term_id, filename)


class Pronunciation(CustomBaseModel):
    term = models.ForeignKey(Term, related_name='pronunciations')
    phonetic_text = models.CharField(max_length=30, blank=True, null=True)
    audio = models.FileField(blank=True, null=True, upload_to=audio_upload_path)
    score = models.SmallIntegerField(default=0, blank=True)

    def __unicode__(self):
        return '{}:{} - {}'.format(self.pk, self.term.name, self.phonetic_text)
