import os
import json
import requests
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


API_KEY = os.getenv('OPENWEATHER_API_KEY')
CITIES = ['New York', "Mumbai", "Sydney", 'Chicago', 'London']
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather(city):
    params = {"q": city, "appid": API_KEY}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temp_c": round(data["main"]["temp"] - 273.15, 2),  # Kelvin to Celsius
            "humidity": data["main"]["humidity"],
            "timestamp": datetime.utcnow().isoformat()
        }
    return None

# Collect data
weather_data = []
for _ in range(10):  # ~10 minutes (1 call/min)
    for city in CITIES:
        data = fetch_weather(city)
        if data:
            weather_data.append(data)
            print(f"Fetched: {data}")
    time.sleep(15) 

# Save to JSON
with open("weather_data.json", "w") as f:
    json.dump(weather_data, f, indent=2)
print("Saved to weather_data.json")