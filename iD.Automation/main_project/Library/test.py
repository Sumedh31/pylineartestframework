import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver import ActionChains
from OR import CollapsibleLocators
from BaseWrappers.WebdriverHelper import webdriverenhancement

class Test(unittest.TestCase):


    def setUp(self):
        print("opening URL") 
        self.driver=webdriver.Firefox()


    def tearDown(self):
        print("Closing URL")
        self.driver.quit()
    
    def isElementPresent(self,locator):
        try:
            self.driver.find_element_by_xpath(locator)
        except NoSuchElementException:
            print("return false")
            return False
        return True


    def testCollapsibleList(self):
        self.driver.get("http://id/home/?uiexamples=true")
        self.driver.maximize_window()
        time.sleep(5)
        
        self.driver.find_element_by_xpath(CollapsibleLocators.CollapsibleLocatorsTest.firstLocator(self)).click()
        time.sleep(3)
        
        self.driver.find_element_by_xpath("//div[@class='helpPageToggleContent']//div//span[@class=contains(text(),'View Properties')]").click()
        time.sleep(3)
        
        print("Test Case 1:Check if the props are present.")
        
        if(self.isElementPresent("//div[@class='helpPageToggleContent']//tbody//tr//td//div[.='collapseFrom']")):
            self.driver.find_element_by_xpath("//div[@class='helpPageToggleContent']//tbody//tr//td//div[.='collapseFrom']").click()
            time.sleep(1)
            print("collapseFrom prop is present in Collapsible List component")
        
        if(self.isElementPresent("//div[@class='helpPageToggleContent']//tbody//tr//td//div[.='dropdownProps']")):
            self.driver.find_element_by_xpath("//div[@class='helpPageToggleContent']//tbody//tr//td//div[.='dropdownProps']").click()
            time.sleep(1)
            print("dropdownProps prop is present in Collapsible List component")
            
        if(self.isElementPresent("//div[@class='helpPageToggleContent']//tbody//tr//td//div[.='dropdownTarget']")):
            self.driver.find_element_by_xpath("//div[@class='helpPageToggleContent']//tbody//tr//td//div[.='dropdownTarget']").click()
            time.sleep(1)
            print("dropdownTarget prop is present in Collapsible List component")
            
        if(self.isElementPresent("//div[@class='helpPageToggleContent']//tbody//tr//td//div[.='renderVisibleItem']")):
            self.driver.find_element_by_xpath("//div[@class='helpPageToggleContent']//tbody//tr//td//div[.='renderVisibleItem']").click()
            time.sleep(1)
            print("renderVisibleItem prop is present in Collapsible List component")
            
        if(self.isElementPresent("//div[@class='helpPageToggleContent']//tbody//tr//td//div[.='styleType']")):
            self.driver.find_element_by_xpath("//div[@class='helpPageToggleContent']//tbody//tr//td//div[.='styleType']").click()
            time.sleep(1)
            print("styleType prop is present in Collapsible List component")
            
        if(self.isElementPresent("//div[@class='helpPageToggleContent']//tbody//tr//td//div[.='visibleItemClassName']")):
            self.driver.find_element_by_xpath("//div[@class='helpPageToggleContent']//tbody//tr//td//div[.='visibleItemClassName']").click()
            #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            print("visibleItemClassName prop is present in Collapsible List component")
            
        if(self.isElementPresent("//div[@class='helpPageToggleContent']//tbody//tr//td//div[.='visibleItemCount']")):
            self.driver.find_element_by_xpath("//div[@class='helpPageToggleContent']//tbody//tr//td//div[.='visibleItemCount']").click()
            #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            print("visibleItemCount prop is present in Collapsible List component")
            
            
            
            
            
        #Lets Check if the examples and code snippet are working fine
        print("Test Case 2: Make sure Collapsible List, Visible Items, Collapse From and Chnage Style Type examples are present.")
        #Check example Collapsible List
        if(self.isElementPresent("//div[@class='componentSection']//div//h5[contains(text(),'Collapsible List')]")):
            self.driver.find_element_by_xpath("//div[@class='componentSection']//div//div[@class='helpPage']/div[@class='helpPageComponent']//span[@class='pt-breadcrumbs-collapsed']").click()
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        #Check code for Collapsible List
        if(self.isElementPresent("//div[@class='componentContent']//div[@class='componentSection']//div//h5[contains(text(),'Collapsible List')]//..//..//..//div[@class='helpPageToggleContent']//span[.='View Source']")):
            self.driver.find_element_by_xpath("//div[@class='componentContent']//div[@class='componentSection']//div//h5[contains(text(),'Collapsible List')]//..//..//..//div[@class='helpPageToggleContent']//span[.='View Source']").click()
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            if(self.isElementPresent("//div//h5[contains(text(),'Collapsible List')]//..//div[@class='helpPageToggleContent']//code")):
                print("Code snippet for Collapsible is present")
         
        #Check example for Visible Items       
        if(self.isElementPresent("//div[@class='helpPageComponent']//div[@class='pt-slider-track']")):
            self.driver.find_element_by_xpath("//div[@class='helpPageComponent']//div[@class='pt-slider-track']").click()
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        #Check code for Visible Items
        if(self.isElementPresent("//div//h6[contains(text(),' Visible Items ')]//..//div[@class='helpPageToggleContent']//span[.='View Source']")):
            self.driver.find_element_by_xpath("//div//h6[contains(text(),' Visible Items ')]//..//div[@class='helpPageToggleContent']//span[.='View Source']").click()
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            if(self.isElementPresent("//div//h6[contains(text(),' Visible Items ')]//..//div[@class='helpPageToggleContent']//code")):
                time.sleep(5)
                print("Code snippet for Visible Items is present")
                
        #Check example for Collapse from       
        if(self.isElementPresent("//h6[contains(text(),' Collapse From ')]//..//..//label[.='Start']")):
            self.driver.find_element_by_xpath("//label[.='End']").click()
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            self.driver.find_element_by_xpath("//label[.='Start']").click()
            
        #Check code for Collapse from
        if(self.isElementPresent("//label[.='Start']//..//..//..//div[@class='helpPageToggleContent']//span[contains(text(),'View Source')]")):
            self.driver.find_element_by_xpath("//label[.='Start']//..//..//..//div[@class='helpPageToggleContent']//span[contains(text(),'View Source')]").click()
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            if(self.isElementPresent("//label[.='Start']//..//..//..//div[@class='helpPageToggleContent']//code")):
                time.sleep(5)
                print("Code snippet for Collapse from is present")
                
        #Check example for Change StyleType       
        if(self.isElementPresent("//label[.='Standard']")):
            self.driver.find_element_by_xpath("//label[.='Breadcrumb']").click()
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(10)
            self.driver.find_element_by_xpath("//label[.='Standard']").click()
            time.sleep(3)
        #Check code for Change StyleType
        if(self.isElementPresent("//label[.='Standard']//..//..//..//div[@class='helpPageToggleContent']//span[contains(text(),'View Source')]")):
            self.driver.find_element_by_xpath("//label[.='Standard']//..//..//..//div[@class='helpPageToggleContent']//span[contains(text(),'View Source')]").click()
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            if(self.isElementPresent("//label[.='Standard']//..//..//..//div[@class='helpPageToggleContent']//code")):
                time.sleep(5)
                print("Code snippet for Collapse from is present")
            print("Test Case 2 executed succefully")
        else:
            print("Test case 2 failed")
        
        
        
        
        
        print("Test case 3: By default clicking on collapsible crumb icon 3 menu items should be opened from Start that is Dev & Test, iDCMS and Home respectively.")
        if(self.isElementPresent("//div[@class='helpPageComponent']//ul[@class='pt-collapse-list']//span[@class='pt-popover-target']")):
            self.driver.find_element_by_xpath("//div[@class='helpPageComponent']//ul[@class='pt-collapse-list']//span[@class='pt-popover-target']").click()
            time.sleep(3)
            #Check if all expected  menu items are present in the collapsioble list
            if(self.isElementPresent("//ul[@class='pt-menu']//li[1]//a[.='Dev & Test']") and self.isElementPresent("//ul[@class='pt-menu']//li[2][.='ID CMS']") and self.isElementPresent("//ul[@class='pt-menu']//li[3]//a[.='Home']") ):
                print("All, that is 3 menu items are present with the correct order and with Coolapse From set to **Start** and **style type** set to Standard. ")
                self.driver.find_element_by_xpath("//div[@class='helpPageComponent']//ul[@class='pt-collapse-list']//span[@class='pt-popover-target pt-popover-open']").click()
                
                time.sleep(2)
            else:
                print("Please review the test case manually.")
            if(self.isElementPresent("//ul[@class='pt-collapse-list']//li[2]//a[.='Dev Tools']") and self.isElementPresent("//ul[@class='pt-collapse-list']//li[3]//a[.='Style Guides']") and self.isElementPresent("//ul[@class='pt-collapse-list']//li[4]//a[.='FrontEnd Redo']")):
                print("Only 'Dev Tools', 'Style Guides' and 'FrontEnd Redo ' list items are visible in the collapsible list.")
                          
            # Check if drop down icon for menu is in the list format with other visible collapsible list items
            if(self.isElementPresent("//ul[@class='pt-collapse-list']//li[1]//span[@class='pt-popover-target']")):
                #Now check if the collapsible icon is at the first position since collapse from is selected as 'Start'
                if(self.isElementPresent("//ul[@class='pt-collapse-list']//li[1]//span[@class='pt-popover-target']")):
                    print("Collapsible icon is present at Top and in the List format with other visible items")
                else:
                    Exception
                    print("Collapsible icon is not at the Top hence fail the test case")
        
        
        
        
        
        print("Test Case 4:Make Sure Change Style Type has Standard Checked-->Drag the visible items slider to 1 then set Collapse from option to Start and click on bread crumb icon should open 5 menu items which are Style Guides, Dev Tools,Dev & Test, iDCMS and Home respectively.")
       
        if(self.isElementPresent("//div[@class='helpPageComponent']//div[@class='pt-slider']//div[@class='pt-slider-axis']")):
            move = ActionChains(self.driver)
            #Lets drag the slider to 1
            self.driver.find_element_by_xpath("//div//h6[contains(text(),' Visible Items ')]//..//div[@class='helpPageToggleContent']//span[.='View Source']").click()
            self.driver.find_element_by_xpath("//div//h6[contains(text(),' Visible Items ')]//..//div[@class='helpPageToggleContent']//span[.='View Source']").click()
            move.drag_and_drop(self.driver.find_element_by_xpath("//div[@class='helpPageComponent']//div[@class='pt-slider']//span[@class='pt-slider-handle']"), self.driver.find_element_by_xpath("//div[@class='helpPageComponent']//div[@class='pt-slider']//div[@class='pt-slider-axis']//div[contains(text(),'1')]")).perform()
            time.sleep(3)
            self.driver.find_element_by_xpath("//label[.='Start']").click()
            self.driver.find_element_by_xpath("//label[.='Standard']").click()
            self.driver.find_element_by_xpath("//div[@class='helpPageComponent']//ul[@class='pt-collapse-list']//span[@class='pt-popover-target']").click()
            time.sleep(3)
            #Check if all expected  menu items are present in the collapsioble list
            if(self.isElementPresent("//ul[@class='pt-menu']//li[1]//a[.='Style Guides']") and self.isElementPresent("//ul[@class='pt-menu']//li[2]//a[.='Dev Tools']") and self.isElementPresent("//ul[@class='pt-menu']//li[3]//a[.='Dev & Test']") and self.isElementPresent("//ul[@class='pt-menu']//li[4][.='ID CMS']") and self.isElementPresent("//ul[@class='pt-menu']//li[5]//a[.='Home']") ):
                print("All, that is 5 menu items are present with the correct order and with Coolapse From set to **Start** and **style type** set to Standard. ")
                self.driver.find_element_by_xpath("//div[@class='helpPageComponent']//ul[@class='pt-collapse-list']//span[@class='pt-popover-target pt-popover-open']").click()
                time.sleep(2)
            else:
                print("Please review the test case manually.")
            
            #Check only expected visible items are present.
            if(self.isElementPresent("//ul[@class='pt-collapse-list']//li[2]//a[.='FrontEnd Redo']")):
                print("Only 'FrontEnd Redo ' menu item is visible in the collapsible list.")
                          
            # Check if drop down icon for menu is in the list format with other visible collapsible list items
            if(self.isElementPresent("//ul[@class='pt-collapse-list']//li[1]//span[@class='pt-popover-target']")):
                #Now check if the collapsible icon is at the first position since collapse from is selected as 'Start'
                if(self.isElementPresent("//ul[@class='pt-collapse-list']//li[1]//span[@class='pt-popover-target']")):
                    print("Collapsible icon is present at Top and in the List format with other visible items")
                else:
                    Exception
                    print("Collapsible icon is not at the Top hence fail the test case")
            else:
                print("Test case 4 failed Collapsible icon is not in the List position even though StyleType is selected as Standard.")
            print("Test case 4 executed succefully.")
        else:
            print("Test case 4 failed")
        
        
        
        
        
        print("Test Case 5: Make Sure Change Style Type has BreadCrumb Checked -->Drag the visible items slider to 1 then set Collapse from option to Start and click on bread crumb icon should open 5 menu items which are Style Guides, Dev Tools,Dev & Test, iDCMS and Home respectively./n --> Make sure FronEnd Redo is inline to and after breadcrumb icon ")
        if(self.isElementPresent("//div[@class='helpPageComponent']//div[@class='pt-slider']//div[@class='pt-slider-axis']")):
            #move = ActionChains(self.driver)
            #Lets drag the slider to 1
            #move.drag_and_drop(self.driver.find_element_by_xpath("//div[@class='helpPageComponent']//div[@class='pt-slider']//span[@class='pt-slider-handle']"), self.driver.find_element_by_xpath("//div[@class='helpPageComponent']//div[@class='pt-slider']//div[@class='pt-slider-axis']//div[contains(text(),'1')]")).perform()
            #time.sleep(3)
            self.driver.find_element_by_xpath("//label[.='Start']").click()
            self.driver.find_element_by_xpath("//label[.='Breadcrumb']").click()
            self.driver.find_element_by_xpath("//div[@class='helpPageComponent']//ul[@class='pt-collapse-list pt-breadcrumbs']//span[@class='pt-popover-target']").click()
            time.sleep(3)
            #Check if all expected  menu items are present in the collapsioble list
            if(self.isElementPresent("//ul[@class='pt-menu']//li[1]//a[.='Style Guides']") and self.isElementPresent("//ul[@class='pt-menu']//li[2]//a[.='Dev Tools']") and self.isElementPresent("//ul[@class='pt-menu']//li[3]//a[.='Dev & Test']") and self.isElementPresent("//ul[@class='pt-menu']//li[4][.='ID CMS']") and self.isElementPresent("//ul[@class='pt-menu']//li[5]//a[.='Home']") ):
                print("All, that is 5 menu items are present with the correct order Coolapse From set to **Start** and **style type** set to Standard. ")
            else:
                print("Please review the test case manually.")
             
            #Check only expected visible items are present.
            if(self.isElementPresent("//ul[@class='pt-collapse-list pt-breadcrumbs']//li[2][.='FrontEnd Redo']")):
                print("Only 'FrontEnd Redo ' menu item is visible in the collapsible list.")
                           
            # Check if drop down icon for menu is in the list format with other visible collapsible list items
            if(self.isElementPresent("//ul[@class='pt-collapse-list pt-breadcrumbs']//li[1]//span[@class='pt-popover-target pt-popover-open']")):
                #Now check if the collapsible icon is at the first position since collapse from is selected as 'Start'
                if(self.isElementPresent("//ul[@class='pt-collapse-list pt-breadcrumbs']//li[1]//span[@class='pt-popover-target pt-popover-open']")):
                    print("Collapsible icon is present at Top and in the List format with other visible items")
                else:
                    Exception
                    print("Collapsible icon is not at the Top hence fail the test case")
            else:
                print("Collapsible icon is not in the List position even though StyleType is selected as Standard.")
            print("Test case 5 executed succefully.")
        else:
            print("Test case 5 failed")
        
        
        
        
        print("Test Case 6:Make sure Change Style Type to Breadcrumb -->Drag the visible items slider to 1 --> then set Collapse from option to End --> and click on bread crumb icon should open 5 menu items which are iDCMS,Dev & Test, Dev Tools, Style Guides and FrontEndRedo respectively. Also verify that collapsible icon is inline with  and after the visible items")
        if(self.isElementPresent("//div[@class='helpPageComponent']//div[@class='pt-slider']//div[@class='pt-slider-axis']")):
            #move = ActionChains(self.driver)
            #Lets drag the slider to 1
            #move.drag_and_drop(self.driver.find_element_by_xpath("//div[@class='helpPageComponent']//div[@class='pt-slider']//span[@class='pt-slider-handle']"), self.driver.find_element_by_xpath("//div[@class='helpPageComponent']//div[@class='pt-slider']//div[@class='pt-slider-axis']//div[contains(text(),'1')]")).perform()
            #time.sleep(3)
            self.driver.find_element_by_xpath("//label[.='End']").click()
            self.driver.find_element_by_xpath("//label[.='Breadcrumb']").click()
            self.driver.find_element_by_xpath("//div[@class='helpPageComponent']//ul[@class='pt-collapse-list pt-breadcrumbs']//span[@class='pt-popover-target']").click()
            time.sleep(3)
            #Check if all expected  menu items are present in the collapsioble list
            if(self.isElementPresent("//ul[@class='pt-menu']//li[1]//a[.='ID CMS']") and self.isElementPresent("//ul[@class='pt-menu']//li[2]//a[.='Dev & Test']") and self.isElementPresent("//ul[@class='pt-menu']//li[3]//a[.='Dev Tools']") and self.isElementPresent("//ul[@class='pt-menu']//li[4][.='Style Guides']") and self.isElementPresent("//ul[@class='pt-menu']//li[5]//a[.='FrontEnd Redo']") ):
                print("All, that is 5 menu items are present with the correct order Coolapse From set to **Start** and **style type** set to Standard. ")
            else:
                print("Please review the test case manually.")
             
            #Check only expected visible items are present.
            if(self.isElementPresent("//ul[@class='pt-collapse-list pt-breadcrumbs']//li[1][.='Home']")):
                print("Only 'Home' menu item is visible in the collapsible list inline with collapsible icon.")
                           
            # Check if drop down icon for menu is in the list format with other visible collapsible list items and is second in position.
            if(self.isElementPresent("//ul[@class='pt-collapse-list pt-breadcrumbs']//li[2]//span[@class='pt-popover-target pt-popover-open']")):
                print("Collapsible icon is present at Top and in the List format with other visible items")
            else:
                Exception
                print("Collapsible icon is not at the Top hence fail the test case")
            print("Test case 6 executed succefully.")
        else:
            print("Test case 6 failed")
        
        
        
        
        
        print("Test Case 7:Make sure Change Style Type to Standard -->Drag the visible items slider to 1 --> then set Collapse from option to End --> and click on bread crumb icon should open 5 menu items which are iDCMS,Dev & Test, Dev Tools, Style Guides and FrontEndRedo respectively. Also verify that collapsible icon is in list and below visible items")
        if(self.isElementPresent("//div[@class='helpPageComponent']//div[@class='pt-slider']//div[@class='pt-slider-axis']")):
            #move = ActionChains(self.driver)
            #Lets drag the slider to 1
            #move.drag_and_drop(self.driver.find_element_by_xpath("//div[@class='helpPageComponent']//div[@class='pt-slider']//span[@class='pt-slider-handle']"), self.driver.find_element_by_xpath("//div[@class='helpPageComponent']//div[@class='pt-slider']//div[@class='pt-slider-axis']//div[contains(text(),'1')]")).perform()
            #time.sleep(3)
            self.driver.find_element_by_xpath("//label[.='End']").click()
            self.driver.find_element_by_xpath("//label[.='Standard']").click()
            self.driver.find_element_by_xpath("//div[@class='helpPageComponent']//ul[@class='pt-collapse-list']//span[@class='pt-popover-target']").click()
            time.sleep(3)
            #Check if all expected  menu items are present in the collapsioble list
            if(self.isElementPresent("//ul[@class='pt-menu']//li[1]//a[.='ID CMS']") and self.isElementPresent("//ul[@class='pt-menu']//li[2]//a[.='Dev & Test']") and self.isElementPresent("//ul[@class='pt-menu']//li[3]//a[.='Dev Tools']") and self.isElementPresent("//ul[@class='pt-menu']//li[4][.='Style Guides']") and self.isElementPresent("//ul[@class='pt-menu']//li[5]//a[.='FrontEnd Redo']") ):
                print("All, that is 5 menu items are present with the correct order Coolapse From set to **Start** and **style type** set to Standard. ")
            else:
                print("Please review the test case manually.")
             
            #Check only expected visible items are present.
            if(self.isElementPresent("//ul[@class='pt-collapse-list']//li[1][.='Home']")):
                print("Only 'FrontEnd Redo ' menu item is visible in the collapsible list.")
                           
            # Check if drop down icon for menu is in the list format with other visible collapsible list items
            if(self.isElementPresent("//ul[@class='pt-collapse-list pt-breadcrumbs']//li[2]//span[@class='pt-popover-target pt-popover-open']")):
                print("Collapsible icon is present at Top and in the List format with other visible items")
            else:
                Exception
                print("Collapsible icon is not at the Top hence fail the test case")
            
            print("Test case 7 executed succefully.")
        else:
            print("Test case 7 failed")