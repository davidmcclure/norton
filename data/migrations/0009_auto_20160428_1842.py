# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 18:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_auto_20160428_1834'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='work',
            unique_together=set([('title', 'author', 'parent')]),
        ),
    ]
