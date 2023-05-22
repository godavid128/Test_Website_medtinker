'''
TEST PAGINA: ‘CONTACT’
Testul 3 – In acest test incercam sa observam, daca elementele de contact sunt accesibile si se poate trimite
un mesaj cu succes.
Testul = PASS
'''
from proiect_unittest.home_page_medtinker import HomeMedtinkerChrome
from proiect_unittest.locators_medtinker import LocatorsContact


class ContactPage(HomeMedtinkerChrome):
    def test_3_trimite_mesaj(self):
        self.driver.find_element(*LocatorsContact.CONTACT_PAGE).click()
        self.driver.find_element(*LocatorsContact.CONTACT_NUME).send_keys('david')
        self.driver.find_element(*LocatorsContact.CONTACT_EMAIL).send_keys('godavid128@gmail.com')
        self.driver.find_element(*LocatorsContact.ALEGE_SUBIECT).click()
        self.driver.find_element(*LocatorsContact.SUBIECT_ALES).click()
        self.driver.find_element(*LocatorsContact.CONTACT_MESAJ).send_keys('Am gasit un bug la pagina "ce merita"')
        self.driver.find_element(*LocatorsContact.CONTACT_BIFARE_TERM_COND).click()
        self.driver.find_element(*LocatorsContact.CONTACT_BIFARE_ACORD_PRIMIRE_EMAIL).click()
        self.driver.find_element(*LocatorsContact.TRIMITE_MESAJ).click()
        self.assertEqual(self.driver.find_element(*LocatorsContact.MESAJ_TRIMIS_CU_SUCCCES).
                         text, 'Mulțumim pentru mesaj. Te vom contacta cât de curând posibil.')
