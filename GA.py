from Data import delivery_locations  # Import delivery_locations and haversine from your data script
from DataRep import haversine

# Function to find the nearest neighbor from a given location
def find_nearest_neighbor(location, unvisited_locations):
    min_distance = float('inf')
    nearest_neighbor = None

    for neighbor in unvisited_locations:
        distance = haversine(location['location'][0], location['location'][1], neighbor['location'][0],
                             neighbor['location'][1])
        if distance < min_distance:
            min_distance = distance
            nearest_neighbor = neighbor

    return nearest_neighbor, min_distance


# Initialize variables
current_location = delivery_locations[0]  # Starting location (e.g., depot)
unvisited_locations = delivery_locations[1:]  # Remove the starting location

# Initialize the route with the starting location
route = [current_location]

# Find the nearest neighbor until all locations are visited
while unvisited_locations:
    nearest_neighbor, min_distance = find_nearest_neighbor(current_location, unvisited_locations)
    route.append(nearest_neighbor)
    current_location = nearest_neighbor
    unvisited_locations.remove(nearest_neighbor)

# Return to the depot to complete the route
route.append(route[0])

# Print the optimized route
print("Optimized Route:")
for location in route:
    print(location['name'])
