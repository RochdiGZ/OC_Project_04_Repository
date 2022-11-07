from models.round_model import Round
from models.console_style_model import Style


class Rounds(Style):
    def __init__(self):
        super().__init__()

    def display_start_new_round(self, index: int):
        self.console.rule("[bold blue]Start of the new round [/]" + str(index))

    def display_end_round(self, index: int):
        self.console.rule("[bold blue]End of the round [/]" + str(index))

    def display_round_created(self, index: int):
        self.console.rule("[bold blue]The new round [/]" + str(index) + " [bold blue]has been created[/]")

    def display_round_model(self, round_i: "Round"):
        print()
        self.console.print(round_i, style=self.style_b)
        print()
