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
from OR.IDAdminLocators import IDAdminLocators

class commonactions(unittest.TestCase):
    
    
    driver=webdriverenhancement.driver
        
    def LogintoAdmin(self):
        
        self.driver.get("http://id/admin")
        self.driver.maximize_window()
        
#         if(BaseWrappers.WebdriverHelper.webdriverenhancement.isElementPresent("//div[@id='userDisplay']/a[.='Logout']")):
#             self.driver.find_element_by_xpath("//div[@id='userDisplay']/a[.='Logout']").click()
#             self.driver.switch_to_alert(self).accept()
#         else:
        time.sleep(5)
        self.driver.find_element_by_xpath(IDAdminLocators.Adminusername(self)).send_keys("superuser")
        
        time.sleep(5)
        
        self.driver.find_element_by_xpath(IDAdminLocators.Adminpassword(self)).send_keys("dashboard")
        
        time.sleep(5)
        
        self.driver.find_element_by_xpath(IDAdminLocators.AdminLoginButton(self)).click()
    def LogOutFromAdmin(self):
        self.driver.switch_to_default_content() 
        self.driver.switch_to_frame(self.driver.find_element_by_id("header"))
        
        time.sleep(2)
        
        self.driver.find_element_by_xpath(IDAdminLocators.LogOutLink(self)).click()
        
        time.sleep(2)
        
        self.driver.switch_to_alert().accept()
        
        time.sleep(2)
        
        
    def LoginToFE(self):
        self.driver.get("http://id/home")
        
        
        
        
     
    
        
        
        
        
        
        
        