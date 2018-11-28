class Type_Matcher:
    def __init__(self, pokemon_type):
        self.pokemon_type = pokemon_type
        self.strong_against = self.list_strength()
        self.weak_against = self.list_weakness()

    def list_weakness(self):
        return {
            'fire': ['water', 'ground'],
            'water': ['grass', 'electric'],
            'grass': ['fire'],
            'ground': ['water', 'grass'],
            'electric': ['ground']
        }.get(self.pokemon_type, [])

    def list_strength(self):
        return {
            'fire': ['grass'],
            'water': ['ground'],
            'grass': ['water', 'ground'],
            'ground': ['fire', 'electric'],
            'electric': ['water']
        }.get(self.pokemon_type, [])
