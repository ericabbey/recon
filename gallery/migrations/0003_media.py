# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-11 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gallery', '0002_delete_media'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('source', models.FileField(upload_to='')),
                ('url', models.URLField()),
                ('updated', models.DateField(auto_now=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
