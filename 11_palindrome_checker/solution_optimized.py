import requests

class WeatherService:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_weather(self, city: str) -> dict:
        response = requests.get(
            "https://api.weatherapi.com/v1/current.json",
            params={"key": self.api_key, "q": city},
            timeout=5
        )
        response.raise_for_status()
        data = response.json()
        return {
            "city": data["location"]["name"],
            "temperature": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"]
        }
