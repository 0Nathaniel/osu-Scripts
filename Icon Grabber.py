import time
import requests
import os
from settings import apiKey

urlprefix = 'https://osu.ppy.sh/images/flags/'
directory = 'icons'

if not os.path.exists(directory):
    os.makedirs(directory)

with open("players.txt") as f:
    # Filters out any empty lines
    ids = list(filter(None, (line.rstrip() for line in f)))

for i, id in enumerate(ids):
    req = requests.get(f'https://osu.ppy.sh/api/get_user?k={apiKey}&u={id}&m=0')
    if req.status_code != 200:
        print('\rSomething went wrong getting info for', id)
        continue
    country = req.json()[0]['country']
    username = req.json()[0]['username']

    img_data = requests.get(urlprefix + country + ".png").content
    with open(f'{directory}/{username}.png', 'wb') as handler:
        handler.write(img_data)

    print(f'\r[{i + 1}/{len(ids)}]', end='')
