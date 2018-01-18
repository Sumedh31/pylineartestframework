'''
Created on 29-Jun-2017

@author: Sumedh.Tambe
'''
class IDAdminLocators():
    
    def Adminusername(self):
        return "//div/input[@id='LoginUserName']"
    def Adminpassword(self):
        return "//div/input[@id='LoginPassword']"
    def AdminLoginButton(self):
        return "//div[@class='loginButtons']//div/input[@id='Login']"
    def LogOutLink(self):
        return "//div[@id='userDisplay']/a[.='Logout']"