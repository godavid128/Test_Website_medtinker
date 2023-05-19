'''
TEST PAGINA: ‘CREARE CONT’
Intram pe site, facem click pe creare cont, si indetificam elementele de tip prenume, nume, username, email, parola,
casuta termeni si conditi; si inseram valori.
Testul 4 – Inseram valori corecte, dar in casuta email punem un email fara arond. Apoi dam click
pe butonul 'inregistrare' si verificam ca: se returneaza eroarea corecta
Testul 5 – Inseram valori corecte, insa elementul parola lasam gol si verificam daca avem mesajul de eroare corect.
Testul 6 – In acest test vrem sa ne inregistram fara a accepta conditiile de inregistrare si verificam
daca este afisat mesajul de eroare.
Testul 7 – In acest test verificam daca putem sa ne inregistram cu un cont valid deja existent.
Trebuie sa gasim mesajele de eroare, precum ca: ‘username este deja folosit’ si ‘un cont cu email-ul dat este existent,
incercati cu alt email’.
Testele = PASS
'''
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from proiect_unittest.home_page_medtinker import HomeMedtinkerChrome
from proiect_unittest.locators_medtinker import LocatorsCreareCont


class CreareContPage(HomeMedtinkerChrome):
    def test_4_creare_cont_cu_email_fara_arond(self):
        self.driver.find_element(*LocatorsCreareCont.SIGNUP_PAGE).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(*LocatorsCreareCont.PRENUME).send_keys('david')
        self.driver.find_element(*LocatorsCreareCont.NUME).send_keys('go')
        self.driver.find_element(*LocatorsCreareCont.USERNAME).send_keys('godavid128')
        self.driver.find_element(*LocatorsCreareCont.EMAIL_CREARE_CONT).send_keys('godavid128gmail.com')
        self.driver.find_element(*LocatorsCreareCont.PWD_CREARE_CONT).send_keys('david12345')
        self.driver.find_element(*LocatorsCreareCont.BIFARE_TERMENI_CONDITII).click()
        self.driver.find_element(*LocatorsCreareCont.INREGISTRARE_CONT).click()
        time.sleep(3)
        self.assertEqual(self.driver.find_element(*LocatorsCreareCont.MESAJ_ERROR_INREGISTRARE_1).
                         text, 'Enter valid Email!')

    def test_5_creare_cont_fara_parola(self):
        self.driver.find_element(*LocatorsCreareCont.SIGNUP_PAGE).click()
        self.driver.find_element(*LocatorsCreareCont.PRENUME).send_keys('ion')
        self.driver.find_element(*LocatorsCreareCont.NUME).send_keys('popescu')
        self.driver.find_element(*LocatorsCreareCont.USERNAME).send_keys('pescuitorul')
        self.driver.find_element(*LocatorsCreareCont.EMAIL_CREARE_CONT).send_keys('pescuitorul@gmail.com')
        self.driver.find_element(*LocatorsCreareCont.BIFARE_TERMENI_CONDITII).click()
        self.driver.find_element(*LocatorsCreareCont.INREGISTRARE_CONT).click()
        time.sleep(3)
        self.assertEqual(self.driver.find_element(*LocatorsCreareCont.MESAJ_ERROR_INREGISTRARE_2).
                         text, 'This Field is required!')

    def test_6_creare_cont_fara_acceptare_conditii(self):
        self.driver.find_element(*LocatorsCreareCont.SIGNUP_PAGE).click()
        self.driver.find_element(*LocatorsCreareCont.PRENUME).send_keys('david')
        self.driver.find_element(*LocatorsCreareCont.NUME).send_keys('go')
        self.driver.find_element(*LocatorsCreareCont.USERNAME).send_keys('godavid128')
        self.driver.find_element(*LocatorsCreareCont.EMAIL_CREARE_CONT).send_keys('godavid128@gmail.com')
        self.driver.find_element(*LocatorsCreareCont.PWD_CREARE_CONT).send_keys('david12345')
        self.driver.find_element(*LocatorsCreareCont.INREGISTRARE_CONT).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LocatorsCreareCont.MESAJ_ERROR_INREGISTRARE_3))
        self.assertEqual(self.driver.find_element(*LocatorsCreareCont.MESAJ_ERROR_INREGISTRARE_3).
                         text, 'Please accept the Terms and Conditions to proceed.')

    def test_7_creare_cont_valid_deja_existent(self):
        self.driver.find_element(*LocatorsCreareCont.SIGNUP_PAGE).click()
        self.driver.find_element(*LocatorsCreareCont.PRENUME).send_keys('david')
        self.driver.find_element(*LocatorsCreareCont.NUME).send_keys('go')
        self.driver.find_element(*LocatorsCreareCont.USERNAME).send_keys('godavid128')
        self.driver.find_element(*LocatorsCreareCont.EMAIL_CREARE_CONT).send_keys('godavid128@gmail.com')
        self.driver.find_element(*LocatorsCreareCont.PWD_CREARE_CONT).send_keys('david12345')
        self.driver.find_element(*LocatorsCreareCont.BIFARE_TERMENI_CONDITII).click()
        self.driver.find_element(*LocatorsCreareCont.INREGISTRARE_CONT).click()
        time.sleep(3)
        self.assertEqual(self.driver.find_element(*LocatorsCreareCont.MESAJ_ERROR_INREGISTRARE_4).
                         text, 'This username is already registered. Please choose another one.')
        time.sleep(3)
        self.assertEqual(self.driver.find_element(*LocatorsCreareCont.MESAJ_ERROR_INREGISTRARE_5).
                         text, 'An account is already registered with your email address. Please choose another one.')
