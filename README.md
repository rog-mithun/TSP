# 🧭 Traveling Salesman Route Optimizer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A full-stack web application that solves the **Traveling Salesman Problem (TSP)** using Python and visualizes the optimal route across Indian cities on an interactive map. The application allows users to select start and end cities, then calculates and displays the shortest path based on Haversine distances using a brute-force approach.

---

## 📌 Key Features

- 🗺️ Visual route plotting on a Leaflet-based map
- 📍 Selectable start and end cities from a dropdown
- 🧠 Brute-force based TSP optimization using Python
- 📏 Real geographical distance calculations with Haversine formula
- ⚡ Displays total distance and optimal city sequence
- 🖥️ Flask backend with dynamic HTML + JS frontend

---

## 🛠️ Tech Stack

### Frontend:
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Leaflet](https://img.shields.io/badge/Leaflet-199900?style=flat&logo=leaflet&logoColor=white)

### Backend:
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)

---

## 📁 Project Structure

| File/Folder          | Description                                   |
|----------------------|-----------------------------------------------|
| `app.py`             | Flask server to handle route calculation      |
| `tsp.py`             | Backend logic for TSP computation             |
| `templates/index.html` | HTML template with Leaflet map               |
| `static/script.js`   | JavaScript logic for frontend interactions    |
| `static/style.css`   | Styling for frontend                          |
| `Screenshot (8-11).png` | Demo screenshots of app in action           |

---

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rog-mithun/Traveling-Salesman-Route-Optimizer.git
   cd Traveling-Salesman-Route-Optimizer

2. **Install dependencies:**
   ```bash
   pip install flask

3. **Run the app:**
   ```bash
   python app.py

4. **Visit the app:**
   - Open your browser and go to http://127.0.0.1:5000

---

## 📸 Screenshots

- ![Sample Input](Screenshot(8).png)
- ![UI](Screenshot(9).png)
- ![Optimal](Screenshot(10).png)
- ![Output](Screenshot(11).png)

---

## 📖 License

This project is licensed under the [MIT License](LICENSE) © 2023 Mithunsankar S.
