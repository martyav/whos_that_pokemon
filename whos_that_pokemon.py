#!/usr/bin/python3

"""
whos_that_pokemon.py

A script that makes requests against the Pokemon API.
"""

from string import Template
import argparse
import pokebase as pb

PARSER = argparse.ArgumentParser()
PARSER.add_argument('name', help='The name of the Pokemon you want information on.')
ARGS = PARSER.parse_args()
QUICK_LOOK_UP = pb.pokemon(ARGS.name)
TEMPLATE = Template('$name, a very special Pokemon.')
FORMATTED = TEMPLATE.substitute(name=QUICK_LOOK_UP.species[0].upper() + QUICK_LOOK_UP.species[1:])

# TO-DO:
# Simple goal: Get height & weight in standard metric, type(s), and game(s) it has appeared in
# Stretch goal: Return weaknesses and strengths based on type. This is less hard than tedious.

print(FORMATTED)
