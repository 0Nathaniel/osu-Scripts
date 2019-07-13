import requests
from settings import apiKey
file = open("players.txt")
players = []

for line in file:
	parts = line.split('\n')
	players.append(parts[0])
file.close()

fileOut = open('playersOut.txt', 'w+')
for player in players:
		r = requests.get(f'https://osu.ppy.sh/api/get_user?k={apiKey}&u={player}')
		if not r.json():
			print('User',player,'does not exist!')
			continue
		rJson = r.json()[0]
		fileOut.write(player + ', ' + rJson['user_id'] + ', ' + rJson['country'] + '\n')
fileOut.close()
