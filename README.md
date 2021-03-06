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
Each player comes in a certain format - as this module is heavily in development certain features might not work at the moment. The features that aren't working are indicated below.

* `advanced_statistics`
  1. `catchshootpoints`
  2. `driveast`
  3. `drivefta`
  4. `drivepass`
  5. `drivepf`
  6. `drivepts`
  7. `elbowtouchpoints`
  8. `overallassist`
  9. `passesmade`
  10. `passesreceived`
  11. `pointscreatedbyassist`
  12. `postpasses`
  13. `postpf`
  14. `posttouchpoints`
  15. `posttov`
  16. `postups`
  17. `potentialassist`
  18. `pullupoints`
  19. `rimfga`
  20. `rimfgm`
  21. `rimfgp`
  22. `secondaryassist`
  23. `touches`
  24. `year`
* `raw_data_seasons`
  1. `age`
  2. `ast`
  3. `blk`
  4. `dreb`
  5. `fga`
  6. `fgm`
  7. `fgp`
  8. `ftm`
  9. `gp`
  10. `gs`
  11. `min`
  12. `oreb`
  13. `pf`
  14. `playerid`
  15. `pts`
  16. `reb`
  17. `stl`
  18. `teamabr`
  19. `teamid`
  20. `threea`
  21. `threem`
  22. `threep`
  23. `tov`
  24. `year`
* `advanced_statistic_seasons`(NOT WORKING AT ALL)
  1. `ast_pct`
  2. `ast_ratio`
  3. `ast_to`
  4. `defensive_rating`
  5. `dreb_percentage`
  6. `gp`
  7. `losses`
  8. `min`
  9. `net_rating`
  10. `offensive_rating`
  11. `oreb_percentage`
  12. `pace`
  13. `pie`
  14. `playerid`
  15. `teamabr`
  16. `teamid`
  17. `tm_tov_pct`
  18. `ts_pct`
  19. `usg_pct`
  20. `win_p`
  21. `wins`
  22. `year`
* `current`
* `height`
* `id`
* `name`
* `position`
* `salary` **(NOT WORKING)**
* `weight`



