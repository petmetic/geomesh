from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from .utils import txt2coordinates


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
        self.assertEqual(log[1], 'Skipped number of lines: 18')
        self.assertEqual(log[2], 'Final number of lines: 7')

    def test_basic_b_first_line_missing(self):
        """

        """
        f, log = txt2coordinates('web/fixtures/basic_b_first_line_missing.csv')
        print(f)
        print(log)

        self.assertEqual(log[0], 'Processing: 25 lines')
        self.assertEqual(log[1], 'Skipped number of lines: 18')
        self.assertEqual(log[2], 'Final number of lines: 7')

    def test_basic_b_txt(self):
        """
        We are testing if an input file .txt can be processed the same as a csv. file.
        The data should be filtered the same as the basic file.
        """
        f, log = txt2coordinates('web/fixtures/basic_b.txt')
        print(f)
        print(log)

        output_txt = f.read().splitlines()
        self.assertEqual(output_txt[0], '414236.6700,127085.7100,525.86')
        self.assertEqual(output_txt[1], '414236.6800,127045.4700,529.03')
        self.assertEqual(output_txt[2], '414236.9900,127036.1400,526.95')
        self.assertEqual(output_txt[3], '414238.0200,127055.5300,528.96')
        self.assertEqual(output_txt[4], '414238.3400,127027.1500,527.02')
        self.assertEqual(output_txt[5], '414238.3800,127081.3700,526.54')
        self.assertEqual(output_txt[6], '414238.4700,127058.8600,528.45')

        self.assertEqual(log[0], 'Processing: 25 lines')
        self.assertEqual(log[1], 'Skipped number of lines: 18')
        self.assertEqual(log[2], 'Final number of lines: 7')

    def test_basic_b_int(self):
        """
        We are testing what happens when there is an 'none elevation number' in the data.
        This '414236.9900,127036.1400,475858'should be skipped.
        """
        f, log = txt2coordinates('web/fixtures/basic_b_int.csv')
        print(f)
        print(log)

        output_txt = f.read().splitlines()
        self.assertEqual(output_txt[0], '414236.6700,127085.7100,525.86')
        self.assertEqual(output_txt[1], '414236.6800,127045.4700,529.03')
        self.assertEqual(output_txt[2], '414236.9900,127036.1400,526.95')
        self.assertEqual(output_txt[3], '414238.0200,127055.5300,528.96')
        self.assertEqual(output_txt[4], '414238.3400,127027.1500,527.02')
        self.assertEqual(output_txt[5], '414238.3800,127081.3700,526.54')
        self.assertEqual(output_txt[6], '414238.4700,127058.8600,528.45')

        self.assertEqual(log[0], 'Processing: 25 lines')
        self.assertEqual(log[1], 'Skipped number of lines: 18')
        self.assertEqual(log[2], 'Final number of lines: 7')

    def test_basic_b_xzy(self):
        f, log = txt2coordinates('web/fixtures/basic_b_xzy.csv')
        print(f)
        print(log)

        self.assertEqual(log[0], 'Processing: 25 lines')
        self.assertEqual(log[1], 'Skipped number of lines: 18')
        self.assertEqual(log[2], 'Final number of lines: 7')

    def test_basic_b_z_is_null(self):
        f, log = txt2coordinates('web/fixtures/basic_b_z_is_null.csv')
        print(f)
        print(log)

        self.assertEqual(log[0], 'Processing: 25 lines')
        self.assertEqual(log[1], 'Skipped number of lines: 18')
        self.assertEqual(log[2], 'Final number of lines: 7')

    def test_basic_b_z_is_wrongfloat(self):
        f, log = txt2coordinates('web/fixtures/basic_b_z_is_wrongfloat.csv')
        print(f)
        print(log)

        self.assertEqual(log[0], 'Processing: 25 lines')
        self.assertEqual(log[1], 'Skipped number of lines: 18')
        self.assertEqual(log[2], 'Final number of lines: 7')

    def test_basic_b_xyzz1(self):
        """
        We are testing if there are Z coordinates that are  written in 2 spaces if you get the right result of xyz.
        the coordinates that look like: [20,15,0,5] or [20,15,,5] will look like [20,15,5]
        """
        f, log = txt2coordinates('web/fixtures/basic_b_xyzz1.csv')
        print(f)
        print(log)

        output_txt = f.read().splitlines()
        self.assertEqual(output_txt[0], '414236.6800,127045.4700,529.03')
        self.assertEqual(output_txt[1], '414236.6700,127085.7100,525.86')
        self.assertEqual(output_txt[2], '414236.9900,127036.1400,526.95')
        self.assertEqual(output_txt[3], '414238.0200,127055.5300,528.96')
        self.assertEqual(output_txt[4], '414238.3400,127027.1500,527.02')
        self.assertEqual(output_txt[5], '414238.3800,127081.3700,526.54')
        self.assertEqual(output_txt[6], '414238.4700,127058.8600,528.45')

        self.assertEqual(log[0], 'Processing: 25 lines')
        self.assertEqual(log[1], 'Skipped number of lines: 18')
        self.assertEqual(log[2], 'Final number of lines: 7')
