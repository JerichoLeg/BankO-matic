import folium
import sqlite3
import pandas as pd


with sqlite3.connect('Locations.db') as conn:
    cursor = conn.cursor()
    cursor.execute("Select * from ATM")

data = cursor.fetchall()

map1 = folium.Map(location=[14.589896,120.982292],zoom_start = 12,tiles = 'Stamen Terrain')
i = 0
try:
    while True:
        folium.Marker(location=[data[i][6],data[i][7]],
                      popup="<strong>%s ATM</strong><br>Open time: %s - %s</br>\n[%s,%s]"%(data[i][0],data[i][2],data[i][3],data[i][6],data[i][7]),
                      tooltip = '%s ATM'%data[i][0],
                      icon = folium.Icon(color='red')).add_to(map1)
        i+=1
except:
    pass

map1.save('map.html')
