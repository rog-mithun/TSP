var map = L.map('map').setView([0, 0], 2);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
    maxZoom: 18,
}).addTo(map);

var cities = [
    { name: "Chennai", lat: 13.0827, lng: 80.2707 },
    { name: "Coimbatore", lat: 11.0168, lng: 76.9558 },
    { name: "Madurai", lat: 9.9252, lng: 78.1198 },
    { name: "Bangalore", lat: 12.9716, lng: 77.5946 },
    { name: "Hyderabad", lat: 17.3850, lng: 78.4867 },
    { name: "Mumbai", lat: 19.0760, lng: 72.8777 },
    { name: "Cochin", lat: 9.9312, lng: 76.2673 },
    { name: "Tiruchirappalli", lat: 10.7905, lng: 78.7047 }
];

var startCitySelect = document.getElementById('start-city');

for (var i = 0; i < cities.length; i++) {
    var option = document.createElement('option');
    option.value = i;
    option.innerHTML = cities[i].name;
    startCitySelect.appendChild(option);
}

var markers = [];

for (var i = 0; i < cities.length; i++) {
    var marker = L.marker([cities[i].lat, cities[i].lng]).addTo(map);
    marker.bindPopup(cities[i].name);
    markers.push(marker);
}

var line;

function calculateOptimalPath() {
    var startCityIndex = parseInt(startCitySelect.value);

    // Send start city index to the backend
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ startCityIndex: startCityIndex })
    })
    .then(response => response.json())
    .then(data => {
        var optimalPath = data.optimalPath;
        var totalDistance = data.totalDistance;

        // Add the start city at the end to form a complete loop
        optimalPath.push(optimalPath[0]);

        // Highlight the optimal path on the map
        if (line) {
            map.removeLayer(line);
        }
        var latLngs = optimalPath.map(index => [cities[index].lat, cities[index].lng]);
        line = L.polyline(latLngs, { color: 'red' }).addTo(map);

        // Display the optimal path and total dista"nce
        document.getElementById('optimal-path').textContent = optimalPath.map(index => cities[index].name).join(' -> ');
        document.getElementById('total-distance').textContent = totalDistance.toFixed(2);
    });
}