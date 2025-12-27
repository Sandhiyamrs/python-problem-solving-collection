from solution_optimized import URLShortener

shortener = URLShortener()
key = shortener.shorten("https://example.com")
assert shortener.expand(key) == "https://example.com"
print("URL shortener tests passed")
