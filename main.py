from models.players_model import Player
from views.players_view import PView
from controllers.players_controller import Controller

MENU1 = """  
            1.1. To print the all tournaments
            1.2. To and to print the all players in alphabetical order and by ranking
"""
MENU2 = """
            2.1. To create the tournament
            2.2. To save the tournament into the table 'tournaments'
"""
MENU3 = """
            3.1. To add a player for the tournament
            3.2. To save the all players of the tournament into the table 'players'
            3.3. To print the list of all players in the tournament, in alphabetical order and by ranking
"""
MENU4 = """
            4.1. To create the round and to generate players pairs for the round
            4.2. To enter the results when the round is complete
            4.3. To print the all rounds with the all matches of the tournament
"""


def print_players():
    p_controller = Controller(player=Player(), p_view=PView())
    list_of_players = p_controller.add_players()
    PView().output(list_of_players)


if __name__ == "__main__":
    print("-" * 15, "To print the list of players in the tournament", "-" * 16)
    print("-" * 79, MENU3, "-" * 79)
    print_players()
