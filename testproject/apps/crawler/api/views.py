
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pdfx
import re

from django.http import HttpResponse, HttpResponseForbidden
from django.core.files.storage import FileSystemStorage
from django.views import View
from django.views.generic import DetailView, ListView

from ..models import FilesStorage, FoundLinks


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
        data = {}
        return HttpResponse(data)


class GetFileInfo(DetailView):

    model = FilesStorage

    def get(self, pk):
        return
