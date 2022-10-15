from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from web.utils import txt2coordinates
from web.utils_functions import is_it_a_header


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
        """
        We are running tests for filtering data, that does not have a z coordinate.
        """
        f, log = txt2coordinates('web/fixtures/basic.csv')
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

        self.assertIn('Processing: 24 lines', log)
        self.assertIn('Skipped number of lines: 17', log)
        self.assertIn('Final number of lines: 7', log)

    def test_basic_b_first_line_missing(self):
        """
        We test what happens if the name of the columns is missing 'Position x, Position y, height...'
        It should start with the list position 0, instead of 1.
        """
        f, log = txt2coordinates('web/fixtures/basic_b_first_line_missing.csv')
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

        self.assertIn('Processing: 24 lines', log)
        self.assertIn('Skipped number of lines: 17', log)
        self.assertIn('Final number of lines: 7', log)

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

        self.assertIn('Processing: 24 lines', log)
        self.assertIn('Skipped number of lines: 17', log)
        self.assertIn('Final number of lines: 7', log)

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

        self.assertIn('Processing: 24 lines', log)
        self.assertIn('Skipped number of lines: 17', log)
        self.assertIn('Final number of lines: 7', log)

    def test_basic_b_xzy(self):
        """
        We are testing if that app recognizes that the z coordinates in the y position and it corrects it.
        This '457000,300,320000' should look like '457000,320000,300'.
        """
        f, log = txt2coordinates('web/fixtures/basic_b_xzy.csv')
        print(f)
        print(log)

        self.assertIn('Processing: 24 lines', log)
        self.assertIn('Skipped number of lines: 17', log)
        self.assertIn('Final number of lines: 7', log)

    def test_basic_b_z_is_null(self):
        """
        We are testing if the code excludes the null values '0.00', '0' with the ''string for z.
        """
        f, log = txt2coordinates('web/fixtures/basic_b_z_is_null.csv')
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

        self.assertIn('Processing: 24 lines', log)
        self.assertIn('Skipped number of lines: 17', log)
        self.assertIn('Final number of lines: 7', log)

    def test_basic_b_z_is_wrongfloat(self):
        f, log = txt2coordinates('web/fixtures/basic_b_z_is_wrongfloat.csv')
        print(f)
        print(log)

        self.assertIn('Processing: 24 lines', log)
        self.assertIn('Skipped number of lines: 17', log)
        self.assertIn('Final number of lines: 7', log)

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

        self.assertIn('Processing: 24 lines', log)
        self.assertIn('Skipped number of lines: 17', log)
        self.assertIn('Final number of lines: 7', log)


class HeaderTests(TestCase):
    def test_is_it_a_header(self):
        """
        Trying to see if it knows that the first line is made of text or floats.
        It should recognize that 'Position x, position y, position z' is a header.
        """

        answer = is_it_a_header(['Position x', 'Position z', 'a'])
        answer1 = is_it_a_header(['1', 'a', '3'])
        answer2 = is_it_a_header(['1', '2', '3'])
        self.assertTrue(answer)
        self.assertTrue(answer1)
        self.assertFalse(answer2)

