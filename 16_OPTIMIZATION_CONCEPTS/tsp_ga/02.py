from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_app")
location = geolocator.geocode("mahajanwadi, India")
print(location.address)
print((location.latitude, location.longitude))
