
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re
import pdfx
import json

from django.http import HttpResponse, HttpResponseForbidden
from django.core.files.storage import FileSystemStorage
from django.views import View
from django.views.generic import DetailView, ListView

from ..models import FilesStorage, FoundLinks
from ..serializers import serialize_data


URL_PATTERN = ('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|'
               '[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')


class PostFile(View):

    def post(self, request):
        ufile = request.FILES.get('file')

        if ufile:
            file_type = ufile .name.split('.')[-1]
            if file_type == 'pdf':
                fs = FileSystemStorage()
                filename = fs.save(ufile .name, ufile)
                pdf = pdfx.PDFx(filename)
                urls = re.findall(URL_PATTERN, pdf.get_text())
                filestorage = FilesStorage.objects.create(filename=filename)
                if urls:
                    for url in urls:
                        try:
                            f = FoundLinks.objects.get(url=url)
                        except FoundLinks.DoesNotExist:
                            f = FoundLinks.objects.create(url=url)
                        f.filename.add(filestorage)

                fs.delete(ufile.name)
                return HttpResponse('Ok')
        return HttpResponseForbidden()


class GetGeneralIngo(ListView):

    model = FilesStorage

    def get(self, *args, **kwargs):
        data = [ob.as_json() for ob in self.get_queryset()]
        return HttpResponse(json.dumps(data), content_type="application/json")


class GetFileInfo(DetailView):

    model = FoundLinks

    def get_queryset(self):
        return self.model.objects.filter(filename=self.pk)

    def get(self, request, pk, *args, **kwargs):
        self.pk = pk
        data = serialize_data(self.get_queryset(), fields=('url'))
        return HttpResponse(data)
