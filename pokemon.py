from string import Template
from type_matcher import Type_Matcher
import json

class Pokemon:
    """An object that parses & formats the results from a Pokemon API hit."""

    def __init__(self, api_response):
        self.name = str(api_response.species).capitalize()
        self.height = '{0:.2f}'.format(api_response.height/10)
        self.weight = '{0:.2f}'.format(api_response.weight/10)
        self.types = json.loads(str(api_response.types).replace('\'', '"'))
        self.games = json.loads(str(api_response.game_indices).replace('\'', '"'))
        self.matcher = Type_Matcher(self.types[0]['type']['name'])
        self.strengths = self.matcher.list_strength()
        self.weaknesses = self.matcher.list_weakness()
  
        self.name_and_measurements = self.format_name_and_measurements_string()
        self.type_description = self.format_types_string()
        self.game_appearances = self.format_games_string()
        self.strengths_and_weaknesses = self.format_type_matches_string()

    def format_name_and_measurements_string(self):
        """Returns a string detailing, in plain English, the Pokemon's name, height, and weight"""
        return_text = ''

        return_text += f'{ self.name }, a very special Pokemon. It is { self.height } meters tall, and weighs { self.weight } kilos.'

        return return_text

    def format_types_string(self):
        """Returns a string detailing, in plain English, the Pokemon's types"""

        return_text = ''

        type1 = self.types[0]['type']['name'].capitalize()

        if len(self.types) == 1:
            return_text += f'It is a pure { type1 } type.'
        else:
            type2 = self.types[1]['type']['name'].capitalize()
            return_text += f'It is a { type1 } type, and also a { type2 } type.'
    
        return return_text

    def format_games_string(self):
        """Returns a string detailing, in plain English, the games the Pokemon has appeared in"""
        
        return_text = ''

        if len(self.games) < 1:
            return_text = 'This is a very new Pokemon, and our API doesn\'t know what games it has appeared in yet.'
        else:
            return_text = 'You can find it in the following games: '
        
            for i in range(0, len(self.games)):
                game = self.games[i]['version']['name'].capitalize()

                if len(self.games) < 2:
                    return_text +=  f'{ game }.'
                else:
                    if i == 0:
                        return_text += '\n'

                    return_text += f'* { game }\n'

        return return_text

    def format_type_match(self, strong_or_weak, list_of_types):
        """Formats sentences within the type match-up string"""

        return_text = ''

        if len(list_of_types) < 1:
            return_text += f'It is not { strong_or_weak } against anything.'
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


    def format_type_matches_string(self):
        """Returns a string detailing, in plain English, the types the Pokemon is strong and weak against"""

        return_text = ''

        strength_string = self.format_type_match('strong', self.strengths)
        weakness_string = self.format_type_match('weak', self.weaknesses)

        return_text +=  f'{ strength_string }{ weakness_string }'

        return return_text
