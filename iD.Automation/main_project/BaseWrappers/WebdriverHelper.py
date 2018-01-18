'''
Created on 22-Jun-2017

@author: Sumedh.Tambe
'''
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

class webdriverenhancement():

        driver=webdriver.Firefox()
        
        def isElementPresent(self,locator):
            try:
                self.driver.find_element_by_xpath(locator)
            except NoSuchElementException:
                print("return false")
                return False
            return True