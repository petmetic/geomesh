from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from web.utils import txt2coordinates


class IndexTest(TestCase):
    def test_homepage_loads(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text='This app is for professionals who need')

    def test_submit_file(self):
        csv_file = SimpleUploadedFile("text.csv", open('web/fixtures/basic_b.txt', 'rb+').read())
        response = self.client.post('/', {'input_file': csv_file})
        self.assertEqual(response.status_code, 302)

        report_page_response = self.client.get(response.url)
        self.assertEqual(report_page_response.status_code, 200)
        self.assertContains(report_page_response, "Here is your report")
        self.assertContains(report_page_response, 'Processing: 25 lines')


class Txt2CoordinatesTest(TestCase):

    def test_basic_import(self):
        f, log = txt2coordinates('web/fixtures/basic.csv')
        print(f)
        print(log)

        self.assertEqual(log[0], 'Processing: 25 lines')
        self.assertEqual(log[1], 'Skipped number of lines: 17')
        self.assertEqual(log[2], 'Final number of lines: 7')

    def test_basic_b_first_line_missing(self):
        f, log = txt2coordinates('web/fixtures/basic_b_first_line_missing.csv')
        print(f)
        print(log)

        self.assertEqual(log[0], 'Processing: 25 lines')
        self.assertEqual(log[1], 'Skipped number of lines: 17')
        self.assertEqual(log[2], 'Final number of lines: 7')

    def test_basic_b_txt(self):
        f, log = txt2coordinates('web/fixtures/basic_b.txt')
        print(f)
        print(log)

        self.assertEqual(log[0], 'Processing: 25 lines')
        self.assertEqual(log[1], 'Skipped number of lines: 17')
        self.assertEqual(log[2], 'Final number of lines: 7')

    def test_basic_b_int(self):
        f, log = txt2coordinates('web/fixtures/basic_b_int.csv')
        print(f)
        print(log)

        self.assertEqual(log[0], 'Processing: 25 lines')
        self.assertEqual(log[1], 'Skipped number of lines: 17')
        self.assertEqual(log[2], 'Final number of lines: 7')

    def test_basic_b_xyzz1(self):
        """
        napisi kaj test testira: napises kaksni bi morali
        biti rezultati in toliko casa popravljas dolker ne dobis pravilnega rezultata
        """
        f, log = txt2coordinates('web/fixtures/basic_b_xyzz1.csv')
        print(f)
        print(log)

        output_txt = f.read().splitlines()
        self.assertEqual(output_txt[0], '414236.6700,127085.7100,525.86')
        self.assertEqual(output_txt[1], '414236.6800,127045.4700,529.03')

        self.assertEqual(log[0], 'Processing: 25 lines')
        self.assertEqual(log[1], 'Skipped number of lines: 17')
        self.assertEqual(log[2], 'Final number of lines: 7')
