# Clashpy Python Package

The **Clashpy** Python package provides a simple and convenient way to interact with the Clash of Clans API, allowing you to retrieve information about clans and players in the Clash of Clans game.

## Installation

You can install the Clashpy package using pip:

```bash
pip install clashpy
```

## Usage

1. Import the necessary classes from the package:

```python
import clashpy

api_key = "your_api_key_here"
```

2. Create an instance of the `Connect` class with your API key:

```python
connect = clashpy.Connect(api_key)
```

3. Create instances of `Clan` or `Player` using the `clan` and `player` methods of the `Connect` instance:

```python
# Example for Clan
clan_id = "#2YVQ0VJ8P"
clan = connect.clan(clan_id)
members, chat = clan.info("members", "chatLanguage")
warlog = clan.warlog()

# Example for Player
player_tag = "#PJ2ULUGQ0"
my_player = connect.player(player_tag)
heroes, exp = my_player.info("heroes", "expLevel")
```

4. Use the created instances to retrieve information about clans and players.

## Classes

### `Connect`

The `Connect` class is used to create instances of the `Clan` and `Player` classes, and takes your Clash of Clans API key as an argument.

#### Methods:

- `clan(tag)`: Create an instance of the `Clan` class with the specified clan tag.
- `player(tag)`: Create an instance of the `Player` class with the specified player tag.

### `Clan`

The `Clan` class allows you to retrieve information about a Clash of Clans clan.

#### Methods:

- `info(*args)`: Retrieve clan information for the specified attributes. Pass attribute names as arguments to get specific data.
- `members()`: Retrieve a list of clan members.
- `warlog()`: Retrieve the war log for the clan.
- `capitalraidseasons()`: Retrieve the capital raid seasons for the clan.
- `currentwar()`: Retrieve information about the clan's current war.
- `warleague()`: Retrieve information about the clan's current war league group.
- `warleaguewars()`: Retrieve information about the clan's war league wars.

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
import clashpy

api_key = "your_api_key_here"
connect = clashpy.Connect(api_key)

# Retrieve clan and player information
clan_id = "#2YVQ0VJ8P"
clan = connect.clan(clan_id)
members, chat = clan.info("members", "chatLanguage")
warlog = clan.warlog()

player_tag = "#PJ2ULUGQ0"
my_player = connect.player(player_tag)
heroes, exp = my_player.info("heroes", "expLevel")
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests on the GitHub repository.

## License

This package is open-source and available under the [MIT License](LICENSE).