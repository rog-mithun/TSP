import numpy as np
import itertools

def tsp(cities, start_city, end_city, distance_matrix):
    num_cities = len(cities)
    city_indices = range(num_cities)
    all_permutations = list(itertools.permutations(city_indices))

    min_distance = float('inf')
    optimal_path = None

    for permutation in all_permutations:
        if permutation[0] != start_city or permutation[-1] != end_city:
            continue

        distance = 0
        for i in range(num_cities - 1):
            distance += distance_matrix[permutation[i]][permutation[i+1]]

        if distance < min_distance:
            min_distance = distance
            optimal_path = permutation

    return min_distance, optimal_path

# Customize the city names
city_names = ['CBE', 'CHENNAI', 'THENI', 'OOTY', 'BANGLORE', 'KARUR', 'THIRCHY', 'CHITHODE', 'KERALA', 'KARNATAKA']

# Customize the distance matrix
distance_matrix = np.array([
    [0, 10, 15, 20, 25, 30, 35, 40, 45, 50],
    [10, 0, 12, 18, 24, 30, 36, 42, 48, 54],
    [15, 12, 0, 15, 21, 27, 33, 39, 45, 51],
    [20, 18, 15, 0, 10, 16, 22, 28, 34, 40],
    [25, 24, 21, 10, 0, 8, 14, 20, 26, 32],
    [30, 30, 27, 16, 8, 0, 6, 12, 18, 24],
    [35, 36, 33, 22, 14, 6, 0, 5, 10, 15],
    [40, 42, 39, 28, 20, 12, 5, 0, 5, 10],
    [45, 48, 45, 34, 26, 18, 10, 5, 0, 5],
    [50, 54, 51, 40, 32, 24, 15, 10, 5, 0]
])

# Print the available cities
print("Available cities:")
for i, city in enumerate(city_names):
    print(f"{i}: {city}")

# Print the distance matrix in matrix format
print("\nDistance Matrix:")
for row in distance_matrix:
    for distance in row:
        print(f"{distance:<3}", end=" ")
    print()

# Get user input for the starting and ending cities
start_city = int(input("\nEnter the starting city index (0-9): "))
end_city = int(input("Enter the ending city index (0-9): "))

# Perform TSP
distance, path = tsp(city_names, start_city, end_city, distance_matrix)


# Print the total distance and the optimal path
print(f"\nTotal Distance: {distance}")
print("Optimal Path:")
for i in range(len(path)-1):
    print(f"{city_names[path[i]]} -> ", end='')
print(f"{city_names[path[-1]]}")
