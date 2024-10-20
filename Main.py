import pandas as pd
import dask.dataframe as dd
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

def get_cost(aircraft_id):
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
            # Calculate distance
            distance = great_circle(departure_coords, arrival_coords).kilometers
            
            # Example fuel parameters
            fuel_burn_rate = 0.5  # Fuel burn rate in gallons per kilometer
            fuel_price_per_gallon = 93.98  # Fuel price in dollars per gallon
            
            # Calculate fuel used (in gallons)
            fuel_used = distance * fuel_burn_rate
            
            # Calculate total cost
            total_cost = fuel_used * fuel_price_per_gallon
            
            return f"{total_cost:.2f}",departure_airport, arrival_airport, f"{distance:.2f}Km"
    else:
        return 0


