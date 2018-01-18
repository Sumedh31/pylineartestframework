'''
Created on 22-Jun-2017

@author: Sumedh.Tambe
'''


class CollapsibleLocatorsTest():
    def firstLocator(self):
        return "//table[@class='id-wiki-layout']/tbody//tr//td//div[@class='componentContainer']//a[.='Collapsible List']"
    
    def ViewProps(self):
        return "//div[@class='helpPageToggleContent']//div//span[@class=contains(text(),'View Properties')]"
    
    