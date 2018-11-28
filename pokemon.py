from string import Template
import json

class Pokemon:
    """An object that parses & formats the results from a Pokemon API hit."""

    def __init__(self, api_response):
        self.name = str(api_response.species).capitalize()
        self.height = '{0:.2f}'.format(api_response.height/10)
        self.weight = '{0:.2f}'.format(api_response.weight/10)
        self.types = json.loads(str(api_response.types).replace('\'', '"'))
        self.games = json.loads(str(api_response.game_indices).replace('\'', '"'))
  
        self.name_and_measurements = self.format_name_and_measurements_string()
        self.type_description = self.format_types_string()
        self.game_appearances = self.format_games_string()

    def format_name_and_measurements_string(self):
        """Returns a string detailing, in plain English, the Pokemon's name, height, and weight"""

        name_and_vitals = Template('$name, a very special Pokemon. It is $height meters tall, and weighs $weight kilos.')
        return_text = name_and_vitals.substitute(name=self.name, height=self.height, weight=self.weight)

        return return_text

    def format_types_string(self):
        """Returns a string detailing, in plain English, the Pokemon's types"""

        return_text = ''

        if len(self.types) == 1:
            temp_text = Template('It is a pure $type type.')
            return_text = temp_text.substitute(type=self.types[0]['type']['name'].capitalize())
        else:
            temp_text = Template('It is a $type1 type, and also a $type2 type.')
            return_text = temp_text.substitute(type1=self.types[0]['type']['name'].capitalize(), type2=self.types[1]['type']['name'].capitalize())
    
        return return_text

    def format_games_string(self):
        """Returns a string detailing, in plain English, the games the Pokemon has appeared in"""
        
        return_text = ''

        if len(self.games) < 1:
            return_text = 'This is a very new Pokemon, and our API doesn\'t know what games it has appeared in yet.'
        else:
            return_text = 'You can find it in the following games: '
        
            for i in range(0, len(self.games)):
                if len(self.games) < 2:
                    return_text +=  self.games[i]['version']['name'].capitalize() + '.'
                else:
                    if i == 0:
                        return_text += '\n'

                    return_text += '* ' + self.games[i]['version']['name'].capitalize() + '\n'

        return return_text
