class Type_Matcher:
    def __init__(self, pokemon_type):
        self.pokemon_type = pokemon_type
        self.strong_against = self.list_strength()
        self.weak_against = self.list_weakness()

    def list_weakness(self):
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
        }.get(self.pokemon_type, [])

    def list_strength(self):
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
        }.get(self.pokemon_type, [])
