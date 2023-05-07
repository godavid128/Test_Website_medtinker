import time

from proiect_unittest.home_page_medtinker import HomeMedtinkerChrome
from proiect_unittest.locators_medtinker import LocatorsSearch


class SearchPage(HomeMedtinkerChrome):
    # test1 - intram pe site, indetificam elementele de tip user si parola si inseram valori incorecte. Apoi dam click
    # pe butonul 'autentificare' si verificam ca: se returneaza eroarea corecta
    def test_10_search_omida(self):
        self.driver.find_element(*LocatorsSearch.SEARCH_BARRE).send_keys('omida')
        self.driver.find_element(*LocatorsSearch.CLICK_BARRE_SEARCH).submit()
        time.sleep(3)
        self.assertEqual(self.driver.find_element(*LocatorsSearch.MESSAGE_ERROR_FIND).
                         text, 'Îmi pare rău, nu am găsit rezultate.')
        time.sleep(3)

    def test_11_search_analize(self):
        self.driver.find_element(*LocatorsSearch.SEARCH_BARRE).send_keys('analize')
        self.driver.find_element(*LocatorsSearch.CLICK_BARRE_SEARCH).submit()
        for i in range(len(LocatorsSearch.TITLUL_PRODUSE)):
            assert len(LocatorsSearch.TITLUL_PRODUSE) >= 2, 'Error'
        resultate = self.driver.find_element(*LocatorsSearch.RESULTS_NUMBER).click()
        if resultate == '4 results':
            print(resultate)
            pass
        else:
            f'error, rezultate sunt mai multe'
