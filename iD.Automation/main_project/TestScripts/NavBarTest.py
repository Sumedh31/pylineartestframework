'''
Created on 29-Jun-2017

@author: Sumedh.Tambe
'''
import unittest
from AppModule.commonactions import commonactions
from selenium import webdriver
from BaseWrappers.WebdriverHelper import webdriverenhancement
from Library import Navbartestobjects




class Test(unittest.TestCase):

    driver=webdriverenhancement.driver
    
    def setUp(self):
        print("opening URL") 
        
    def tearDown(self):
        print("Closing URL")
        self.driver.quit()


    def test_NavBar(self):
        commonactions.LogintoAdmin(self)
        Navbartestobjects.NavBarTestObjects.NavigateToNavBar(self)
        Navbartestobjects.NavBarTestObjects.AddNavBar(self)
        commonactions.LogOutFromAdmin(self)
        commonactions.LoginToFE(self)
        Navbartestobjects.NavBarTestObjects.VerifyNavIsAddedOnFE(self)
if __name__ == "__main__":
    unittest.main()
   
        


