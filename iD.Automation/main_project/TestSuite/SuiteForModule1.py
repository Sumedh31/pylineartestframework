'''
Created on 13-Jul-2017

@author: Sumedh.Tambe
'''
import unittest
from TestScripts import NavBarTest, CollapsibleListTest
from unittest import runner


class SuiteForModule1(unittest.TestCase):
    def test_main(self):
        self.suite=unittest.TestSuite()
        self.suite.addTest(NavBarTest.Test("test_NavBar"))
        #self.suite.addTests([
            #unittest.defaultTestLoader.loadTestsFromTestCase(NavBarTest.Test),
            #unittest.defaultTestLoader.loadTestsFromTestCase(CollapsibleListTest.CollapsibleList)
            #unittest.defaultTestLoader.loadTest(name, module)
            
            #])
        runnerobject=unittest.TextTestRunner()
        runnerobject.run(self.suite)
                
        
if __name__ == "__main__":
    unittest.main()