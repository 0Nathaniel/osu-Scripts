import requests
from settings import apiKey

file = open("mappool.txt")
mappool = []

for line in file:
	parts = line.split('\n')
	mappool.append(parts[0])
file.close()

fileOut = open('mappoolOut.txt', 'w+')
for bmap in mappool:
	bmapId = bmap[len('https://osu.ppy.sh/b/'):]
	r = requests.get(f'https://osu.ppy.sh/api/get_beatmaps?k={apiKey}&b={bmapId}')
	rJson = r.json()[0]
	t = '\t'
	#outputString += f'{rJson['beatmap_id']}\t{rJson['atrist']}\t{rJson['title']}\t{rJson['version']}\t{rJson['creator']}\t{math.round(float(rJson['difficultyrating']),2)}\t{rJson['bpm']}\t{rJson['total_length']}\n'
	fileOut.write('https://osu.ppy.sh/b/' + rJson['beatmap_id'] + t 
					+ rJson['artist'] + t
					+ rJson['title'] + t
					+ rJson['version'] + t
					+ rJson['creator'] + t
					+ str(round(float(rJson['difficultyrating']), 2)) + t
					+ rJson['bpm'] + t
					+ rJson['total_length'] + t
					+ '\n')
fileOut.close()