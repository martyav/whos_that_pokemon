#!/usr/bin/python3

"""
whos_that_pokemon.py

A script that makes requests against the Pokemon API.
"""

from getter import Getter
from pokemon import Pokemon
import argparse

PARSER = argparse.ArgumentParser()
PARSER.add_argument('name', help='The name of the Pokemon you want information on.')
ARGS = PARSER.parse_args()

# TO-DO:
# Stretch goal: Return weaknesses and strengths based on type. This is less hard than tedious.

getter = Getter(ARGS)
pokemon = Pokemon(getter.quick_look_up)

print('\n')
print(pokemon.name_and_measurements)
print('\n')
print(pokemon.type_description)
print('\n')
print(pokemon.strengths_and_weaknesses)
print('\n')
print(pokemon.game_appearances)
