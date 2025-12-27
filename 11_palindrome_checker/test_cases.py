from solution_optimized import WeatherService

service = WeatherService("dummy_key")
assert service.api_key == "dummy_key"
print("Weather API basic test passed")
