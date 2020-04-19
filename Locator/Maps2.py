import folium
import sqlite3
import math
from geopandas.tools import geocode
with sqlite3.connect('Locations.db') as conn:
    cursor = conn.cursor()
    cursor.execute("Select * from Branch")

data = cursor.fetchall()

map1 = folium.Map(location=[14.589896,120.982292],zoom_start = 12,tiles = 'Stamen Terrain')

while True:
    try:
        loc = input("\nEnter Location: ")
        info = geocode(loc, provider = 'nominatim')
        long = info['geometry'].loc[0].x
        lat = info['geometry'].loc[0].y
        break
    except:
        print("Please try again")
        
folium.Marker(location=[lat,long],
              popup="Your location: \n%s" %loc,
              tooltip = 'Click for more info',
              icon = folium.Icon(color='blue')).add_to(map1)
dist = []
num = []
i = 0
try:
    while True:
        dist.append(math.sqrt((data[i][5] - lat)**2 + (data[i][6] - long)**2))
        num.append(i)
        i+=1
except:
    pass

dist,num = zip(*sorted(zip(dist,num)))

i = 0
for a in num:
    try:
        folium.Marker(location=[data[a][5],data[a][6]],
                      popup="<strong>%s Branch</strong><br>Open time: %s - %s</br>\n[%s,%s]"%(data[a][0],data[a][2],data[a][3],data[a][5],data[a][6]),
                      tooltip = '%s Branch'%data[a][0],
                      icon = folium.Icon(color='red')).add_to(map1)
        i+=1
    except:
        pass
    if i == 5:
        break

map1.save('map2.html')