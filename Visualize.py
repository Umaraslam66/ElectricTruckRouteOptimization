import pip
import folium
from Data import delivery_locations
from DataRep import haversine
from GA import route

# Function to calculate the total distance of a route
def calculate_total_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        location1 = route[i]['location']
        location2 = route[i + 1]['location']
        total_distance += haversine(location1[0], location1[1], location2[0], location2[1])
    return total_distance

# Create a map centered around the first delivery location (Location 1)
map_center = delivery_locations[0]['location']
m = folium.Map(location=map_center, zoom_start=10)

# Create markers for delivery locations
for location in delivery_locations:
    folium.Marker(
        location=location['location'],
        popup=location['name']
    ).add_to(m)

# Create a polyline to represent the optimized route
# Replace this with your actual optimized route data
optimized_route = [
    {"name": "Location 1", "location": (59.3293, 18.0686)},
    {"name": "Location 2", "location": (57.7089, 11.9746)},
    {"name": "Location 3", "location": (55.6049, 13.0038)},
    # Add more locations as needed
]

route_coordinates = [(location['location'][0], location['location'][1]) for location in optimized_route]
folium.PolyLine(route_coordinates, color="blue", weight=5, opacity=0.7).add_to(m)

# Display the total distance of the optimized route
total_distance = calculate_total_distance(optimized_route)
folium.Marker(
    location=map_center,
    popup=f"Total Distance: {total_distance:.2f} km",
    icon=folium.DivIcon(html=f"<div>{total_distance:.2f} km</div>")
).add_to(m)

# Save the map to an HTML file
m.save("optimized_route_map.html")

# Display the map in a Jupyter Notebook or a web browser
m
