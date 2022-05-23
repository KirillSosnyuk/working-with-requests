import requests

TOKEN = '2619421814940190'

class SuperHero:
    host = 'https://superheroapi.com/api/' + TOKEN + '/'

    def __init__(self, name):
        self.name = name

    def get_id(self):
        id = requests.get(self.host + f'search/{self.name}')
        self.id = int(id.json()['results'][0]['id'])
        return int(self.id)

    def get_intelligence(self):
        intelligence = requests.get(self.host + f'{self.id}/powerstats').json().get('intelligence')
        return int(intelligence)


super_heroes= {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}

for super_hero in super_heroes.keys():
    super_hero_class = SuperHero(super_hero)
    super_hero_id = super_hero_class.get_id()
    super_hero_intelligence = super_hero_class.get_intelligence()
    super_heroes[super_hero] = super_hero_intelligence

print(max(super_heroes.items(), key=lambda x: x[1]))
