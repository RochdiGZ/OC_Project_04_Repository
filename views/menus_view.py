from rich.console import Console
from models.console_style_model import Style


class Menus(Style):
    def __init__(self):
        super().__init__()

    def choice(self, index: int) -> int:
        print()
        try:
            self.console.print("Please, enter your choice from 1 to " + str(index), end=" : ", style=self.style_y)
            number = int(input())
            if number in range(1, index+1):
                return number
            else:
                raise ValueError
        except ValueError:
            self.console.print("Please, you must reenter a integer number between 1 and " + str(index) + "!",
                               style=self.style_r)
            return self.choice(index)

    def display_main_menu(self):
        print()
        console = Console(width=40)
        console.print("Main menu", style=self.style_g, justify="center")
        console.print("1. Players", style=self.style_b, justify="left")
        console.print("2. Tournaments", style=self.style_b, justify="left")
        console.print("3. Reports", style=self.style_b, justify="left")
        console.print("4. Exit", style=self.style_b, justify="left")

    def display_players_menu(self):
        print()
        console = Console(width=40)
        console.print("Players menu", style=self.style_r, justify="center")
        console.print("1. Add a player", style=self.style_g, justify="left")
        console.print("2. Update a player ranking", style=self.style_g, justify="left")
        console.print("3. Back to main menu", style=self.style_g, justify="left")

    def display_tournaments_menu(self):
        print()
        console = Console(width=40)
        console.print("Tournaments menu", style=self.style_b, justify="center")
        console.print("1. Create and start a tournament", style=self.style_r, justify="left")
        console.print("2. Select and start a tournament", style=self.style_r, justify="left")
        console.print("3. Back to main menu", style=self.style_g, justify="left")

    def display_reports_menu(self):
        print()
        console = Console(width=80)
        console.print("Reports menu", style=self.style_r, justify="center")
        console.print("1. Display the sorted all players by name", style=self.style_g, justify="left")
        console.print("2. Display the sorted all players by ranking", style=self.style_g, justify="left")
        console.print("3. Display the all tournaments", style=self.style_y, justify="left")
        console.print("4. Display sorted players by name and rounds matches of a tournament", style=self.style_b,
                      justify="left")
        console.print("5. Display sorted players by ranking and rounds matches of a tournament", style=self.style_b,
                      justify="left")
        console.print("6. Back to main menu", style=self.style_g, justify="left")
