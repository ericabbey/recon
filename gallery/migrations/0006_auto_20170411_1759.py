# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-11 17:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20170411_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media',
            old_name='author',
            new_name='artist',
        ),
    ]
