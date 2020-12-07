import requests
import json

# Make a get request to get the latest position  of the space station
response = requests.get("http://api.open-notify.org/iss-now.json")

# Print the status of the code response - Should return 200
print(response.status_code)

# Set up the parameters we want to pass to the API
# This is the latitude and longitude of the New York City
parameters = {"lat": 40.71, "lon": -74}

# Make a get request with the parameters
response = requests.get(
    "http://api.open-notify.org/iss-pass.json", params=parameters)

# Print the content of the response
print(response.content)