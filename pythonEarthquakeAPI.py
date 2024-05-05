import requests
from datetime import datetime, timedelta

def getEarthquakes(start_time=None, end_time=None, min_magnitude=None, 
                    max_magnitude=None, format="geojson"):
  
  base_url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
  params = {"format": format}

  if start_time:
    params["starttime"] = start_time
  if end_time:
    params["endtime"] = end_time

  if min_magnitude:
    params["minmagnitude"] = min_magnitude
  if max_magnitude:
    params["maxmagnitude"] = max_magnitude

  #Request to the API
  response = requests.get(base_url, params=params)

  if response.status_code == 200:
    return response.json()
  else:
    print(f"Error: API request failed with status code {response.status_code}")
    return None

def printInfo(earthquake_data):

  if not earthquake_data["features"]:
    print("No earthquakes found in the data.")
    return

  # Access data from features list
  earthquake = earthquake_data["features"][0]

  properties = earthquake["properties"]

  magnitude = properties.get("magnitude")

  mmi = properties.get("mmi") 
  coordinates = earthquake["geometry"]["coordinates"]

  print(f"Magnitude: {magnitude}")
  # Print intensity if available
  if mmi:
    print(f"Modified Mercalli Intensity: {mmi}")
  print(f"Coordinates: {coordinates}")

today = datetime.utcnow()
one_week_ago = today - timedelta(days=7)

earthquake_data = getEarthquakes(start_time=one_week_ago.isoformat(), format="geojson")

if earthquake_data:
  # Print information about earthquake
  printInfo(earthquake_data)
else:
  print("No earthquake data found.")
