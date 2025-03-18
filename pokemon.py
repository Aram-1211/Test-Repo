

"""
Exercise 3.2.v2: Simulate a Turn-Based Battle (Updated Stub)
"""

import requests
import random

def calculate_stat(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's stat at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)

def calculate_hp(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's HP at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)

def calculate_damage(attacker_stats, defender_stats, level=50, base_power=60):
    """Calculate battle damage using standard formula."""
    return int((((2 * level * 0.4 + 2) * attacker_stats['attack'] * base_power) 
                / (defender_stats['defense'] * 50)) + 2)

def get_pokemon(pokemon):
    api_get = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}")
    return api_get.json()


def get_stats(pokemon):
    base = {stat['stat']['name']: stat['base_stat'] for stat in pokemon['stats']}

    return {
        'name': pokemon['name'], 'attack': calculate_stat(base['attack']), 'defense': calculate_stat(base['defense']), 'hp': calculate_hp(base['hp']), 'spd': calculate_stat(base['speed']),
    }

def simulate_battle(pokemon1, pokemon2):
    """Simulate a battle between two Pokémon."""
    # TODO: Fetch Pokémon Data
    # - Create lowercase URLs for both Pokémon
    p1data = get_pokemon(pokemon1)
    p2data = get_pokemon(pokemon2)
    # - Make GET requests and check response codes
    # - Extract JSON data if successful
    
    # TODO: Calculate Initial Stats
    p1stats = get_stats(p1data)
    p2stats = get_stats(p2data)
    # - Use calculate_stat() for attack/defense/speed
    # - Use calculate_hp() for HP stats
    # - Store in dictionaries

    # TODO: Initialise Battle Display
    # - Show battle start message
    print(f"{pokemon1} vs {pokemon2}")
    # - Display initial HP values
    print(f"{pokemon1} HP: {p1stats['hp']}")
    print(f"{pokemon2} HP: {p2stats['hp']}")

    # TODO: Determine First Attacker
    # - Compare speed stats
    if (p1stats['spd'] > p2stats['spd']):
        attacker = p1stats
        defender = p2stats
    elif (p1stats['spd'] < p2stats['spd']):
        attacker = p2stats
        defender = p1stats
    else:
        coin = random.choice(["0", "1"])
        if coin == 0:
            attacker = p1stats
            defender = p2stats
        else:
            attacker = p2stats
            defender = p1stats

    print(f"{attacker['name']} goes first")

    # - Set up attacker/defender variables
    # - Store corresponding stats

    # TODO: Battle Loop
    round = 1
    while p1stats['hp'] > 0 and p2stats['hp'] > 0:
        print(f"Round {round}")
        damage = calculate_damage(attacker, defender)
        defender['hp'] -= damage
        print(f"{attacker['name']} dealt {damage} damage")
        print(f"{defender['name']} has {max(0, defender['hp'])} HP left")
        if (defender['hp'] <= 0):
            print(f"{defender['name']} fainted")
            print(f"{attacker['name']} wins")
            return
        
        attacker, defender = defender, attacker
        round += 1

    # - Track round numbers
    # - While both have HP > 0:
    #   - Show current round
    #   - Calculate and deal damage
    #   - Check for fainting (==< 0)
    #   - Show remaining HP
    #   - Swap roles
    #   - Increment round

    # TODO: End Battle
    # - Show victory message
    # - Display winner

if __name__ == "__main__":
    simulate_battle("eevee", "jigglypuff")

"""
Helper Info:
- Use calculate_damage() for proper battle mechanics
- Remember to handle API response errors
- Keep battle display clear and informative
"""