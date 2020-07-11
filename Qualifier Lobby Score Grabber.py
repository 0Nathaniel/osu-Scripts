import requests
from settings import apiKey
import sys
import json
import os

api_url = lambda lobby_id : f'https://osu.ppy.sh/api/get_match?k={apiKey}&mp={lobby_id}'
user_scores = {}

if __name__ == "__main__":
    lobby_id = sys.argv[1]
    req = requests.get(api_url(lobby_id))
    if req.status_code != 200:
        print('\rSomething went wrong with lobby id', lobby_id)
        quit()
    #print(len(req.json()['games']))
    for game in req.json()['games']:
        for user_score in game['scores']:
            if user_score['user_id'] not in user_scores:
                user_scores[user_score['user_id']] = []
            
            user_scores[user_score['user_id']].append(user_score['score'])
    
    with open("scores.txt", 'w') as f:
        for key in user_scores:
            output_string = key + '\t'
            for score in user_scores[key]:
                output_string += score + '\t'
            output_string = output_string[:-1]
            output_string += '\n'
            f.write(output_string)