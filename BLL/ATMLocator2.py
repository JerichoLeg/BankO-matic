import folium
import sqlite3
import math
from geopandas.tools import geocode
with sqlite3.connect('Locations.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ATM")

data = cursor.fetchall() #Fetch all information from branch


class startLocation():
    def __init__(self,location):
        self.q = 0
        while True:
            while True:
                try:
                    if location.lower() == "exit":
                        self.q = 1
                        break
                    info = geocode(location, provider = 'nominatim') #get information about input location
                   # print(info)
                   # print(info['address'].loc[0])
                    self.name = info['address'].loc[0] #get name of location
                    self.long = info['geometry'].loc[0].x #get longitude of input location
                    self.lat = info['geometry'].loc[0].y #get latitude of input location
                    break
                except:
                    print("Please try again") #Cannot find the input location
                    location = input("\nEnter Location(Type exit to stop)\nInput:")
            if self.q == 0:
                self.dist = []
                self.num = []
                i = 0
                try:
                    while True:
                        self.dist.append(float(math.sqrt((data[i][6] - self.lat)**2 + (data[i][7] - self.long)**2))) #create list of distances
                        self.num.append(i)
                        i+=1
                except:
                    self.dist,self.num = zip(*sorted(zip(self.dist,self.num))) #sort both list according to smallest distance

                if self.dist[0] < 5:
                    break
                else:
                    print("Please try again") #Request for another input if location is too far
                    location = input("\nEnter Location(Type exit to stop)\nInput:")
            else:
                break
    
    def getName(self):
        return self.name
    def getLong(self):
        return self.long
    def getLat(self):
        return self.lat
    def getDist(self):
        return self.dist
    def getNum(self):
        return self.num

    def getQuitVal(self):
        if self.q == 1:
            return 1
        else:
            return 0

def createMap(name,long,lat,dist,num):
    map1 = folium.Map(location=[14.589896,120.982292],zoom_start = 12,tiles = 'Stamen Terrain') #generate map centered around the city
    folium.Marker(location=[lat,long],
                  popup="<strong>Your location:</strong> \n%s" %name,
                  tooltip = 'Click for more info',
                  icon = folium.Icon(color='blue')).add_to(map1) #create marker based on input location
    i = 0
    for a in num:
        try:
            folium.Marker(location=[data[a][6],data[a][7]],
                          popup="<strong>%s ATM</strong><br>Open time: %s - %s</br>\n[%s,%s]"%(data[a][0],data[a][2],data[a][3],data[a][6],data[a][7]),
                          tooltip = '%s ATM'%data[a][0],
                          icon = folium.Icon(color='red')).add_to(map1) #create markers for nearest locations
            i+=1
        except:
            pass
        if i == 5:
            break
    map1.save('map2.html') #save map

"""
#Sample:
mp = startLocation(input("\nEnter Location(Type exit to stop)\nInput:")) #initiate
if mp.getQuitVal() == 0: #check if the user wanted to exit
    createMap(mp.getName(),mp.getLong(),mp.getLat(),mp.getDist(),mp.getNum()) #pass values to create map function
"""
