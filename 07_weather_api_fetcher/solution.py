import requests

def fetch_weather(city: str, api_key: str) -> dict:
    url = "https://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": city}
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Failed to fetch weather data")

    return response.json()


if __name__ == "__main__":
    print("Provide API key to test")
