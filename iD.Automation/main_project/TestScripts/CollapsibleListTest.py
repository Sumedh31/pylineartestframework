'''
Created on 26-Jun-2017

@author: Sumedh.Tambe

'''

import unittest
import pypyodbc
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver import ActionChains
from OR import CollapsibleLocators
from BaseWrappers.WebdriverHelper import webdriverenhancement
from Library import CollapsibleListObject
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

class CollapsibleList(unittest.TestCase):


    def setUp(self):
        print("opening URL") 
        #self.driver=webdriver.Firefox()


    def tearDown(self):
        print("Closing URL")
        #self.driver.quit()
    
    def test_collapsiblelist(self):
        #testobject=CollapsibleListObject.CollapsibleListPage()
        #self.driver=webdriver.Firefox()
        connection_string="DB_CONNECTION_STRING' value='Data Source='ADBIN0161\SQL2016';Initial Catalog='id-project/FrontendRedo';User Id='sa';Password='Cambo123';"
        connection=pypyodbc.connect(connection_string)
        SQL="Update tblDB_NV_NavBar Set [Name]='Company third' Where [Name]='Nav Item 3' "
        cur=connection.cursor()
        cur.execute(SQL)
        cur.commit()
        cur.close()
        connection.close()
        
    