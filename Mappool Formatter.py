import requests
from settings import apiKey

with open("mappool.txt") as f:
    # Filters out any empty lines
    mappool = list(filter(None, (line.rstrip() for line in f)))

with open('mappoolOut.txt', 'w+') as fout:
    for i, bmap in enumerate(mappool):
        bmapId = bmap[len('https://osu.ppy.sh/b/'):]
        
        req = requests.get(f'https://osu.ppy.sh/api/get_beatmaps?k={apiKey}&b={bmapId}')
        if req.status_code != 200:
            print('\rSomething went wrong getting info for beatmap ID ', bmapId)
            continue
        
        bmapJson = req.json()[0]
        t = '\t'
        fout.write(bmap + t
                   + bmapJson['artist'] + t
                   + bmapJson['title'] + t
                   + bmapJson['version'] + t
                   + bmapJson['creator'] + t
                   + str(round(float(bmapJson['difficultyrating']), 2)) + t
                   + bmapJson['bpm'] + t
                   + bmapJson['total_length'] + t
                   + '\n')

        print(f'\r[{i + 1}/{len(mappool)}]', end='')
