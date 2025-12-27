import uuid

class URLShortener:
    def __init__(self):
        self.store = {}

    def shorten(self, url: str) -> str:
        key = uuid.uuid4().hex[:6]
        self.store[key] = url
        return key

    def expand(self, key: str) -> str:
        return self.store.get(key, "Not found")
