import requests
import json

def heroes():
    response = requests.get('https://akabab.github.io/superhero-api/api/all.json').json()
    hero_list = ["Hulk", "Captain America", "Thanos"]
    hero_dict = {}
    for i in response:
        for k in range(len(hero_list)):
            if i['name'] == hero_list[k]:
               hero_dict[hero_list[k]] = i['powerstats']["intelligence"]
    print(max(hero_dict))

if __name__ == '__main__':
    heroes()

#как лучше написать? как автоматизировать нахождение "intelligence"?