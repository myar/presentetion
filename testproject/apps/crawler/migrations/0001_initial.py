# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilesStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='FoundLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(unique=True)),
                ('filename', models.ManyToManyField(related_name='urls', to='crawler.FilesStorage')),
            ],
        ),
    ]
