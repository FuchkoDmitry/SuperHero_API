import requests


class SuperHero:

    def __init__(self, name):
        self.name = name.title()
        self.url = 'https://superheroapi.com/api/2619421814940190'

    def get_character_id(self):
        url = f"{self.url}/search/{self.name}"
        resp = requests.get(url).json()['results']
        character_id = resp[0]['id']
        return character_id

    def get_intelligence(self):
        url = f"{self.url}/{self.get_character_id()}/powerstats"
        intelligence = requests.get(url).json()['intelligence']
        return int(intelligence)


def most_intelligence(superheroes):
    mark_of_intelligence = 0
    most_intelligence_superhero = ''
    for superhero in superheroes:
        if superhero.get_intelligence() > mark_of_intelligence:
            mark_of_intelligence = superhero.get_intelligence()
            most_intelligence_superhero = superhero.name
    return f'The most intelligence superhero: {most_intelligence_superhero}, ' \
           f'his intelligence: {mark_of_intelligence}'


if __name__ == '__main__':
    hulk = SuperHero('Hulk')
    cap_america = SuperHero('Captain America')
    thanos = SuperHero('Thanos')
    list_of_superheroes = [hulk, cap_america, thanos]
    print(most_intelligence(list_of_superheroes))


