'''
Instalam li
Adaugam toate clasele de test create intr-o suita de teste
Definim in aceasta suita raportul html
Rulam suita de teste si analizati rezultatele

'''
import unittest
import HtmlTestRunner

from proiect_unittest.ce_merita_page import CeMeritaPage
from proiect_unittest.contact_page import ContactPage
from proiect_unittest.creare_cont_page import CreareContPage
from proiect_unittest.login_page import LoginPage
from proiect_unittest.search_page import SearchPage


class MedtinkerTestSuite(unittest.TestCase):
    def test_suite_medtinker(self):
        smoke_test_med = unittest.TestSuite()
        smoke_test_med.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(CeMeritaPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContactPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(CreareContPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(LoginPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(SearchPage)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            report_title='report1', report_name='Smoke Test Medtinker', combine_reports=True
        )
        runner.run(smoke_test_med)
