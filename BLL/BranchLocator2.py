import folium
import sqlite3
import math
from geopandas.tools import geocode

class startLocation:
    def __init__(self):
        #Fetch all information from branch
        with sqlite3.connect('Locations.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Branch")
        self.data = cursor.fetchall()#Fetch all information from branch
        map1 = folium.Map(location=[14.589896,120.982292],zoom_start = 12,tiles = 'Stamen Terrain') #generate Map centered around the city
        map1.save('BranchMap2.html')
        self.name = ""
        self.long = ""
        self.lat = ""
        self.dist = ""
   
    def checkLocation(self,location):
        try:
            info = geocode(location, provider = 'nominatim') #get information about input location
            self.name = info['address'].loc[0] #get name of location
            self.long = info['geometry'].loc[0].x #get longitude of input location
            self.lat = info['geometry'].loc[0].y #get latitude of input location
            self.dist = []
            self.num = []
            i = 0
            try:
                while True:
                    self.dist.append(float(math.sqrt((self.data[i][5] - self.lat)**2 + (self.data[i][6] - self.long)**2))) #create list of distances
                    self.num.append(i)
                    i+=1
            except:
                self.dist,self.num = zip(*sorted(zip(self.dist,self.num))) #sort both list according to smallest distance

            if self.dist[0] < 5:
                return "LocationFound"
            else:
                return "TooFar"
            
        except:
            return "LocationNotFound"

    def createMap(self):
        map1 = folium.Map(location=[14.589896,120.982292],zoom_start = 12,tiles = 'Stamen Terrain') #generate map centered around the city
        folium.Marker(location=[self.lat,self.long],
                      popup="<strong>Your location:</strong> \n%s" %self.name,
                      tooltip = 'Click for more info',
                      icon = folium.Icon(color='blue')).add_to(map1) #create marker based on input location
        i = 0
        for a in self.num:
            try:
                folium.Marker(location=[self.data[a][5],self.data[a][6]],
                              popup="<strong>%s Branch</strong><br>Open time: %s - %s</br>\n[%s,%s]"%(self.data[a][0],self.data[a][2],self.data[a][3],self.data[a][5],self.data[a][6]),
                              tooltip = '%s Branch'%self.data[a][0],
                              icon = folium.Icon(color='red')).add_to(map1) #create markers for nearest locations
                i+=1
            except:
                pass
            if i == 5:
                break
        map1.save('BranchMap2.html') #save map

"""
#Sample:
mp = startLocation(input("\nEnter Location(Type exit to stop)\nInput:")) #initiate
if mp.getQuitVal() == 0: #check if the user wanted to exit
    createMap(mp.getName(),mp.getLong(),mp.getLat(),mp.getDist(),mp.getNum()) #pass values to create map function
"""