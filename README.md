# Earthquake Data Retrieval
This Python script fetches earthquake data from api.geonet.org.nz and prints information about earthquakes that occurred within a specified time range.

## Features
Fetch earthquake data from Geonet earthquake API.

Specify start and end time for earthquake data retrieval.

Filter earthquakes based on minimum and maximum magnitude.

Print information about the latest earthquake within the specified time range.

## Installation
Clone the repository

Install the required dependencies

## Usage
1. Open the pythonEarthquakeAPI.py file in your Python environment.
2. Modify the parameters in the getEarthquakes function call to specify the desired time range and magnitude filters.
3. Run the script:

The script will fetch earthquake data from the Geonet API and print information about the latest earthquake within the specified time range.

## Parameters
start_time: Start time for earthquake data retrieval (optional).

end_time: End time for earthquake data retrieval (optional).

min_magnitude: Minimum magnitude of earthquakes to retrieve (optional).

max_magnitude: Maximum magnitude of earthquakes to retrieve (optional).

format: Format of the earthquake data (default is "geojson").
### Dependencies
requests: For making HTTP requests to the Geonet earthquake API.
