# osu-Scripts
Scripts to help with tournament moderation/administration.

**Player Verification Formatter**  
Takes a list of player names or IDS and outputs their name, ID and ISO country code.
```
Input (players.txt) | Output (playersOut.txt)    
------------------- | ---------------------------
idke                | idke, 4650315, US          
Vaxei               | Vaxei, 4787150, US         
FreddieBenson       | Freddie Benson, 7342622, US
FlyingTuna          | FlyingTuna, 9224078, KR    
```

**Avatar Grabber**  
Takes a list of player IDS and outputs a `<playerusername>.jpg` for each player. Ready to be used in the tourney client.

**Mappool Formatter**  
Takes in a list of beatmap URLs and outputs a bunch of info about the map.
```
Input (mappool.txt)         | Output (mappoolOut.txt)                                                                
--------------------------- | ---------------------------------------------------------------------------------------
https://osu.ppy.sh/b/397535 | https://osu.ppy.sh/b/397535	Kuba Oms	My Love	Insane	W h i t e	3.81	128	224             
https://osu.ppy.sh/b/714001 | https://osu.ppy.sh/b/714001	Reol	No title	jieusieu's Lemur	VINXIS	6.85	200	70          
https://osu.ppy.sh/b/351189 | https://osu.ppy.sh/b/351189	cYsmix feat. Emmy	Tear Rain	Insane	jonathanlfj	3.79	128	240
https://osu.ppy.sh/b/736215 | https://osu.ppy.sh/b/736215	Panda Eyes & Teminite	Highscore	Game Over	Fort	7.37	110	257
```
Note: `mappoolOut.txt` is tab separated and can be pasted into Excel / Google Sheets

# Usage
Create a file named `settings.py` containing your [osu! api key](https://osu.ppy.sh/p/api) in the format:  
`apiKey = '<api token>'`

## Player Verification Formatter
1. Create a file named `players.txt` containing one player name per line.  
1. Run the script: `python "Player Verification Formatter.py"`.  
1. A file named `playersOut.txt` will be created containing the output.

## Avatar Grabber
1. Create a file named `players.txt` containing one player name per line.  
1. Run the script: `python "Avatar Grabber.py"`.  
1. A directory names `icons/` will be created containing files for each users avatar.

## Mappool Formatter
1. Create a file named `mappool.txt` containing one beatmap URL per line.  URLs can be old or new style, but must 
link to a beatmap, not a map set.
E.g. `https://osu.ppy.sh/b/397535` or `https://osu.ppy.sh/beatmapsets/163112#osu/397535`.  
1. Run the script: `python "Mappool Formatter.py"`.  
1. A file named `mappoolOut.txt` will be created containing the output.
