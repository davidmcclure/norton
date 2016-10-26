# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0024_add_notes_to_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='gb_country',
            field=models.CharField(blank=True, choices=[('England', 'England'), ('Northern Ireland', 'Northern Ireland'), ('Wales', 'Wales'), ('Scotland', 'Scotland')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='race',
            field=models.ManyToManyField(blank=True, to='data.Race', verbose_name='Race / Ethnicity'),
        ),
    ]