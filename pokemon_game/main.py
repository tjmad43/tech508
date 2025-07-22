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

good_input = False
while not good_input:

    print('Do you want to choose a pokemon or get a random pokemon? (Type "choose" or "random")')
    user_choice = input()

    if user_choice.lower() == 'choose':
        good_input = True
        # Ask the user to choose a pokemon
        print('Enter your pokemon:')

        # Get the user's choice
        choice = input().lower()

    elif user_choice.lower() == 'random':
        good_input = True

        choice = random_pokemon.random_choice()

    else:
        print('Invalid input. Try again.')

print(f'Your pokemon is {choice}')

# Print the pokemon's stats
user_stats = poke_stats.get_stats(choice)

# Get a random pokemon for the CPU
cpu = random_pokemon.random_choice()
print('')
print(f'Your opponent has chosen {cpu}')
# And print it's stats
cpu_stats = poke_stats.get_stats(cpu)

