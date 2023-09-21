# Usage example:
from clash_api import Clan, Player,Connect,Leagues

api_key = "your-key-here"
Connect.api_key = api_key

clan_id = "#"
player_tag = "#"

clan = Clan(clan_id)
player = Player(player_tag)
leagues = Leagues()

print(clan.info("name","tag","description"))

print(player.info("name","tag","description"))