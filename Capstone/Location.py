"""
Create a script called location that return the location parameters of any location you want.
"""
import requests

def get_location(place):
  ENDPOINT = "https://nominatim.openstreetmap.org/search"

  params = {
    "format": "json",
    "q": place
  }

  response = requests.get(ENDPOINT, params=params)
  data = response.json()

  if len(data) == 0:
    return "Sorry, we could not find any results for that location."

  latitude = data[0]["lat"]
  longitude = data[0]["lon"]

  return f"Latitude: {latitude}, Longitude: {longitude}"

place = input("Enter a location: ")
print(get_location(place))
