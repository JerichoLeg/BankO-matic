import folium
import sqlite3

with sqlite3.connect('Locations.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Branch")

data = cursor.fetchall() #Fetch all information from branch
map1 = folium.Map(location=[14.589896,120.982292],zoom_start = 12,tiles = 'Stamen Terrain') #generate Map centered around the city

i = 0
try:
    while True:
        folium.Marker(location=[data[i][5],data[i][6]],
                      popup="<strong>%s Branch</strong><br>Open time: %s - %s</br>\n[%s,%s]"%(data[i][0],data[i][2],data[i][3],data[i][5],data[i][6]),
                      tooltip = '%s Branch'%data[i][0],
                      icon = folium.Icon(color='red')).add_to(map1) #create markers from the locations
        i+=1
except:
    pass
map1.save('map.html') #save map

"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    with sqlite3.connect('Locations.db') as conn:
        cursor = conn.cursor()
        cursor.execute("Select * from ATM")

    data = cursor.fetchall()

    map1 = folium.Map(location=[14.589896,120.982292],zoom_start = 12,tiles = 'Stamen Terrain')
    i = 0
    try:
        while True:
            folium.Marker(location=[data[i][6],data[i][7]],
                          popup="<strong>%s Branch</strong><br>Open time: %s - %s</br>\n[%s,%s]"%(data[i][0],data[i][2],data[i][3],data[i][6],data[i][7]),
                          tooltip = '%s Branch'%data[i][0],
                          icon = folium.Icon(color='red')).add_to(map1)
            i+=1
    except:
        pass

    return map1._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)
"""