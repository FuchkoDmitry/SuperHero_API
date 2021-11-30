import requests


def get_character_id(hero):
    url = f"https://superheroapi.com/api/{TOKEN}/search/{hero}"
    hero_specifications = requests.get(url).json()['results']
    for specifications in hero_specifications:
        if specifications['name'] == hero:
            character_id = specifications['id']
            return character_id


def get_intelligence(hero):
    url = f"https://superheroapi.com/api/{TOKEN}/{get_character_id(hero)}/powerstats"
    intelligence = int(requests.get(url).json()['intelligence'])
    return intelligence


def most_intelligence_superhero(list_of_superheroes):
    most_intelligence = 0
    most_intelligence_hero = ''
    for hero in list_of_superheroes:
        if get_intelligence(hero) > most_intelligence:
            most_intelligence = get_intelligence(hero)
            most_intelligence_hero = hero
    return f'The most intelligence hero: {most_intelligence_hero},' \
           f' his intelligence: {most_intelligence}'


if __name__ == '__main__':
    TOKEN = '2619421814940190'
    print(most_intelligence_superhero(['Captain America', 'Hulk', 'Thanos']))
