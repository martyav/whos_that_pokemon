from string import Template
import pokebase as pb
import json

class Pokemon_Getter:
    """
    An object that makes a hit to the Pokemon API & holds the results.

    It contains several methods for formatting the information from the results.
    """
    def __init__(self, command_line_args):
        self.command_line_args = command_line_args
        self.quick_look_up = pb.pokemon(command_line_args.name)
        self.name_and_vitals = Template('$name, a very special Pokemon. It is $height meters tall, and weighs $weight kilos.')

        self.name = str(self.quick_look_up.species).capitalize()
        self.height = '{0:.2f}'.format(self.quick_look_up.height/10)
        self.weight = '{0:.2f}'.format(self.quick_look_up.weight/10)
        self.types = json.loads(str(self.quick_look_up.types).replace('\'', '"'))
        self.games = json.loads(str(self.quick_look_up.game_indices).replace('\'', '"'))
  
        self.formatted_vitals = self.name_and_vitals.substitute(name=self.name, height=self.height, weight=self.weight)
        self.type_description = self.format_types_string()
        self.game_appearances = self.format_games_string()

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