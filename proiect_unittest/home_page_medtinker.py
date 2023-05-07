'''
Aici avem novoie sa importam libraria unittest
'''
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from proiect_unittest.locators_medtinker import LocatorsHomeMedTinker


class HomeMedtinkerChrome(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://medtinker.ro/')
        self.driver.implicitly_wait(2)
        try:
            # self.driver.find_element(self.accept_cookies).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                LocatorsHomeMedTinker.ACCEPT_COOKIES)).click()
        except:
            pass

    def tearDown(self) -> None:
        self.driver.quit()
