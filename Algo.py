# Sample code for charging station integration
from Data import delivery_locations, charging_stations, truck_capacity
from DataRep import haversine
from GA import find_nearest_neighbor

# Function to find the nearest charging station
def find_nearest_charging_station(current_location, available_stations):
    min_distance = float('inf')
    nearest_station = None

    for station in available_stations:
        distance = haversine(current_location['location'][0], current_location['location'][1], station['location'][0],
                             station['location'][1])
        if distance < min_distance and station['capacity'] >= (truck_capacity - current_battery_level):
            min_distance = distance
            nearest_station = station

    return nearest_station, min_distance


# Initialize variables
current_location = delivery_locations[0]  # Starting location (e.g., depot)
unvisited_locations = delivery_locations[1:]  # Remove the starting location
current_battery_level = truck_capacity  # Initialize the battery level

# Initialize the route with the starting location
route = [current_location]

# Find the nearest neighbor and charging station until all locations are visited
while unvisited_locations:
    nearest_neighbor, min_distance = find_nearest_neighbor(current_location, unvisited_locations)
    nearest_station, station_distance = find_nearest_charging_station(current_location, charging_stations)

    # Decide whether to go to the next location or charge at the station
    if station_distance < min_distance and nearest_station:
        # Go to the nearest charging station
        route.append(nearest_station)
        current_location = nearest_station
        current_battery_level += (nearest_station['capacity'] - current_battery_level)  # Charge to full capacity
    else:
        # Go to the nearest delivery location
        route.append(nearest_neighbor)
        current_location = nearest_neighbor
        unvisited_locations.remove(nearest_neighbor)
        current_battery_level -= min_distance  # Reduce battery level based on distance

# Return to the depot to complete the route
route.append(route[0])

# Print the optimized route
print("Optimized Route:")
for location in route:
    print(location['name'])
