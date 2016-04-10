# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 21:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import terms.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pronunciation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('phonetic_text', models.CharField(blank=True, max_length=30, null=True)),
                ('audio', models.FileField(blank=True, null=True, upload_to=terms.models.audio_upload_path)),
                ('score', models.SmallIntegerField(blank=True, default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('query_count', models.IntegerField(blank=True, default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='pronunciation',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pronunciations', to='terms.Term'),
        ),
    ]
