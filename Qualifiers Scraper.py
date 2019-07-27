import requests
from settings import apiKey

with open("matches.txt") as f:
    # Filters out any empty lines
    lobbies = list(filter(None, (line.rstrip() for line in f)))

with open('matchesOut.txt', 'w+') as fout:
    data = {}
    t = '\t'
    for i, lobby in enumerate(lobbies):
        lobbyID = lobby[len('https://osu.ppy.sh/community/matches/'):]

        req = requests.get(f'https://osu.ppy.sh/api/get_match?k={apiKey}&mp={lobbyID}')
        if req.status_code != 200:
            print('\rSomething went wrong getting info for match ID ', lobbyID)
            continue

        lobbyJson = req.json()

        for game in lobbyJson['games']:
            for score in game['scores']:
                if score['user_id'] in data.keys():
                    data[score['user_id']] = data[score['user_id']] + [score['score']]
                else:
                    data[score['user_id']] = [score['score']]

        print(f'\r[{i + 1}/{len(lobbies)}]', end='')

    for userID in data:
        fout.write(userID)
        for score in data[userID]:
            fout.write(t + score)
        fout.write('\n')
