import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from proiect_unittest.home_page_medtinker import HomeMedtinkerChrome
from proiect_unittest.locators_medtinker import LocatorsInregistrare


class InregistrarePage(HomeMedtinkerChrome):
    # test1 - intram pe site, facem click pe inregistrare, si indetificam elementele de tip prenume, nume, username,
    # email, parola, casuta termeni si conditi; si inseram valori corecte, exceptie la email introducem email fara aron.
    # Apoi dam click pe butonul 'inregistrare' si verificam ca: se returneaza eroarea corecta
    def test_4_creare_cont_cu_email_fara_aron(self):
        self.driver.find_element(*LocatorsInregistrare.INREGISTRARE_PAGINA).click()
        self.driver.find_element(*LocatorsInregistrare.PRENUME).send_keys('david')
        self.driver.find_element(*LocatorsInregistrare.NUME).send_keys('go')
        self.driver.find_element(*LocatorsInregistrare.USERNAME).send_keys('godavid128')
        self.driver.find_element(*LocatorsInregistrare.EMAIL_CREARE_CONT).send_keys('godavid128gmail.com')
        self.driver.find_element(*LocatorsInregistrare.PWD_CREARE_CONT).send_keys('david12345')
        time.sleep(3)
        self.driver.find_element(*LocatorsInregistrare.BIFARE_TERMENI_CONDITII).click()
        time.sleep(3)
        self.driver.find_element(*LocatorsInregistrare.INREGISTRARE_CONT).click()
        time.sleep(3)
        self.assertEqual(self.driver.find_element(*LocatorsInregistrare.MESAJ_ERROR_INREGISTRARE_1).
                         text, 'Enter valid Email!')

    def test_5_creare_cont_fara_parola(self):
        self.driver.find_element(*LocatorsInregistrare.INREGISTRARE_PAGINA).click()
        self.driver.find_element(*LocatorsInregistrare.PRENUME).send_keys('ion')
        self.driver.find_element(*LocatorsInregistrare.NUME).send_keys('popescu')
        self.driver.find_element(*LocatorsInregistrare.USERNAME).send_keys('pescuitorul')
        self.driver.find_element(*LocatorsInregistrare.EMAIL_CREARE_CONT).send_keys('pescuitorul@gmail.com')
        time.sleep(3)
        self.driver.find_element(*LocatorsInregistrare.BIFARE_TERMENI_CONDITII).click()
        time.sleep(3)
        self.driver.find_element(*LocatorsInregistrare.INREGISTRARE_CONT).click()
        time.sleep(3)
        self.assertEqual(self.driver.find_element(*LocatorsInregistrare.MESAJ_ERROR_INREGISTRARE_2).
                         text, 'This Field is required!')
        time.sleep(3)

    def test_6_creare_cont_fara_acceptare_conditii(self):
        self.driver.find_element(*LocatorsInregistrare.INREGISTRARE_PAGINA).click()
        self.driver.find_element(*LocatorsInregistrare.PRENUME).send_keys('david')
        self.driver.find_element(*LocatorsInregistrare.NUME).send_keys('go')
        self.driver.find_element(*LocatorsInregistrare.USERNAME).send_keys('godavid128')
        self.driver.find_element(*LocatorsInregistrare.EMAIL_CREARE_CONT).send_keys('godavid128@gmail.com')
        self.driver.find_element(*LocatorsInregistrare.PWD_CREARE_CONT).send_keys('david12345')
        self.driver.find_element(*LocatorsInregistrare.INREGISTRARE_CONT).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LocatorsInregistrare.MESAJ_ERROR_INREGISTRARE_3))
        self.assertEqual(self.driver.find_element(*LocatorsInregistrare.MESAJ_ERROR_INREGISTRARE_3).
                         text, 'Please accept the Terms and Conditions to proceed.')
        time.sleep(3)

    def test_7_creare_cont_valid_deja_existent(self):
        self.driver.find_element(*LocatorsInregistrare.INREGISTRARE_PAGINA).click()
        self.driver.find_element(*LocatorsInregistrare.PRENUME).send_keys('david')
        self.driver.find_element(*LocatorsInregistrare.NUME).send_keys('go')
        self.driver.find_element(*LocatorsInregistrare.USERNAME).send_keys('godavid128')
        self.driver.find_element(*LocatorsInregistrare.EMAIL_CREARE_CONT).send_keys('godavid128@gmail.com')
        self.driver.find_element(*LocatorsInregistrare.PWD_CREARE_CONT).send_keys('david12345')
        self.driver.find_element(*LocatorsInregistrare.BIFARE_TERMENI_CONDITII).click()
        time.sleep(3)
        self.driver.find_element(*LocatorsInregistrare.INREGISTRARE_CONT).click()
        time.sleep(3)
        self.assertEqual(self.driver.find_element(*LocatorsInregistrare.MESAJ_ERROR_INREGISTRARE_4).
                         text, 'This username is already registered. Please choose another one.')
        time.sleep(3)
        self.assertEqual(self.driver.find_element(*LocatorsInregistrare.MESAJ_ERROR_INREGISTRARE_5).
                         text, 'An account is already registered with your email address. Please choose another one.')
        time.sleep(3)
