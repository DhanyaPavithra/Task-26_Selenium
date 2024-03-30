# main.py
#importing Data and Locator files
from Data import data
from Locator import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# importing select:
from selenium.webdriver.support.ui import Select

# Importing Exceptions
from selenium.common.exceptions import *

class SearchIMDB:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(data.Webdata().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def quit(self):
        self.driver.quit()

    def searchInIMDB(self):

        try:
            self.driver.find_element(by=By.XPATH,value=locator.WebLocators().expandAllLocatorXpath).click()
            self.driver.find_element(by=By.XPATH,value=locator.WebLocators().inputBoxLocatorXpath).send_keys(data.Webdata().inputBoxData)
            dropdown_element = self.driver.find_element(by=By.ID, value=locator.WebLocators().dropDownBoxLocatorID)
            dropdown = Select(dropdown_element)
            dropdown.select_by_visible_text(data.Webdata().dropDownBoxData)
            self.driver.find_element(by=By.XPATH,value=locator.WebLocators().optionsLocatorXpath)
            self.driver.find_element(by=By.XPATH,value=locator.WebLocators().resultLocatorXpath).click()
            if self.driver.current_url == data.Webdata().resultURL:
                print("Search successfully completed")

        except NoSuchElementException as e:
            print(e)

        finally:
            self.quit()

obj = SearchIMDB()
obj.boot()
obj.searchInIMDB()





