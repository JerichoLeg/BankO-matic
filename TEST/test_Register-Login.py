import unittest
from Login import login
from Register import register

reg = register()
reg1 = register()
log = login()
log1 = login()

class TestRegister(unittest.TestCase):
    def test_checkUser(self):
        self.assertEqual(reg.checkUser("admin"),"Exist")
    
    def test_setPassword(self):
        self.assertIsNone(reg.setPassword("123456"))
    
    def test_setFirstName(self):
        self.assertIsNone(reg.setFirstName("Test"))
    
    def test_setLastName(self):
        self.assertIsNone(reg.setLastName("Test"))

    def test_setEmail(self):
        self.assertIsNone(reg.setEmail("Test"))
        
    def test_sendToFile(self):
        self.assertIsNone(reg.sendToFile())
    
    def test_closeDataBase(self):
        self.assertIsNone(reg1.closeDataBase())

class TestLogin(unittest.TestCase):
    def test_checkAccount1(self):
        self.assertEqual(log.checkAccount("UnitTest","Password"),"DoesNotExist")
    
    def test_checkAccount2(self):
        self.assertEqual(log.checkAccount("admin","Password"),"incorrect")
        
    def test_checkAccount3(self):
        self.assertEqual(log.checkAccount("admin","123456"),"correct")
    
    def test_getFirstName(self):
        log.checkAccount("admin","123456")
        self.assertEqual(log.getFirstName(),"Test")
    
    def test_getLastName(self):
        log.checkAccount("admin","123456")
        self.assertEqual(log.getLastName(),"Scenario")
    
    def test_closeDataBase(self):
        self.assertIsNone(log1.closeDataBase())

if __name__ == '__main__':
    unittest.main()
    reg.closeDataBase()