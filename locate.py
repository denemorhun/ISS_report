from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="denem")
location = geolocator.reverse("52.509669, 13.376294")
print(location.address)
