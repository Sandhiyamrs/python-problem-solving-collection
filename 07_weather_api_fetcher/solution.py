import requests

API_KEY = "your_api_key_here"

city = input("Enter city: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

data = requests.get(url).json()

print("Temperature:", data["main"]["temp"], "°C")
print("Weather:", data["weather"][0]["description"])
