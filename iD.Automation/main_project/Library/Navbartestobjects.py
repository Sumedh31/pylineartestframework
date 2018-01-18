'''
Created on 29-Jun-2017

@author: Sumedh.Tambe
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common import by
import BaseWrappers
from BaseWrappers.WebdriverHelper import webdriverenhancement
from OR.VerticalNavBarLocators import VerticalNavBarLocators
from xml.etree.ElementTree import iselement
from selenium.webdriver.support.select import Select
class NavBarTestObjects(object):
    
    driver=webdriverenhancement.driver
    
    def NavigateToNavBar(self):  
        
        
        self.driver.switch_to_default_content() 
        
        self.driver.switch_to_frame(self.driver.find_element_by_id("menu"))
        self.driver.find_element_by_xpath(VerticalNavBarLocators.ExpandHomeSite(self)).click()
        
        time.sleep(2)
        
        self.driver.find_element_by_xpath(VerticalNavBarLocators.ExpandNavEditor(self)).click()
        
    
    def AddNavBar(self):
        
        self.driver.find_element_by_xpath(VerticalNavBarLocators.EditNavBarInNavEditor(self)).click()
        time.sleep(3)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(self.driver.find_element_by_id("main"))
               
        self.driver.find_element_by_xpath(VerticalNavBarLocators.EditButtonOfFirstVerticalNav(self)).click()
        self.driver.find_element_by_xpath(VerticalNavBarLocators.NavItemtabInEditVerticalNav(self)).click()
        self.driver.find_element_by_xpath(VerticalNavBarLocators.AddNavIteminNav(self)).click()
        
        time.sleep(2)
        self.driver.find_element_by_xpath(VerticalNavBarLocators.NavItemName(self)).send_keys("Vertical Navigation First")
        time.sleep(3)
        self.driver.find_element_by_xpath(VerticalNavBarLocators.NavItemLink(self)).send_keys("https://github.com/casesandberg/react-color/")
        
        self.driver.find_element_by_xpath(VerticalNavBarLocators.EditNavOkButton(self)).click()
    
    def VerifyNavIsAddedOnFE(self):
        if(webdriverenhancement.isElementPresent(self,VerticalNavBarLocators.AddedNavItemOnFE(self))):
            
            self.driver.find_element_by_xpath(VerticalNavBarLocators.AddedNavItemOnFE(self)).click()
            time.sleep(10)
            self.driver.get("http://id/home")
            
                
            
            
        