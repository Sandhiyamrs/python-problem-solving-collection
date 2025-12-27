from solution_optimized import WeatherFetcher

fetcher = WeatherFetcher("test_key")
assert fetcher.api_key == "test_key"
print("Weather fetcher basic test passed")
