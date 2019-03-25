import json

'''
TO-DO

Use existing libraries for heavy lifting
Refactor formating methods into separate module
'''

class Pokemon:
    """An object that parses the results from a Pokemon API hit."""

    def __init__(self, api_response):
        self.name = str(api_response.species).capitalize()
        self.height = '{0:.2f}'.format(api_response.height/10)
        self.weight = '{0:.2f}'.format(api_response.weight/10)
        self.types = json.loads(str(api_response.types).replace('\'', '"'))
        self.games = json.loads(str(api_response.game_indices).replace('\'', '"'))
        self.strengths = self.list_strength(self.types[0]['type']['name'])
        self.weaknesses = self.list_weakness(self.types[0]['type']['name'])

        if len(self.types) > 1:
            self.strengths.extend(self.list_strength(self.types[1]['type']['name']))

        if len(self.types) > 1:
            self.strengths.extend(self.list_weakness(self.types[1]['type']['name']))

    def list_weakness(self, pokemon_type):
        return {
            'fire': ['water', 'ground', 'rock'],
            'water': ['grass', 'electric'],
            'grass': ['fire', 'bug', 'flying', 'poison', 'ice'],
            'ground': ['water', 'grass'],
            'electric': ['ground'],
            'normal': ['fighting'],
            'fighting': ['psychic', 'flying'],
            'rock': ['fighting', 'grass', 'ground', 'steel', 'water'],
            'steel': ['fire', 'fighting', 'ground'],
            'ice': ['fighting', 'fire', 'rock', 'steel'],
            'dark': ['bug', 'fighting', 'fairy'],
            'bug': ['fire', 'flying', 'rock'],
            'flying': ['rock', 'electric', 'ice'],
            'dragon': ['fairy', 'dragon', 'ice'],
            'psychic': ['bug', 'dark', 'ghost'],
            'ghost': ['dark', 'ghost'],
            'poison': ['ground', 'psychic']
        }.get(pokemon_type, [])

    def list_strength(self, pokemon_type):
        return {
            'fire': ['grass', 'ice', 'steel', 'bug'],
            'water': ['ground', 'fire', 'rock'],
            'grass': ['water', 'ground', 'rock'],
            'ground': ['fire', 'electric'],
            'electric': ['water', 'flying'],
            'normal': [],
            'fighting': ['normal', 'rock', 'steel', 'ice', 'dark'],
            'rock': ['bug', 'fire', 'ice', 'flying'],
            'steel': ['ice', 'rock'],
            'ice': ['dragon', 'flying', 'grass', 'ground'],
            'dark': ['psychic', 'ghost'],
            'bug': ['dark', 'grass', 'psychic'],
            'flying': ['bug', 'fighting', 'grass'],
            'dragon': ['dragon'],
            'psychic': ['fighting', 'poison'],
            'ghost': ['ghost', 'psychic'],
            'poison': ['grass']
        }.get(pokemon_type, [])
