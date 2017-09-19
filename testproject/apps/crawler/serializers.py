# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers

def serialize_data(data, fields):
    return serializers.serialize('json', data, fields=fields)
