'''
TEST PAGINA: ‘CE MERITA’
Aici vom testa daca functioneaza optiunea de abonare la serviciile propuse de website.
Testul 1 –   Testam daca putem sa ne abonam cu email invalid.  Observam un bug: nu ar trebui sa se permita abonarea
cu un email invalid, si totusi, in loc sa intampinam un mesaj de eroare, primim mesajul de succes.
Testul 2 – Testam daca putem sa ne abonam cu email valid. Observam ca putem sa ne abonam, desi nu primim nici
un email cu confirmare, ceea ce ne duce la faptul ca exista o eroare intre comunicarea site-ului cu utilizatorul.
Testele = PASS
'''
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from proiect_unittest.home_page_medtinker import HomeMedtinkerChrome
from proiect_unittest.locators_medtinker import LocatorsCeMerita


class CeMeritaPage(HomeMedtinkerChrome):
    def test_1_abonare_la_ce_merita_cu_invalid_email(self):
        self.driver.find_element(*LocatorsCeMerita.RUBRICA_SOCIAL).click()
        self.driver.find_element(*LocatorsCeMerita.NEWSLETTER).click()
        self.driver.find_element(*LocatorsCeMerita.CE_MERITA_PAGE).click()
        self.assertEqual(self.driver.current_url, 'https://medtinker.ro/ce-merita/')
        self.driver.find_elements(*LocatorsCeMerita.CUM_TE_CHEAMA)[0].send_keys('Emil')
        self.driver.find_element(*LocatorsCeMerita.ADRESA_EMAIL).send_keys('invalid_email@gmail.com')
        self.driver.find_element(*LocatorsCeMerita.BIFARE_TERM_COND_CE_MERITA).click()
        self.driver.find_element(*LocatorsCeMerita.BIFARE_ACORD_NEWSLETTER).click()
        self.driver.find_element(*LocatorsCeMerita.CLICK_VREAU_SA_AFLU_CE_MERITA).click()
        time.sleep(3)
        mesaj_de_succes = self.driver.find_element(*LocatorsCeMerita.MESAJ_DE_SUCCESS).text
        self.assertEqual(mesaj_de_succes, 'Gata! Primul e-mail e deja pe drum.')
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LocatorsCeMerita.MESAJ_DE_SUCCESS))

    def test_2_abonare_la_ce_merita_cu_valid_email(self):
        self.driver.find_element(*LocatorsCeMerita.RUBRICA_SOCIAL).click()
        self.driver.find_element(*LocatorsCeMerita.NEWSLETTER).click()
        self.driver.find_element(*LocatorsCeMerita.CE_MERITA_PAGE).click()
        self.assertEqual(self.driver.current_url, 'https://medtinker.ro/ce-merita/')
        self.driver.find_elements(*LocatorsCeMerita.CUM_TE_CHEAMA)[0].send_keys('david')
        self.driver.find_element(*LocatorsCeMerita.ADRESA_EMAIL).send_keys('godavid128@gmail.com')
        self.driver.find_element(*LocatorsCeMerita.BIFARE_TERM_COND_CE_MERITA).click()
        self.driver.find_element(*LocatorsCeMerita.BIFARE_ACORD_NEWSLETTER).click()
        self.driver.find_element(*LocatorsCeMerita.CLICK_VREAU_SA_AFLU_CE_MERITA).click()
        time.sleep(3)
        mesaj_de_succes = self.driver.find_element(*LocatorsCeMerita.MESAJ_DE_SUCCESS).text
        self.assertEqual(mesaj_de_succes, 'Gata! Primul e-mail e deja pe drum.')
