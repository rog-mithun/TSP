from flask import Flask, render_template, request, jsonify
import itertools
import math

app = Flask(__name__)

def calculate_distance(coord1, coord2):
    # Coordinates are in (latitude, longitude) format
    lat1, lng1 = coord1
    lat2, lng2 = coord2

    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lng1_rad = math.radians(lng1)
    lat2_rad = math.radians(lat2)
    lng2_rad = math.radians(lng2)

    # Haversine formula
    dlat = lat2_rad - lat1_rad
    dlng = lng2_rad - lng1_rad
    a = math.sin(dlat/2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlng/2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    radius = 6371  # Radius of the Earth in kilometers
    distance = radius * c

    return distance


def calculate_distance_matrix(cities):
    # Calculate the distance matrix between all cities
    num_cities = len(cities)
    distance_matrix = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(i+1, num_cities):
            distance = calculate_distance((cities[i]['lat'], cities[i]['lng']), (cities[j]['lat'], cities[j]['lng']))
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance
    return distance_matrix


def tsp(cities, start_city_index, distance_matrix):
    num_cities = len(cities)
    city_indices = range(num_cities)
    all_permutations = list(itertools.permutations(city_indices))

    min_distance = float('inf')
    optimal_path = None

    for permutation in all_permutations:
        if permutation[0] != start_city_index:
            continue
        distance = 0
        for i in range(num_cities - 1):
            distance += distance_matrix[permutation[i]][permutation[i+1]]
        distance += distance_matrix[permutation[num_cities - 1]][permutation[0]]  # Add distance from last city to start city
        if distance < min_distance:
            min_distance = distance
            optimal_path = permutation

    return min_distance, optimal_path


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    cities = [
        { 'name': 'Chennai', 'lat':  13.0827, 'lng': 80.2707 },
        { 'name': 'Coimbatore', 'lat': 11.0168, 'lng': 76.9558 },
        { 'name': 'Madurai', 'lat': 9.9252, 'lng': 78.1198 },
        { 'name': 'Banglore', 'lat': 12.9716, 'lng': 77.5946 },
        { 'name': 'Hyderabad', 'lat': 17.3850, 'lng': 78.4867 },
        { 'name': 'Mumbai', 'lat': 19.0760, 'lng': 72.8777 },
        { 'name': 'Cochin', 'lat': 9.9312, 'lng': 76.2673 },
        { 'name': 'Tirchy', 'lat': 10.7605, 'lng': 78.7047 }
    ]

    distance_matrix = calculate_distance_matrix(cities)

    start_city_index = request.json['startCityIndex']

    min_distance, optimal_path = tsp(cities, start_city_index, distance_matrix)

    return jsonify({ 'optimalPath': optimal_path, 'totalDistance': min_distance })


if __name__ == '__main__':
    app.run(debug=True)
