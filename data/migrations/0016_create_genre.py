# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0015_rename_circa_to_birth_death_circa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='birth_death_circa',
            field=models.BooleanField(default=False, verbose_name='Birth / death dates are approximate.'),
        ),
    ]
