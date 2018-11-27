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
TYPE_DESCRIPTION = 'It is a '
GAME_APPEARANCES = 'You can find it in the following games: '

NAME = str(QUICK_LOOK_UP.species).capitalize()
HEIGHT = '{0:.2f}'.format(QUICK_LOOK_UP.height/10)
WEIGHT = '{0:.2f}'.format(QUICK_LOOK_UP.weight/10)
TYPES = json.loads(str(QUICK_LOOK_UP.types).replace('\'', '"'))
GAMES = json.loads(str(QUICK_LOOK_UP.game_indices).replace('\'', '"'))
  
FORMATTED_VITALS = NAME_AND_VITALS.substitute(name=NAME, height=HEIGHT, weight=WEIGHT)

for i in range(0, len(TYPES)):
  if i == 0 and len(TYPES) == 1:
    TYPE_DESCRIPTION += 'pure ' + TYPES[i]['type']['name'].capitalize() + ' type.'
  else:
    if i == 0:
      TYPE_DESCRIPTION += TYPES[i]['type']['name'].capitalize() + ' type, '
    else:
      TYPE_DESCRIPTION += 'and also a ' + TYPES[i]['type']['name'].capitalize() + ' type.'

if len(GAMES) < 1:
  GAME_APPEARANCES = 'This is a very new Pokemon, and our API doesn\'t know what games it has appeared in yet'
else:
  for i in range(0, len(GAMES)):
    if len(GAMES) < 2:
      GAME_APPEARANCES +=  GAMES[i]['version']['name'].capitalize() + '.'
    else:
      if i == 0:
        GAME_APPEARANCES += '\n'  
      GAME_APPEARANCES += '* ' + GAMES[i]['version']['name'].capitalize() + '\n'



# TO-DO:
# Simple goal: Get height & weight in standard metric, type(s), and game(s) it has appeared in
# Stretch goal: Return weaknesses and strengths based on type. This is less hard than tedious.

print('\n')
print(FORMATTED_VITALS)
print('\n')
print(TYPE_DESCRIPTION)
print('\n')
print(GAME_APPEARANCES)
