import folium
import pandas as pd

#Colour Dictionary so that I can set the icon colour based on the starting letter of the capital city "http://www.christianfaur.com/color/Site/Picking%20Colors.html"
colorDic = {'a':'#0000B4', 'b':'#AF0D66', 'c':'#92F846', 'd':'#FFC82F', 'e':'#FF7600', 'f':'#B9B9B9', 'g':'#EBEBDE', 'h':'#646464', 'i':'#FFFF00', 'j':'#371370','k':'#FFFF96', 'l':'#CA3E5E',
            'm':'#CD913F', 'n':'#0C4B64', 'o':'#FF0000', 'p':'#AF9B32', 'q':'#000000', 'r':'#254619', 's':'#792187', 't':'#538CD0', 'u':'#009A25', 'v':'#B2DCCD', 'w':'#FF98D5',
            'x':'#00004A', 'y':'#AFC84A', 'z':'#3F190C'}

#Read in the .txt file and propogate lists for faster iteration.
data= pd.read_csv("capitals.txt", encoding = "ISO-8859-1")
lat = list(data["Latitude"])
lng = list(data["Longitude"])
name = list(data["Capital"])

#This function will map the parsed city to the specified colour based on the colour dictionary.
def colorPick(cityName):
    return colorDic[cityName[0].lower()]

#Define the map and place markers on it
map = folium.Map(location=[-0.002205, -78.4563984], zoom_start=4, tiles='OpenStreetMap')
fgCapCities = folium.FeatureGroup(name="Capital Cities")
for lat, lng, name in zip(lat, lng, name):
            fgCapCities.add_child(folium.CircleMarker(location=[lat, lng], popup=folium.Popup(name,parse_html=True), radius=6, color=colorPick(name),fill_color=colorPick(name),
                                             fill=True, fill_opacity=1))

fgCountryPop = folium.FeatureGroup(name="Population")
#Adds a layer that colours countries based on their population using GeoJson
fgCountryPop.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000
                                                     else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgCapCities)
map.add_child(fgCountryPop)
map.add_child(folium.LayerControl())
map.save("Map1.html")
