# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 09:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Beer',
            new_name='FeedItem',
        ),
    ]
