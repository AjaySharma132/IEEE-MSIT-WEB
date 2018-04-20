# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-20 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='event',
            name='event_description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
    ]