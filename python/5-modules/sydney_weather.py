import requests

# Open-Meteo endpoint
url = "https://api.open-meteo.com/v1/forecast"

# Parameters: latitude, longitude, and what we want (temperature, wind, etc.)
params = {
    "latitude": -33.87,   # Sydney latitude
    "longitude": 151.21,  # Sydney longitude
    "current_weather": True
}

# Send GET request
response = requests.get(url, params=params)

# Parse JSON response
data = response.json()

# Show full response
print("Full response:", data)

# Extract current weather info
current = data["current_weather"]
print("\nCurrent Weather in Sydney:")
print("Temperature:", current["temperature"], "°C")
print("Windspeed:", current["windspeed"], "km/h")
print("Weather Code:", current["weathercode"])
