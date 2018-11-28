#!/usr/bin/python3

"""
whos_that_pokemon.py

A script that makes requests against the Pokemon API.
"""

from pokemon_getter import Pokemon_Getter
import argparse

PARSER = argparse.ArgumentParser()
PARSER.add_argument('name', help='The name of the Pokemon you want information on.')
ARGS = PARSER.parse_args()

# TO-DO:
# Stretch goal: Return weaknesses and strengths based on type. This is less hard than tedious.

pg = Pokemon_Getter(ARGS)

print('\n')
print(pg.formatted_vitals)
print('\n')
print(pg.type_description)
print('\n')
print(pg.game_appearances)
