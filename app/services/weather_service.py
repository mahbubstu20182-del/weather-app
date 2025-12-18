import os
import requests
from dotenv import load_dotenv

load_dotenv()

class WeatherService:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        if not self.api_key:
            raise ValueError("OPENWEATHER_API_KEY not found in .env file")

    def get_weather(self, city: str) -> dict:
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        response = requests.get(self.BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"].title()
        }
