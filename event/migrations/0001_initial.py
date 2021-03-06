# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-11 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('organizer', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('theme', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('cover', models.FileField(upload_to='')),
                ('map_image', models.FileField(upload_to='')),
                ('map_url', models.URLField()),
                ('timestamp', models.DateField(auto_now=True)),
            ],
        ),
    ]
