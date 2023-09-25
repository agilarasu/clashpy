import requests
from .connect import Connect

class League(Connect):
    def __init__(self):
        super().__init__(self.api_key)
        self.endpoints = {
            "capitalleagues": "capitalleagues",
            "leagues": "leagues"
        }

    def __getattr__(self, name):
        if name in self.endpoints:
            endpoint = self.endpoints[name]
            return lambda: self._make_request(endpoint)
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")