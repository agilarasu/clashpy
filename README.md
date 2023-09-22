# Clashpy Python Package

The **Clashpy** Python package provides a simple and convenient way to interact with the Clash of Clans API, allowing you to retrieve information about clans and players in the Clash of Clans game.

## Installation

You can install the ClashAPI package using pip:

```bash
pip install clashpy
```

## Usage

1. Import the necessary classes from the package:

```python
from clashpy import Clan, Player, Connect
```

2. Set your Clash of Clans API key using `Connect.api_key`:

```python
api_key = "your_api_key_here"
Connect.api_key = api_key
```

3. Create instances of `Clan` or `Player` without passing the API key explicitly:

```python
# Example for Clan
clan_id = "#2YVQ0VJ8P"
clan = Clan(clan_id)
members, chat = clan.info("members", "chatLanguage")

# Example for Player
player_tag = "#PJ2ULUGQ0"
my_player = Player(player_tag)
heroes, exp = my_player.info("heroes", "expLevel")
```

4. Use the created instances to retrieve information about clans and players.

## Classes

### `Clan`

The `Clan` class allows you to retrieve information about a Clash of Clans clan.

#### Methods:

- `info(*args)`: Retrieve clan information for the specified attributes. Pass attribute names as arguments to get specific data.

#### Available Arguments:

- `tag`
- `name`
- `type`
- `description`
- `location`
- `isFamilyFriendly`
- `badgeUrls`
- `clanLevel`
- `clanPoints`
- `clanBuilderBasePoints`
- `clanVersusPoints`
- `clanCapitalPoints`
- `capitalLeague`
- `requiredTrophies`
- `warFrequency`
- `warWinStreak`
- `warWins`
- `isWarLogPublic`
- `warLeague`
- `members`
- `memberList`
- `labels`
- `requiredBuilderBaseTrophies`
- `requiredVersusTrophies`
- `requiredTownhallLevel`
- `clanCapital`
- `chatLanguage`

### `Player`

The `Player` class allows you to retrieve information about a Clash of Clans player.

#### Methods:

- `info(*args)`: Retrieve player information for the specified attributes. Pass attribute names as arguments to get specific data.

#### Available Arguments:

- `tag`
- `name`
- `townHallLevel`
- `townHallWeaponLevel`
- `expLevel`
- `trophies`
- `bestTrophies`
- `warStars`
- `attackWins`
- `defenseWins`
- `builderHallLevel`
- `builderBaseTrophies`
- `versusTrophies`
- `bestBuilderBaseTrophies`
- `bestVersusTrophies`
- `versusBattleWins`
- `role`
- `warPreference`
- `donations`
- `donationsReceived`
- `clanCapitalContributions`
- `clan`
- `league`
- `builderBaseLeague`
- `achievements`
- `playerHouse`
- `labels`
- `troops`
- `heroes`
- `spells`

## Example

```python
from clashpy import Clan, Player, Connect

# Set your API key
api_key = "your_api_key_here"
Connect.api_key = api_key

# Retrieve clan and player information
clan_id = "#2YVQ0VJ8P"
clan = Clan(clan_id)
members, chat = clan.info("members", "chatLanguage")

player_tag = "#PJ2ULUGQ0"
my_player = Player(player_tag)
heroes, exp = my_player.info("heroes", "expLevel")
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests on the GitHub repository

## License

This package is open-source and available under the [MIT License](LICENSE).
```
