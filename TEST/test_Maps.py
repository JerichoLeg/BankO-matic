import unittest
from BranchLocator2 import startLocation
from BranchLocator1 import create

loc = startLocation()

class TestMaps2(unittest.TestCase):
    def test_Name(self):
        
        self.assertEqual(loc.checkLocation("Manila"),"LocationFound")
    
    def test_Map(self):
        loc.checkLocation("Manila")
        self.assertIsNone(loc.createMap())

class TestMaps(unittest.TestCase):
    def test_create(self):
        self.assertIsNone(create())
        
if __name__ == '__main__':
    unittest.main()