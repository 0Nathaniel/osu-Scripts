import requests
import re
from settings import apiKey

with open("mappool.txt") as f:
    # Filters out any empty lines
    mappool = list(filter(None, (line.rstrip() for line in f)))

with open('mappoolOut.txt', 'w+') as fout:
    for i, bmap in enumerate(mappool):
        # Finds the last digit in the url string
        bmapId = re.findall(r'\d+', bmap)[-1]
        
        req = requests.get(f'https://osu.ppy.sh/api/get_beatmaps?k={apiKey}&b={bmapId}')
        if req.status_code != 200:
            print('\rSomething went wrong getting info for beatmap ID ', bmapId)
            continue
        
        bmapJson = req.json()[0]
        t = '\t'
        fout.write('https://osu.ppy.sh/b/' + bmapId + t
                   + bmapJson['creator'] + t
                   + str(round(float(bmapJson['difficultyrating']), 2)) + t
                   + bmapJson['bpm'] + t
                   + bmapJson['total_length']
                   + '\n')

        print(f'\r[{i + 1}/{len(mappool)}]', end='')
