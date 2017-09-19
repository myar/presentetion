# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.files import File

from ..models import FilesStorage, FoundLinks


class SimpleTest(TestCase):
    """
    Simple test for testing work with file
    """
    def setUp(self):
        # setting up
        self.pdf_file = File(open('apps/crawler/tests/resources/test.pdf'))
        self.doc_file = File(open('apps/crawler/tests/resources/test.doc'))
        self.url = reverse('postfile')

    def test_upload_pdf(self):
        # Test for pdf's file
        resp = self.client.post(self.url, {'file': self.pdf_file})
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Ok')

    def test_upload_doc(self):
        # Test for doc's file
        resp = self.client.post(self.url, {'file': self.doc_file})
        self.assertEqual(resp.status_code, 403)

    def test_serch_in_pdf(self):
        # Test for seach urs in pdf files
        f_c = FilesStorage.objects.all().count()
        resp = self.client.post(self.url, {'file': self.pdf_file})
        self.assertEqual(f_c, 0)
        f_c = FilesStorage.objects.all().count()
        u_c = FoundLinks.objects.all().count()
        self.assertEqual(f_c, 1)
        self.assertEqual(u_c, 2)

    def test_general(self):
        self.client.post(self.url, {'file': self.pdf_file})
        url = reverse('general-info')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "http://test.com.ua")
