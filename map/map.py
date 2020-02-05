import pandas
import folium
from geopy.geocoders import ArcGIS

file = pandas.read_csv("Volcanoes.txt")
lat = list(file["LAT"])
lon = list(file["LON"])
elev = list(file["ELEV"])

def color_maker(elv):
    if elv < 1000:
        return "green"
    elif 1000 <= elv < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[38,-99],zoom_start=5,tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanos")

for lt,ln,elv in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],popup=elv,radius=6,fill_color=color_maker(elv),color="grey",opacity=0.8))

fgp = folium.FeatureGroup(name="world population")

fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] > 1000000 
else 'orange' if  1000000 <= x['properties']['POP2005'] <2000000 
else 'red'}))


map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("map.html")