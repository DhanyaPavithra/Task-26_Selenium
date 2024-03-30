# locator.py

from selenium.webdriver.common.by import By

class WebLocators:

    def __init__(self):
        self.expandAllLocatorXpath = '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button'
        self.inputBoxLocatorXpath = '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[1]/div[2]/div/div/div/div/div/div/input'
        self.dropDownBoxLocatorID = 'within-topic-dropdown-id'
        self.optionsLocatorXpath = '// *[ @ id = "accordion-item-pageTopicsAccordion"] / div / div / section / button[9]'
        self.resultLocatorXpath ='/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button'

