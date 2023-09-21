import requests

class Connect:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.clashofclans.com/v1/"

    def _make_request(self, endpoint):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(self.base_url + endpoint, headers=headers)
        response.raise_for_status()
        return response.json()

class Clan(Connect):
    def __init__(self, tag):
        super().__init__(self.api_key)  # Access the api_key from the parent class
        self.tag = requests.utils.quote(tag)

    def info(self, *args):
        endpoint = f"clans/{self.tag}"
        self.data = self._make_request(endpoint)
        return tuple(self.data.get(arg) for arg in args)

    def members(self):
        endpoint = f"clans/{self.tag}/members"
        return self._make_request(endpoint)
        
    def warlog(self):
        endpoint = f"clans/{self.tag}/warlog"
        return self._make_request(endpoint)
    
    def currentwar(self):
        endpoint = f"clans/{self.tag}/currentwar"
        return self._make_request(endpoint)
    
    def warleague(self):
        endpoint = f"clans/{self.tag}/currentwar/leaguegroup"
        return self._make_request(endpoint)
    
    def capitalraidseasons(self):
        endpoint = f"clans/{self.tag}/capitalraidseasons"
        return self._make_request(endpoint)
    
class Player(Connect):
    def __init__(self, tag):
        super().__init__(self.api_key)  # Access the api_key from the parent class
        self.tag = requests.utils.quote(tag)

    def info(self, *args):
        endpoint = f"players/{self.tag}"
        self.data = self._make_request(endpoint)
        return tuple(self.data.get(arg) for arg in args)

    def verify(self,token):
        endpoint = f"players/{self.tag}/verifytoken"
        return requests.post(self.base_url + endpoint, data = token)

class Leagues(Connect):
    def __init__(self):
        super().__init__(self.api_key)
        
    def capitalleagues(self):
        endpoint = f"capitalleagues"
        return self._make_request(endpoint)
    
    def leagues(self):
        endpoint = f"leagues"
        return self._make_request(endpoint)

    #make the user use either leauge name or leauge id to get the leauge info
    #need to add more leauge endpoints