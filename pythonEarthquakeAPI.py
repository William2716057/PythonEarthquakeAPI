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

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to retrieve earthquake data: {e}")
        return None

def printInfo(earthquake_data):

    if not earthquake_data["features"]:
        print("No earthquakes found in the data.")
        return

    # Access data from features list
    earthquake = earthquake_data["features"][0]

    properties = earthquake.get("properties", {})
    magnitude = properties.get("mag")

    if magnitude is None:
        print("Magnitude information not available.")
    else:
        print(f"Magnitude: {magnitude}")

    mmi = properties.get("mmi") 
    coordinates = earthquake["geometry"]["coordinates"]

    if mmi:
        print(f"Modified Mercalli Intensity: {mmi}")

    if coordinates:
        longitude, latitude, depth = coordinates
        print(f"Location: Latitude {latitude}, Longitude {longitude}, Depth {depth} km")
    else:
        print("Coordinates not available.")

today = datetime.utcnow()
one_week_ago = today - timedelta(days=7)

earthquake_data = getEarthquakes(start_time=one_week_ago.isoformat(), format="geojson")

if earthquake_data:
    # Print information about earthquake
    printInfo(earthquake_data)
else:
    print("No earthquake data found.")
