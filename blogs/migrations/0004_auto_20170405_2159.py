# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-05 21:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_likes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='likes',
            new_name='like',
        ),
    ]
