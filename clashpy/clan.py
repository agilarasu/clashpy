import requests

class Clan:
    def __init__(self, tag,api_key):
        self.base_url = "https://api.clashofclans.com/v1/"
        self.tag = requests.utils.quote(tag)
        self.api_key = api_key
        self.endpoints = {
            "info": f"clans/{self.tag}",
            "members": f"clans/{self.tag}/members",
            "warlog": f"clans/{self.tag}/warlog",
            "capitalraidseasons": f"clans/{self.tag}/capitalraidseasons",
            "currentwar": f"clans/{self.tag}/currentwar",
            "warleague": f"clans/{self.tag}/currentwar/leaguegroup",
            "warleaguewars": f"clans/{self.tag}/warleagues"
        }
    def _make_get_request(self, endpoint):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(self.base_url + endpoint, headers=headers)
        response.raise_for_status()
        return response.json()

    def __getattr__(self, name):
        if name in self.endpoints:
            endpoint = self.endpoints[name]
            return lambda: self._make_get_request(endpoint)
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")