'''
Pentru inceput vom instala libraria selenium. In Terminal scriem: pip install webdriver-manager si pip install selenium
Daca nu reusim sa instalam, intram la Python Packages si scriem in bara de cautare: webdriver-menager si selenium.
'''
from selenium.webdriver.common.by import By


class LocatorsHomeMedTinker:
    ACCEPT_COOKIES = (By.XPATH, '//*[@id="BorlabsCookieBox"]/div/div/div/div[1]/div/div/div/p[2]/a')


class LocatorsLoginPage:
    # locators login
    EMAIL = (By.ID, 'eael-user-login')
    PASSWORD = (By.ID, 'eael-user-password')
    AUTENTIFICARE = (By.ID, 'eael-login-submit')
    MESAJ_ERROR_LOGIN = (By.CLASS_NAME, 'eael-form-validation-container')
    MESAJ_BUN_VENIT = (By.XPATH, '//*[@id="gamipress-rank-2376"]/div[2]/div/p[1]')


class LocatorsInregistrare:
    INREGISTRARE_PAGINA = (By.XPATH, '//*[@id="menu-item-18379"]/a/span')
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


class LocatorsCeMerita:
    CE_MERITA_PAGE = (By.XPATH, '//*[@id="menu-item-18453"]/a/i')
    CUM_TE_CHEAMA = (By.XPATH, '//*[@id="form-field-nume"]')
    ADRESA_EMAIL = (By.XPATH, '//form[@name="Ce Merita"]//input[@id="form-field-email"]')
    BIFARE_TERM_COND_CE_MERITA = (By.XPATH, '//*[@id="form-field-field_431ec8f"]')
    BIFARE_ACORD_NEWSLETTER = (By.XPATH, '//*[@id="form-field-field_b42d63b"]')
    CLICK_VREAU_SA_AFLU_CE_MERITA = (By.XPATH, '//*[@id="ce-merita"]/div/form/div[1]/div[6]/button/span/span[2]')
    MESAJ_DE_SUCCESS = (By.XPATH, '//span[normalize-space()="Gata! Primul e-mail e deja pe drum."]')
    # MESAJ_DE_SUCCESS = (By.XPATH, '//*[@id="ce-merita"]/div/form/div[2]')
    # CLICK_PE_PAGINA = (By.XPATH, '//*[@id="post-2053"]/div/div/section[2]')


class LocatorsContact:
    CONTACT_PAGE = (By.XPATH, '//*[@id="menu-item-738"]/a')
    CONTACT_PRENUME = (By.XPATH, '//*[@id="form-field-email"]')
    CONTACT_NUME = (By.XPATH, '//*[@id="form-field-nume"]')
    CONTACT_EMAIL = (By.XPATH, '//*[@id="form-field-field_1e18343"]')
    CONTACT_MESAJ = (By.XPATH, '//*[@id="form-field-field_6ba0b23"]')
    CONTACT_BIFARE_TERM_COND = (By.XPATH, '//*[@id="form-field-field_4a9f4e2"]')
    CONTACT_BIFARE_ACORD_PRIMIRE_EMAIL = (By.XPATH, '//input[@id="form-field-field_c3b66b8"]')

    TRIMITE_MESAJ = (By.CLASS_NAME, 'elementor-button-text')
    MESAJ_TRIMIS_CU_SUCCCES = (By.XPATH, '//*[@id="post-2750"]/div/div/section/div/div/div/div[3]/div/form/div[2]')


class LocatorsSearch:
    SEARCH_BARRE = (By.XPATH, '//*[@id="masthead"]/div[1]/div[2]/div/form/label/input')
    CLICK_BARRE_SEARCH = (By.XPATH,
                          '//div[@class="header-search-wrap header-search-primary"]//input[@placeholder="Caută..."]')
    MESSAGE_ERROR_FIND = (By.XPATH, '//p[contains(text(),"Îmi pare rău, nu am găsit rezultate.")]')
    RESULTS_NUMBER = (By.XPATH, '//*[@id="buddypress"]/div/div/nav/ul/li[2]/a/span')
    TITLUL_PRODUSE = (By.CLASS_NAME, 'entry-content entry-summary')
