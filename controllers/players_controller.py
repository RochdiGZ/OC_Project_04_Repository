from models.players_model import Player
from views.players_view import PView


class Controller:
    """Main controller."""

    def __init__(self, player: "Player", p_view: "PView"):
        self.player = player
        self.p_view = p_view

    def add_players(self) -> list:
        return self.p_view.save_players(self.player)


if __name__ == "__main__":
    p_controller = Controller(player=Player(), p_view=PView())
    list_of_players = p_controller.add_players()
    PView().output(list_of_players)
