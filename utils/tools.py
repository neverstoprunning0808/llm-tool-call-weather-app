import json
import os

import requests
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
from groq import Groq

load_dotenv()


def extract_the_city_and_country(client, user_query):

    prompt = (
        f"Extract the city and country from: '{user_query}'. "
        "If the city is missing, just use the capital of the country. "
        "If you cannot find any information about the city and country, please use city as Paris"
        "Return as JSON with 'city' and 'country' keys."
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
    )

    try:
        return json.loads(response.choices[0].message.content)
    except:
        return None


def get_coordinates_for_city(geo_name):
    geolocator = Nominatim(user_agent="city_coordinate_finder",
                               timeout=10)

    if location := geolocator.geocode(f"{geo_name['city']}, {geo_name['country']}"):
        return location.latitude, location.longitude
    else:
        print(
            f"Could not find coordinates for '{geo_name['city']}, {geo_name['country']}'."
        )
        return None, None


def get_current_weather_open_meteo(latitude, longitude):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "precipitation",
            "weather_code",
            "wind_speed_10m",
        ],
        # 'hourly': [
        #     "temperature_2m",
        #     "relative_humidity_2m",
        #     "precipitation_probability",
        #     "weather_code",
        #     "wind_speed_10m"
        #     ],
        # 'forecast_days': 1,
        "timezone": "auto",
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
