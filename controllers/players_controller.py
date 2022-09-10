from models.players_model import Player
from views.players_view import PView


class Controller:
    """Main controller."""

    def __init__(self, p: "Player", pv: "PView"):
        self.p = p
        self.pv = pv

    def add_players(self) -> list:
        return self.pv.save_players_in_list()


if __name__ == "__main__":
    player = Player()
    p_view = PView()
    p_controller = Controller(player, p_view)
    list_of_players = p_controller.add_players()
    p_view.output(list_of_players)
