import folium
import sqlite3
import math
from geopandas.tools import geocode
with sqlite3.connect('Locations.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Branch")

data = cursor.fetchall() #Fetch all information from branch

ex = 0
while True:
    while True:
        try:
            loc = input("\nEnter Location(Type exit to stop)\nInput:")
            if loc.lower() == "exit":
                ex = 1
                break
            info = geocode(loc, provider = 'nominatim') #get information about input location
            name = info['address'].loc[0] #get name of location
            long = info['geometry'].loc[0].x #get longitude of input location
            lat = info['geometry'].loc[0].y #get latitude of input location
            break
        except:
            print("Please try again") #Cannot find the input location
    
    if ex == 1:
        break
    
    dist = []
    num = []
    i = 0
    try:
        while True:
            dist.append(float(math.sqrt((data[i][5] - lat)**2 + (data[i][6] - long)**2))) #create list of distances
            num.append(i)
            i+=1
    except:
        dist,num = zip(*sorted(zip(dist,num))) #sort both list according to smallest distance

    if dist[0] < 25: #Request for another input if location is too far
        break
    else:
        print("Please try again")
        pass
        
def createMap():
    map1 = folium.Map(location=[14.589896,120.982292],zoom_start = 12,tiles = 'Stamen Terrain') #generate map centered around the city
    folium.Marker(location=[lat,long],
                  popup="<strong>Your location:</strong> \n%s" %name,
                  tooltip = 'Click for more info',
                  icon = folium.Icon(color='blue')).add_to(map1) #create marker based on input location

    i = 0
    for a in num:
        try:
            folium.Marker(location=[data[a][5],data[a][6]],
                          popup="<strong>%s Branch</strong><br>Open time: %s - %s</br>\n[%s,%s]"%(data[a][0],data[a][2],data[a][3],data[a][5],data[a][6]),
                          tooltip = '%s Branch'%data[a][0],
                          icon = folium.Icon(color='red')).add_to(map1) #create markers for nearest locations
            i+=1
        except:
            pass
        if i == 5:
            break
    map1.save('map2.html') #save map

if ex == 0: # if no exit is requested, continue the program
    createMap()