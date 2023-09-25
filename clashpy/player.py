import requests

class Player:
    def __init__(self, tag, api_key):
        self.base_url = "https://api.clashofclans.com/v1/"
        self.tag = requests.utils.quote(tag)
        self.api_key = api_key
        self.endpoints = {
            "info": f"players/{self.tag}",
            "verify": f"players/{self.tag}/verifytoken"
        }
    def _make_get_request(self, endpoint):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(self.base_url + endpoint, headers=headers)
        response.raise_for_status()
        return response.json()

    def info(self,*args):
        response = self._make_get_request(self.endpoints["info"])
        return tuple(response[arg] for arg in args)
    
    def verify(self,token):
        headers={"Authorization": f"Bearer {self.api_key}"}
        response=requests.post(self.base_url+self.endpoints["verify"],headers=headers,json={"token":token})
        response.raise_for_status()
        return response.json()["status"]=="ok"