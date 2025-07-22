import requests
import json
import random

def random_choice():
    # Get the list of pokemon from the API
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    pokemon_list = json.loads(response.text)['results']

    poke_names = []
    for pokemon in pokemon_list:
        poke_names.append(pokemon['name'])

    # Get the random choice
    choice = poke_names[random.randint(0, len(pokemon_list) - 1)]
    return choice


