import folium
import sqlite3

def create():
    with sqlite3.connect('Locations.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ATM")

    data = cursor.fetchall() #Fetch all information from branch
    map1 = folium.Map(location=[14.589896,120.982292],zoom_start = 12,tiles = 'Stamen Terrain') #generate Map centered around the city

    i = 0
    try:
        while True:
            folium.Marker(location=[data[i][6],data[i][7]],
                          popup="<strong>%s ATM</strong><br>Open time: %s - %s</br>\n[%s,%s]"%(data[i][0],data[i][2],data[i][3],data[i][6],data[i][7]),
                          tooltip = '%s ATM'%data[i][0],
                          icon = folium.Icon(color='red')).add_to(map1) #create markers from the locations
            i+=1
    except:
        pass
    map1.save('ATMMap1.html') #save map

"""
#Sample:
create() #creates map based on available data
"""