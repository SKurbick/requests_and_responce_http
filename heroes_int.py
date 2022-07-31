import requests
from pprint import pprint

url = "https://akabab.github.io/superhero-api/api/all.json"
resp = requests.get(url)
# pprint(resp.json()['id'])
hulk_intel = {}
captain_am_intel = {}
thanos_intel = {}
heroes = [hulk_intel, captain_am_intel, thanos_intel]
for res in resp.json():
    if res['name'] == 'Thanos':
        thanos_intel[res['name']] = res['powerstats']
    if res['name'] == 'Hulk':
        hulk_intel[res['name']] = res['powerstats']
    if res['name'] == 'Captain America':
        captain_am_intel[res['name']] = res['powerstats']
max_intel = (max(hulk_intel['Hulk']['intelligence'], captain_am_intel['Captain America']['intelligence'],
                 thanos_intel['Thanos']['intelligence']))
for hero in heroes:
    for her in hero.items():
        if her[1]['intelligence'] == max_intel:
            print(f'{her[0]} have max intellegence: {max_intel}')
