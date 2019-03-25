class Formatter:
    """A class that formats Pokemon stats"""
    
    def format_name_and_measurements_string(self, pokemon):
        """Returns a string detailing, in plain English, the Pokemon's name, height, and weight"""
        return_text = ''

        return_text += f'{ pokemon.name }, a very special Pokemon. It is { pokemon.height } meters tall, and weighs { pokemon.weight } kilos.'

        return return_text

    def format_types_string(self, pokemon):
        """Returns a string detailing, in plain English, the Pokemon's types"""

        return_text = ''

        type1 = pokemon.types[0]['type']['name'].capitalize()

        if len(pokemon.types) == 1:
            return_text += f'It is a pure { type1 } type.'
        else:
            type2 = pokemon.types[1]['type']['name'].capitalize()
            return_text += f'It is a { type1 } type, and also a { type2 } type.'
    
        return return_text

    def format_games_string(self, pokemon):
        """Returns a string detailing, in plain English, the games the Pokemon has appeared in"""
        
        return_text = ''

        if len(pokemon.games) < 1:
            return_text = 'This is a very new Pokemon, and our API doesn\'t know what games it has appeared in yet.'
        else:
            return_text = 'You can find it in the following games: '
        
            for i in range(0, len(pokemon.games)):
                game = pokemon.games[i]['version']['name'].capitalize()

                if len(pokemon.games) < 2:
                    return_text +=  f'{ game }.'
                else:
                    if i == 0:
                        return_text += '\n'

                    return_text += f'* { game }\n'

        return return_text

    """Putting a pin in the below funcs"""

    def format_type_match(self, strong_or_weak, list_of_types):
        """Formats sentences within the type match-up string"""

        return_text = ''

        if len(list_of_types) < 1:
            return_text += f'It is not { strong_or_weak } against anything. '
        else:
            for i in range(0, len(list_of_types)):
                if len(list_of_types) < 2:
                    return_text += f'It is { strong_or_weak } against { list_of_types[i].capitalize() }. '
                else:
                    if i == 0:
                        return_text += f'It is { strong_or_weak } against { list_of_types[i].capitalize() }, '
                    elif i == len(list_of_types) - 1:
                        return_text += f'and { list_of_types[i].capitalize() }. '
                    else:
                        return_text += f'{ list_of_types[i].capitalize() }, '
        
        return return_text


    def format_type_matches_string(self, strengths, weaknesses):
        """Returns a string detailing, in plain English, the types the Pokemon is strong and weak against"""

        return_text = ''

        strength_string = self.format_type_match('strong', strengths)
        weakness_string = self.format_type_match('weak', weaknesses)

        return_text +=  f'{ strength_string }{ weakness_string }'

        return return_text
