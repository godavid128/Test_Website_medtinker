'''
TEST PAGINA: ‘LOGIN’
Testul 8 – Aici testam daca putem sa ne logam cu un email invalid. Asteptam ca sa intampinam mesajul de eroare corect
Testul 9 –Aici vrem sa testam daca ne putem loga cu toate valorile corecte si reusim sa intram pe pagina logata.
Testele = PASS
'''
from proiect_unittest.home_page_medtinker import HomeMedtinkerChrome
from proiect_unittest.locators_medtinker import LocatorsLogin


class LoginPage(HomeMedtinkerChrome):

    def test_8_logare_cu_valori_incorecte(self):
        self.driver.find_element(*LocatorsLogin.LOGIN_PAGE).click()
        self.driver.find_element(*LocatorsLogin.EMAIL).send_keys('invalid_email@gmail.com')
        self.driver.find_element(*LocatorsLogin.PASSWORD).send_keys('david12345')
        self.driver.find_element(*LocatorsLogin.SUBMIT).click()
        self.assertEqual(self.driver.find_element(*LocatorsLogin.MESAJ_ERROR_LOGIN).
                         text, 'ERROR: The username or password you entered is incorrect. Lost your password?')

    def test_9_logare_cu_valori_corecte(self):
        self.driver.find_element(*LocatorsLogin.LOGIN_PAGE).click()
        self.driver.find_element(*LocatorsLogin.EMAIL).send_keys('godavid128@gmail.com')
        self.driver.find_element(*LocatorsLogin.PASSWORD).send_keys('david12345')
        self.driver.find_element(*LocatorsLogin.SUBMIT).click()
        self.assertEqual(self.driver.current_url, 'https://medtinker.ro/hub/')
