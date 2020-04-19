import folium
import sqlite3
map1 = folium.Map(location=[14.589896,120.982292],zoom_start = 12,tiles = 'Stamen Terrain')

folium.Marker(location=[14.592659,120.972894],
              popup=folium.Popup('<strong>Intramuros Branch</strong><br>Open time: 9AM - 4PM\n[14.589896,120.982292]'),
              tooltip = 'Intramuros Branch',
              icon = folium.Icon(color='red')).add_to(map1)

#folium.Marker(location = [14.592659,120.972894], popup = folium.Popup("noice"))

map1.save('map.html')

