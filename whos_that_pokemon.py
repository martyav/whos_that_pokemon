#!/usr/bin/python3

"""
whos_that_pokemon.py

A script that makes requests against the Pokemon API.
"""

import argparse
import pokebase as pb

parser = argparse.ArgumentParser()
parser.add_argument("name")
args = parser.parse_args()

print(args.name)