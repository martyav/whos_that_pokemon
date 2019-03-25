from string import Template
import pokebase as pb

class PokemonApiResponse:
    """An object that makes a hit to the Pokemon API & holds the results."""

    def __init__(self, command_line_args):
        self.command_line_args = command_line_args
        self.quick_look_up = pb.pokemon(command_line_args.name)
