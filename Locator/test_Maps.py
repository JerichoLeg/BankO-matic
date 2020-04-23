import unittest
import math
from Maps2 import startLocation, createMap
from Maps import create
import sqlite3
with sqlite3.connect('Locations.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Branch")
data = cursor.fetchall()
dist = []
num = []
loc = startLocation("Manila")
i=0
try:
    while True:
        dist.append(float(math.sqrt((data[i][5] - 14.5906216)**2 + (data[i][6] - 120.9799696)**2)))
        num.append(i)
        i+=1
except:
    dist,num = zip(*sorted(zip(dist,num)))
    
class TestMaps2(unittest.TestCase):
    def test_Name(self):
        self.assertEqual(loc.getName(),"Manila, Metro Manila, Philippines")
    
    def test_Longitude(self):
        self.assertEqual(loc.getLong(),120.9799696)
    
    def test_Latitude(self):
        self.assertEqual(loc.getLat(), 14.5906216)
    
    def test_Dist(self):
        self.assertEqual(loc.getDist(), dist)
    
    def test_Num(self):
        self.assertEqual(loc.getNum(), num)
    
    def test_QuitVal(self):
        self.assertEqual(loc.getQuitVal(),0)
        
    def test_Map(self):
        self.assertIsNone(createMap("Manila, Metro Manila, Philippines",120.9799696,14.5906216,dist,num))

class TestMaps(unittest.TestCase):
    def test_create(self):
        self.assertIsNone(create())
        
if __name__ == '__main__':
    unittest.main()