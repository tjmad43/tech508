import requests
import json

import random_pokemon
import poke_stats

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

for pokemon in pokemon_list:
    print(pokemon['name'])

# Ask the user to choose a pokemon
print('Enter your pokemon:')

# Get the user's choice
choice = input().lower()
print(type(choice))

poke_stats.get_stats(choice)

cpu = random_pokemon.random_choice()
print('')
print(f'Your opponent has chosen {cpu}')

poke_stats.get_stats(cpu)