import requests
from settings import apiKey

with open("players.txt") as f:
    # Filters out any empty lines
    players = list(filter(None, (line.rstrip() for line in f)))

with open('playersOut.txt', 'w+') as fout:
    for i, player in enumerate(players):
        req = requests.get(f'https://osu.ppy.sh/api/get_user?k={apiKey}&u={player}')
        
        if req.status_code != 200:
            print('\rSomething went wrong getting info for', player)
            continue
        
        playerJson = req.json()[0]
        fout.write(playerJson['username'] + ', ' + playerJson['user_id'] + ', ' + playerJson['country'] + '\n')
        
        print(f'\r[{i + 1}/{len(players)}]', end='')
