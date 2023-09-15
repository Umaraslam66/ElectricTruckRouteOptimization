import math


# Function to calculate the Haversine distance between two points on the Earth's surface
def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance


# Dummy charging station data
charging_stations = [
    {"name": "Station A", "location": (59.3293, 18.0686)},  # Stockholm
    {"name": "Station B", "location": (57.7089, 11.9746)},  # Gothenburg
    {"name": "Station C", "location": (55.6049, 13.0038)},  # Malmo
]

# Dummy delivery locations with time windows
delivery_locations = [
    {"name": "Location 1", "location": (59.3293, 18.0686), "demand": 20, "window": (8, 12)},
    {"name": "Location 2", "location": (57.7089, 11.9746), "demand": 30, "window": (10, 14)},
    {"name": "Location 3", "location": (55.6049, 13.0038), "demand": 15, "window": (9, 13)},
]

# Calculate distances between charging stations, delivery locations, and truck's initial location
truck_location = (59.3293, 18.0686)  # Starting from Stockholm

# Calculate distances to charging stations
charging_station_distances = {}
for station in charging_stations:
    station_location = station['location']
    distance = haversine(truck_location[0], truck_location[1], station_location[0], station_location[1])
    charging_station_distances[station['name']] = distance

# Calculate distances to delivery locations
delivery_location_distances = {}
for location in delivery_locations:
    location_name = location['name']
    location_coords = location['location']
    distance = haversine(truck_location[0], truck_location[1], location_coords[0], location_coords[1])
    delivery_location_distances[location_name] = distance

# Print the calculated distances
print("Charging Station Distances:")
print(charging_station_distances)

print("\nDelivery Location Distances:")
print(delivery_location_distances)
