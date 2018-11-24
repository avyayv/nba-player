# NBA Player Data into JSON

## Installation
```
pip install nba-player
```

## Usage

```
import datanba
```

### Get All Players
```
data = datanba.player_stats.AllOfBasketball(arr)
```
arr is the years that you want in the normal year format for NBA (i.e ["2018-19"])

To get all player data into JSON(suggested because you dont want to poll every single time

```
data = datanba.player_stats.AllOfBasketball(["2018-19"])
data.get_player_json("players.json")
```

To get all player data as an array(not suggested since you have to poll every single time)

```
data = datanba.player_stats.AllOfBasketball(["2018-19"])
all_players = data.get_players()
```
