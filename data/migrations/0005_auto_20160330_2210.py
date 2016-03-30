# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-30 22:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20160310_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data.Author'),
        ),
        migrations.AlterField(
            model_name='work',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.Work'),
        ),
    ]
