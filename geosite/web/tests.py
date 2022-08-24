from django.test import TestCase

from .utils import txt2coordinates


class IndexTest(TestCase):
    def test_homepage_loads(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text='This app is for professionals who need ')


class Txt2CoordinatesTest(TestCase):

    def test_basic_import(self):
        f, log = txt2coordinates('web/fixtures/basic.csv')
        print(f)
        print(log)

        self.assertEqual(log[0], 'Processing: 25 lines')
        self.assertEqual(log[1], 'Skipped number of lines: 17')
        self.assertEqual(log[2], 'Final number of lines: 7')
