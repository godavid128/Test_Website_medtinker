'''
Pentru inceput vom instala libraria selenium. In Terminal scriem: pip install webdriver-manager si pip install selenium
Daca nu reusim sa instalam, intram la Python Packages si scriem in bara de cautare: webdriver-menager si selenium.
'''
from selenium.webdriver.common.by import By

class LocatorsHomeMedTinker:
    ACCEPT_COOKIES = (By.XPATH, '//*[@id="BorlabsCookieBox"]/div/div/div/div[1]/div/div/div/p[2]/a')


class LocatorsCeMerita:
    RUBRICA_SOCIAL = (By.XPATH, '//*[@id="menu-item-23292"]/a/span')
    NEWSLETTER = (By.XPATH, '//*[@id="menu-item-23299"]/a/span')
    CE_MERITA_PAGE = (By.XPATH, '//*[@id="menu-item-23300"]/a/span')
    CUM_TE_CHEAMA = (By.XPATH, '//*[@id="form-field-nume"]')
    ADRESA_EMAIL = (By.XPATH, '//*[@id="form-field-email"]')
    BIFARE_TERM_COND_CE_MERITA = (By.XPATH, '//*[@id="form-field-field_431ec8f"]')
    BIFARE_ACORD_NEWSLETTER = (By.XPATH, '//*[@id="form-field-field_b42d63b"]')
    CLICK_VREAU_SA_AFLU_CE_MERITA = (By.XPATH, '//*[@id="ce-merita"]/div/form/div[1]/div[6]/button/span/span[2]')
    MESAJ_DE_SUCCESS = (By.XPATH, '//span[normalize-space()="Gata! Primul e-mail e deja pe drum."]')


class LocatorsContact:
    CONTACT_PAGE = (By.XPATH, '//*[@id="menu-item-23287"]/a/span')
    CONTACT_NUME = (By.XPATH, '//*[@id="ff_1_names_first_name_"]')
    CONTACT_EMAIL = (By.XPATH, '//*[@id="ff_1_email"]')
    ALEGE_SUBIECT = (By.XPATH, '//*[@id="ff_1_subject"]')
    SUBIECT_ALES = (By.XPATH, '//*[@id="ff_1_subject"]/option[3]')
    CONTACT_MESAJ = (By.XPATH, '//*[@id="ff_1_message"]')
    CONTACT_BIFARE_TERM_COND = (By.XPATH, '//*[@id="terms-n-condition_4029fa0c236f5a979f073a0f46083f50"]')
    CONTACT_BIFARE_ACORD_PRIMIRE_EMAIL = (By.XPATH, '//*[@id="gdpr-agreement_5025509a8316f47defcc616e613f3929"]')
    TRIMITE_MESAJ = (By.XPATH, '//*[@id="fluentform_1"]/fieldset/div[7]/button')
    MESAJ_TRIMIS_CU_SUCCCES = (By.XPATH, '//*[@id="fluentform_1_success"]/p')


class LocatorsCreareCont:
    SIGNUP_PAGE = (By.XPATH, '//a[contains(text(),"Creează Cont")]')
    PRENUME = (By.XPATH, '//*[@id="ff_4_names_first_name_"]')
    NUME = (By.XPATH, '//*[@id="ff_4_names_last_name_"]')
    USERNAME = (By.XPATH, '//*[@id="ff_4_username"]')
    EMAIL_CREARE_CONT = (By.XPATH, '//*[@id="ff_4_email"]')
    PWD_CREARE_CONT = (By.XPATH, '//*[@id="ff_4_password"]')
    BIFARE_TERMENI_CONDITII = (By.XPATH, '//*[@id="terms-n-condition_1002c79e3af021e57f67f421ec931146"]')
    BIFARE_ACCORD_DE_PRIMIRE_EMAIL = (By.XPATH, '//*[@id="gdpr-agreement_deb94ac07fe627afbb3249d371a35a0f"]')
    CREARE_CONT = (By.XPATH, '//*[@id="fluentform_4"]/fieldset/div[7]/button')
    MESAJ_ERROR_INREGISTRARE_1 = (By.XPATH, '//span[contains(text(),"Enter valid Email!")]')
    MESAJ_ERROR_INREGISTRARE_2 = (By.XPATH, '//div[@role="alert"]')
    MESAJ_ERROR_INREGISTRARE_3 = (By.XPATH, '//span[@class="error-text"]')


class LocatorsLogin:
    LOGIN_PAGE = (By.XPATH, '//a[contains(text(),"Intră în cont")]')
    EMAIL = (By.XPATH, '//*[@id="user_login"]')
    PASSWORD = (By.XPATH, '//*[@id="user_pass"]')
    SUBMIT = (By.XPATH, '//*[@id="wp-submit"]')
    MESAJ_ERROR_LOGIN = (By.XPATH, '//*[@id="login_error"]')


class LocatorsSearch:
    BUTTON_SEARCH = (By.XPATH, '//i[@class="bb-icon-l bb-icon-search"]')
    SEARCH_BARRE = (By.XPATH, '//*[@id="masthead"]/div[4]/div/form/label/input')
    MESSAGE_ERROR_FIND = (By.XPATH, '//p[contains(text(),"Îmi pare rău, nu am găsit rezultate.")]')
    TITLUL_PRODUSE = (By.CLASS_NAME, 'entry-content entry-summary')
