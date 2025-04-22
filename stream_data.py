import os
import time
import json
import requests
from datetime import datetime
from dotenv import load_dotenv
import boto3

load_dotenv()

API_KEY = os.getenv('OPENWEATHER_API_KEY')
ACCESS_KEY = os.getenv('access_key')
Secret_access_key = os.getenv('secret_access_key')
CITIES = ['New York', "Mumbai", "Sydney", 'Chicago', 'London']
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

kinesis = boto3.client("kinesis", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=Secret_access_key, region_name="us-east-1")

def fetch_weather(city):
    params = {'q':city, 'appid':API_KEY}
    response = requests.get(BASE_URL, params = params)
    if response.status_code == 200:
        data = response.json()
        return {
            'city': data['name'],
            'temp_c': round(data['main']['temp'] - 273.15, 2),  # Kelvin to Celsius
            'humidity': data['main']['humidity'],
            'timestamp': datetime.utcnow().isoformat()
        }
    return None

for _ in range(30):
    for city in CITIES:
        data = fetch_weather(city)
        if data:
            kinesis.put_record(
                StreamName="weather-stream",
                Data=json.dumps(data) + "\n",
                PartitionKey=city
            )
            print(f"data sent, {data}")
    time.sleep(15) 

print('streaming data to kinesis completed')

