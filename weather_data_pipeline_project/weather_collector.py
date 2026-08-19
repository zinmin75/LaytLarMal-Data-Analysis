"""
LaytLarMal youtube channel မှာ တင်ထားတဲ့ "Python Request Library | Automation | အဆင့်မြင့် Data Collection" ဗီဒီယိုရဲ့ portfolio project
https://youtu.be/zntaJQplVdc?si=OeVkJzPZOOhoG12K
"""

import requests
from datetime import datetime
import pandas as pd
import os

airports = [
    {
        "name": "Incheon",
        "latitude": 37.456,
        "longitude": 126.705
    },
    {
        "name": "Jeju",
        "latitude": 33.510,
        "longitude": 126.492
    }
]


def collect_weather_data():
    api_url = "https://api.open-meteo.com/v1/forecast"

    for airport in airports:
        params = {
            "latitude": airport['latitude'],
            "longitude": airport['longitude'],
            "current_weather": "true"
        }

        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            print(f"{airport['name']}: 200 - SUCCESS")
        else:
            print(f"{response.status_code} - Failed")

        data = response.json()

        current_temp = data["current_weather"]["temperature"]
        wind_speed = data["current_weather"]["windspeed"]
        wind_direction = data["current_weather"]["winddirection"]

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        df = pd.DataFrame({
            "Timestamp": [timestamp],
            "Airport": airport["name"],
            "Latitude": [airport["latitude"]],
            "Longitude": [airport["longitude"]],
            "Temperature (C)": [current_temp],
            "Wind Speed (km/h)": [wind_speed]
        })

        file_name = "live_weather_log.csv"

        if os.path.exists(file_name):
            write_header = False
        else:
            write_header = True

        df.to_csv(file_name, mode="a", index=False, header=write_header)

        print(
            f"[{timestamp}] "
            f"{airport['name']} weather data saved."
        )


collect_weather_data()
