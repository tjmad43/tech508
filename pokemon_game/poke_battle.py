import random

def battle(pokemon1, pokemon2):
    turn = 1
    winner = ""

    # While neither pokemon have fainted, keep taking turns
    while pokemon1["hp"] > 0 and pokemon2["hp"] > 0:
        print(f'Turn #{turn}')
        print(f'{pokemon1["name"]}: {pokemon1["hp"]} hp')
        print(f'{pokemon2["name"]}: {pokemon2["hp"]} hp')

        #battle logic - figure out moves



        # Next turn
        turn += 1


    # Find which pokemon fainted and so the winner
    if pokemon1["hp"] <= 0:
        print(f'{pokemon1["name"]} fainted!')
        winner = pokemon2["name"]
    elif pokemon1["hp"] <= 0:
        print(f'{pokemon2["name"]} fainted!')
        winner = pokemon1["name"]

    return winner

