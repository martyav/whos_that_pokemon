#!/usr/bin/python3

"""
whos_that_pokemon.py

A script that makes requests against the Pokemon API.
"""

from string import Template
import argparse
import json
import pokebase as pb

PARSER = argparse.ArgumentParser()
PARSER.add_argument('name', help='The name of the Pokemon you want information on.')
ARGS = PARSER.parse_args()

QUICK_LOOK_UP = pb.pokemon(ARGS.name)
NAME_AND_VITALS = Template('$name, a very special Pokemon. It is $height meters tall, and weighs $weight kilos.')
TYPE_AND_GAMES = 'It is a '

NAME = str(QUICK_LOOK_UP.species).capitalize()
HEIGHT = '{0:.2f}'.format(QUICK_LOOK_UP.height/10)
WEIGHT = '{0:.2f}'.format(QUICK_LOOK_UP.weight/10)
TEMP_TYPES = QUICK_LOOK_UP.types
TEMP_TYPES_STRING = str(TEMP_TYPES).replace('\'', '"')
TYPES = json.loads(TEMP_TYPES_STRING)
  
for i in range(0, len(TYPES)):
  if i == 0 and len(TYPES) == 1:
    TYPE_AND_GAMES += 'pure ' + TYPES[i]['type']['name'].capitalize() + ' type.'
  else:
    if i == 0:
      TYPE_AND_GAMES += TYPES[i]['type']['name'].capitalize() + ' type, '
    else:
      TYPE_AND_GAMES += 'and also a ' + TYPES[i]['type']['name'].capitalize() + ' type.'

FORMATTED_VITALS = NAME_AND_VITALS.substitute(name=NAME, height=HEIGHT, weight=WEIGHT)

# TO-DO:
# Simple goal: Get height & weight in standard metric, type(s), and game(s) it has appeared in
# Stretch goal: Return weaknesses and strengths based on type. This is less hard than tedious.

print(FORMATTED_VITALS)
print(TYPE_AND_GAMES)
