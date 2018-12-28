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

To get all player data into JSON

```
data = datanba.player_stats.AllOfBasketball(["2018-19"])
data.gather("players.json", exists=False)
```
Only use this if you have nothing in your players.json file or it does not exist at all.

However, since you will be polling a lot, you might have your connection work or the NBA stats API will limit you, so if scraping stops in the middle, you can change your code to:

```
data = datanba.player_stats.AllOfBasketball(["2018-19"])
data.gather("players.json", exists=True)
```
Then, scraping will continue from where it left off.

### Use Player JSON data

After polling once, you can reuse the output form the JSON file as long as you would like(until the data that you have polled has become old), by using these commands.

```
import datanba.player_stats as datanba
data = datanba.AllOfBasketball(["2018-19"])
players = data.players_from_json('players.json')
```
Now you have all NBA players in your `players` variable.

### Player Data Format
Each player comes in a certain format - as this module is heavily in development certain features might not work at the moment.

advanced_statistics
  catchshootpoints
  driveast
  drivefta
  drivepass
  drivepf
  drivepts
  elbowtouchpoints
  overallassist
  passesmade
  passesreceived
  pointscreatedbyassist
  postpasses
  postpf
  posttouchpoints
  posttov
  postups
  potentialassist
  pullupoints
  rimfga
  rimfgm
  imfgp
  secondaryassist
  touches
  year

offensive_seasons
  age
  ast
  blk
  dreb
  fga
  fgm
  fgp
  ftm
  gp
  gs
  min
  oreb
  pf
  playerid
  pts
  reb
  stl
  teamabr
  teamid
  threea
  threem
  threep
  tov
  year

defensive_seasons
  age(NOT WORKING)
  gs(NOT WORKING)
  ast_pct
  ast_ratio
  ast_to
  defensive_rating
  dreb_percentage
  gp
  losses
  min
  net_rating
  offensive_rating
  oreb_percentage
  pace
  pie
  playerid
  teamabr
  teamid
  tm_tov_pct
  ts_pct
  usg_pct
  win_p
  wins
  year
  
current
height
id
name
position
salary(NOT WORKING)
weight



