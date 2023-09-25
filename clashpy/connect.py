import requests
from .clan import Clan
from .player import Player

class Connect:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def clan(self, tag):
        return Clan(tag, self.api_key)

    def player(self, tag):
        return Player(tag, self.api_key)
