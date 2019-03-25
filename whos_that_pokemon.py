#!/usr/bin/python3

"""
whos_that_pokemon.py

A script that makes requests against the Pokemon API.
"""

from getter import PokemonApiResponse
from pokemon import Pokemon
from formatter import Formatter
import argparse

PARSER = argparse.ArgumentParser()
PARSER.add_argument('name', help='The name of the Pokemon you want information on.')
ARGS = PARSER.parse_args()

response = PokemonApiResponse(ARGS)
pokemon = Pokemon(response.quick_look_up)
fm = Formatter()

print('\n')
print(fm.format_name_and_measurements_string(pokemon))
print('\n')
print(fm.format_types_string(pokemon))
print('\n')
print(fm.format_type_matches_string(pokemon))
print('\n')
print(fm.format_games_string(pokemon))
