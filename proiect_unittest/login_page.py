from proiect_unittest.home_page_medtinker import HomeMedtinkerChrome
from proiect_unittest.locators_medtinker import LocatorsLoginPage


class LoginPage(HomeMedtinkerChrome):
    # test1 - intram pe site, indetificam elementele de tip user si parola si inseram valori incorecte. Apoi dam click
    # pe butonul 'autentificare' si verificam ca: se returneaza eroarea corecta
    def test_8_logare_cu_valori_incorecte(self):
        self.driver.find_element(*LocatorsLoginPage.EMAIL).send_keys('invalid_email@gmail.com')
        self.driver.find_element(*LocatorsLoginPage.PASSWORD).send_keys('david12345')
        self.driver.find_element(*LocatorsLoginPage.AUTENTIFICARE).click()
        self.assertEqual(self.driver.find_element(*LocatorsLoginPage.MESAJ_ERROR_LOGIN).
                         text, 'Nu ai introdus o parolă corectă!')

    def test_9_logare_cu_valori_corecte(self):
        self.driver.find_element(*LocatorsLoginPage.EMAIL).send_keys('godavid128@gmail.com')
        self.driver.find_element(*LocatorsLoginPage.PASSWORD).send_keys('david12345')
        self.driver.find_element(*LocatorsLoginPage.AUTENTIFICARE).click()
        self.driver.find_element(*LocatorsLoginPage.MESAJ_BUN_VENIT).is_displayed()

