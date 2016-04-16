# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForvoPronunciations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forvo_id', models.PositiveIntegerField()),
                ('addtime', models.DateTimeField()),
                ('hits', models.PositiveIntegerField()),
                ('username', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=1)),
                ('country', models.CharField(max_length=50)),
                ('country_code', models.CharField(max_length=5)),
                ('language_name', models.CharField(max_length=50)),
                ('path_mp3', models.URLField()),
                ('path_ogg', models.URLField()),
                ('rate', models.IntegerField()),
                ('num_votes', models.PositiveIntegerField()),
                ('num_positive_votes', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ForvoWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_word', models.CharField(max_length=30, unique=True)),
                ('num_pronunciations', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='forvopronunciations',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pronunciations', to='forvo.ForvoWord'),
        ),
    ]
