from Data import delivery_locations, charging_stations
from DataRep import haversine
# Define delivery time windows for each location (in minutes)
time_windows = {
    "Location 1": (0, 60),  # Delivery can be made between 0 and 60 minutes from the start.
    "Location 2": (30, 90),  # Delivery can be made between 30 and 90 minutes from the start.
    "Location 3": (60, 120),  # Delivery can be made between 60 and 120 minutes from the start.
}

# Function to calculate the earliest arrival time at a location
def calculate_earliest_arrival_time(location, current_time):
    start_time, end_time = time_windows.get(location['name'], (0, float('inf')))
    return max(start_time, current_time + haversine(location['location'][0], location['location'][1],
                                                    current_location['location'][0], current_location['location'][1]))


# Initialize variables
current_location = delivery_locations[0]  # Starting location (e.g., depot)
unvisited_locations = delivery_locations[1:]  # Remove the starting location
current_time = 0  # Initialize the time

# Initialize the route with the starting location
route = [current_location]

# Find the nearest neighbor until all locations are visited
while unvisited_locations:
    # Calculate the earliest arrival time at each unvisited location
    earliest_arrival_times = {
        location['name']: calculate_earliest_arrival_time(location, current_time)
        for location in unvisited_locations
    }

    # Find the location with the earliest arrival time
    next_location = min(earliest_arrival_times, key=earliest_arrival_times.get)
    min_distance = haversine(current_location['location'][0], current_location['location'][1], next_location['location'][0], next_location['location'][1])

    # Update current_location, current_time, and the route
    current_location = next_location
    current_time = earliest_arrival_times[next_location['name']] + min_distance
    unvisited_locations.remove(next_location)
    route.append(current_location)

# Return to the depot to complete the route
route.append(route[0])

# Print the optimized route with delivery time windows
print("Optimized Route with Delivery Time Windows:")
for location in route:
    print(f"{location['name']} - Time Window: {time_windows.get(location['name'], 'N/A')}")

# ...
# (Previous code)

# Initialize the route with the starting location
route = [current_location]

# Find the nearest neighbor until all locations are visited
while unvisited_locations:
    # Calculate the earliest arrival time at each unvisited location
    earliest_arrival_times = {
        location['name']: calculate_earliest_arrival_time(location, current_time)
        for location in unvisited_locations
    }

    # Find the location with the earliest arrival time
    next_location = min(earliest_arrival_times, key=earliest_arrival_times.get)
    min_distance = haversine(current_location['location'][0], current_location['location'][1],
                             next_location['location'][0], next_location['location'][1])

    # Update current_location, current_time, and the route
    current_location = next_location
    current_time = earliest_arrival_times[next_location['name']] + min_distance
    unvisited_locations.remove(next_location)
    route.append(current_location)

# Return to the depot to complete the route
route.append(route[0])

# Print the optimized route with delivery time windows
print("Optimized Route with Delivery Time Windows:")
for location in route:
    print(f"{location['name']} - Time Window: {time_windows.get(location['name'], 'N/A')}")
