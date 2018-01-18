'''
Created on 29-Jun-2017

@author: Sumedh.Tambe
'''
class VerticalNavBarLocators():
    
    def ExpandHomeSite(self):
        return "//*[@id='tree1']/div/div/table[2]/tbody/tr/td[2]/div[1]/table[2]/tbody/tr/td[2]/div[1]/table[1]/tbody/tr/td[1]/img"
    def ExpandNavEditor(self):
        return "//tbody/tr//td/span[.='Nav Editor']/../..//td//span[.='Nav Editor']"
    def EditNavBarInNavEditor(self):
        return "//tbody//tr//td//a[contains(@href,'/admin/apps/FrontEndNav/EditNavBars.aspx')]"
    def EditButtonOfFirstVerticalNav(self):
        return "//tbody//tr//td//span[contains(text(),'Home Site Vertical Nav')]//..//..//..//td//a[contains(text(),'Edit')]"
    def NavItemtabInEditVerticalNav(self):
        return "//div[@id='NavBarEditPage']//li//a[contains(text(),'Nav Items')]"
    def AddNavIteminNav(self):
        return"//tbody//tr//a[@class='button button-addmenu']"
    def NavItemName(self):
        return"//input[@id='txtNameTree']"
    def NavItemLink(self):
        return "//input[@id='NavTree_txtLinkTree']"
    def EditNavOkButton(self):
        return "//div[@id='NavBarEditPage']//input[@id='CustomEditButtons_Ok']"
    def AddedNavItemOnFE(self):
        return "//a[@class='pt-menu-item pt-popover-dismiss' and @href='https://github.com/casesandberg/react-color/' and contains(text(),'Vertical Navigation First')]"