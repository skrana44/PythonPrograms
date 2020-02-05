from geopy.geocoders import ArcGIS

street = input("Please enter street/society/towns name: ")
city = input("Please input city name: ")
state = input("Please input state name: ")
pin = input("Please enter pin: ")
country = input("Please enter country name: ")

address = street + "," + city + "," + state + "," + pin + "," + country
nom = ArcGIS()
latitude = nom.geocode(address).latitude
longitude = nom.geocode(address).longitude
print("Latitude is: ",latitude,"and Longitude is: ",longitude)