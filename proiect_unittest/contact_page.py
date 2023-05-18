import time
from proiect_unittest.home_page_medtinker import HomeMedtinkerChrome
from proiect_unittest.locators_medtinker import LocatorsContact


class ContactPage(HomeMedtinkerChrome):
    def test_3_trimite_mesaj(self):
        self.driver.find_element(*LocatorsContact.CONTACT_PAGE).click()
        self.driver.find_element(*LocatorsContact.CONTACT_PRENUME).send_keys('ion')
        self.driver.find_element(*LocatorsContact.CONTACT_NUME).send_keys('popescu')
        self.driver.find_element(*LocatorsContact.CONTACT_EMAIL).send_keys('ion@gmail.com')
        self.driver.find_element(*LocatorsContact.CONTACT_MESAJ).send_keys('Am reusit')
        self.driver.find_element(*LocatorsContact.CONTACT_BIFARE_TERM_COND).click()
        time.sleep(3)
        self.driver.find_element(*LocatorsContact.CONTACT_BIFARE_ACORD_PRIMIRE_EMAIL).click()
        self.driver.find_element(*LocatorsContact.TRIMITE_MESAJ).click()
        time.sleep(3)
        self.assertEqual(self.driver.find_element(*LocatorsContact.MESAJ_TRIMIS_CU_SUCCCES).
                         text, 'Gata treaba! Totul pare în regulă.')
        self.driver.implicitly_wait(5)
