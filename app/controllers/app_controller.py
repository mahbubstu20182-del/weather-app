from app.services.weather_service import WeatherService

class AppController:
    def __init__(self):
        self.weather_service = WeatherService()

    def fetch_weather(self, city: str) -> dict:
        if not city:
            raise ValueError("City name cannot be empty")

        return self.weather_service.get_weather(city)
