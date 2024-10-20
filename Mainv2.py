import pandas as pd
import dask.dataframe as dd
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import requests

def get_weather(lat, lon, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'temperature': data['main']['temp'],
            'conditions': data['weather'][0]['description']
        }
        return weather
    else:
        return None

def get_cost(aircraft_id):
    weather_api_key = "840ec2570dc34675c5a7431b62254080"  # Your OpenWeatherMap API key
    file_path = r'C:\Users\omnku\Desktop\Data hack 24hrs\Website\flightplan.csv'
    geolocator = Nominatim(user_agent="airport_distance_calculator")

    # Read the CSV file using Dask
    df_flights = dd.read_csv(file_path, usecols=['departure_airport', 'arrival_airport', 'aircraft_id'])
    df_flights = df_flights.compute()

    # Filter flight information by aircraft_id
    flight_info = df_flights[df_flights['aircraft_id'] == aircraft_id]

    if not flight_info.empty:
        departure_airport = flight_info['departure_airport'].values[0]
        arrival_airport = flight_info['arrival_airport'].values[0]

        # Get departure coordinates
        departure_location = geolocator.geocode(departure_airport + " Airport")
        if departure_location:
            departure_coords = (departure_location.latitude, departure_location.longitude)

        # Get arrival coordinates
        arrival_location = geolocator.geocode(arrival_airport + " Airport")
        if arrival_location:
            arrival_coords = (arrival_location.latitude, arrival_location.longitude)

        if departure_coords and arrival_coords:
            # Get weather for departure and arrival locations
            departure_weather = get_weather(departure_coords[0], departure_coords[1], weather_api_key)
            arrival_weather = get_weather(arrival_coords[0], arrival_coords[1], weather_api_key)

            # Calculate distance
            distance = great_circle(departure_coords, arrival_coords).kilometers
            
            # Example fuel parameters
            fuel_burn_rate = 0.5  # Fuel burn rate in gallons per kilometer
            fuel_price_per_gallon = 93.98  # Fuel price in dollars per gallon
            
            # Calculate fuel used (in gallons)
            fuel_used = distance * fuel_burn_rate
            
            # Calculate total cost
            total_cost = fuel_used * fuel_price_per_gallon
            
            # Prepare the return data
            return {
                'total_cost': f"{total_cost:.2f}",
                'departure_airport': departure_airport,
                'arrival_airport': arrival_airport,
                'distance': f"{distance:.2f} Km",
                'departure_weather': departure_weather,
                'arrival_weather': arrival_weather
            }
    else:
        return {"error": "No flight found"}

# Example usage:
result = get_cost("KAP3201")
print(result)
