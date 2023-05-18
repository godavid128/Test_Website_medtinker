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
    CONTACT_PRENUME = (By.XPATH, '//*[@id="form-field-email"]')
    CONTACT_NUME = (By.XPATH, '//*[@id="form-field-nume"]')
    CONTACT_EMAIL = (By.XPATH, '//*[@id="form-field-field_1e18343"]')
    CONTACT_MESAJ = (By.XPATH, '//*[@id="form-field-field_6ba0b23"]')
    CONTACT_BIFARE_TERM_COND = (By.XPATH, '//*[@id="form-field-field_4a9f4e2"]')
    CONTACT_BIFARE_ACORD_PRIMIRE_EMAIL = (By.XPATH, '//input[@id="form-field-field_c3b66b8"]')
    TRIMITE_MESAJ = (By.CLASS_NAME, 'elementor-button-text')
    MESAJ_TRIMIS_CU_SUCCCES = (By.XPATH, '//*[@id="post-2750"]/div/div/section/div/div/div/div[3]/div/form/div[2]')


class LocatorsCreareCont:
    SIGNUP_PAGE = (By.XPATH, '//a[contains(text(),"Creează Cont")]')
    PRENUME = (By.XPATH, '//input[@placeholder="Care este prenumele tău?"]')
    NUME = (By.XPATH, '//input[@placeholder="Care este numele tău?"]')
    USERNAME = (By.XPATH, '//input[@placeholder="Alege username-ul dorit..."]')
    EMAIL_CREARE_CONT = (By.XPATH, '//input[@placeholder="Scrie adresa ta de email principală..."]')
    PWD_CREARE_CONT = (By.XPATH, '//input[@placeholder="Alege o parolă sigură..."]')
    BIFARE_TERMENI_CONDITII = (By.XPATH, '//span[@class="checkbox-label"]')
    INREGISTRARE_CONT = (By.XPATH, '//span[@class="elementor-button-text uael-registration-submit"]')
    MESAJ_ERROR_INREGISTRARE_1 = (By.XPATH, '//span[contains(text(),"Enter valid Email!")]')
    MESAJ_ERROR_INREGISTRARE_2 = (By.XPATH, '//span[contains(text(),"This Field is required!")]')
    MESAJ_ERROR_INREGISTRARE_3 = (By.XPATH, '//span[@class="uael-register-error"]')
    MESAJ_ERROR_INREGISTRARE_4 = (By.XPATH, '//span[@class="uael-register-error"][normalize-space()="This username is '
                                            'already registered. Please choose another one."]')
    MESAJ_ERROR_INREGISTRARE_5 = (By.XPATH, '//span[@class="uael-register-error"][normalize-space()="An account is '
                                            'already registered with your email address. Please choose another one."]')


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
