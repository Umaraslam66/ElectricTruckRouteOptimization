import csv
import random

# Dummy charging station data

charging_stations = [
    {"name": "Station A", "location": (59.3293, 18.0686), "capacity": 100}, #stockholm
    {"name": "Station B", "location": (57.7089, 11.9746), "capacity": 80},  #Malmo
    {"name": "Station C", "location": (55.6049, 13.0038), "capacity": 120}, #Gothenburg
]

# Dummy electric truck specifications
truck_capacity = 250  # kWh
truck_consumption_rate = 0.35  # kWh per mile

# Dummy delivery locations with time windows
delivery_locations = [
    {"name": "Location 1", "location": (59.3293, 18.0686), "demand": 20, "window": (8, 12)},
    {"name": "Location 2", "location": (57.7089, 11.9746), "demand": 30, "window": (10, 14)},
    {"name": "Location 3", "location": (55.6049, 13.0038), "demand": 15, "window": (9, 13)},
]

# Dummy traffic conditions (random delays in minutes)
traffic_conditions = {
    "Location 1": random.randint(0, 15),
    "Location 2": random.randint(0, 20),
    "Location 3": random.randint(0, 10),
}




# Save charging station data to CSV
with open('charging_stations.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'latitude', 'longitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for station in charging_stations:
        writer.writerow(
            {'name': station['name'], 'latitude': station['location'][0], 'longitude': station['location'][1]})

# Save delivery location data to CSV
with open('delivery_locations.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'latitude', 'longitude', 'demand', 'window_start', 'window_end']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for location in delivery_locations:
        writer.writerow(
            {'name': location['name'], 'latitude': location['location'][0], 'longitude': location['location'][1],
             'demand': location['demand'], 'window_start': location['window'][0], 'window_end': location['window'][1]})

# Save traffic conditions data to CSV
with open('traffic_conditions.csv', 'w', newline='') as csvfile:
    fieldnames = ['location', 'delay_minutes']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for location, delay in traffic_conditions.items():
        writer.writerow({'location': location, 'delay_minutes': delay})

# Save truck specifications to a separate CSV
with open('truck_specifications.csv', 'w', newline='') as csvfile:
    fieldnames = ['capacity_kWh', 'consumption_rate_kWh_per_mile']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'capacity_kWh': truck_capacity, 'consumption_rate_kWh_per_mile': truck_consumption_rate})
