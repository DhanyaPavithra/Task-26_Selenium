
from Data import data
from Locator import locator
import main

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import pytest

class Test:

    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.quit()


    def searchResult(self,boot):
        self.driver.get(data.Webdata().url)
        main.SearchIMDB().searchInIMDB()
        assert self.driver.current_url == data.Webdata().resultURL
        print("Success")


