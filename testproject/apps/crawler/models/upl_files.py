# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class FilesStorage(models.Model):
    filename = models.CharField(max_length=250)

    def __unicode__(self):
        return self.filename

    def count_urls(self):
        return self.urls.all().count()

    def as_json(self):
        return dict(id=self.id, filename=self.filename,
                    count_urls=self.count_urls())


class FoundLinks(models.Model):
    filename = models.ManyToManyField(FilesStorage, related_name='urls')
    url = models.TextField(unique=True)

    def __unicode__(self):
        return self.url
