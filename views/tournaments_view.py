import re
from models.console_style_model import Style
from models.tournament_model import Tournament
from tinydb import TinyDB

NAME_REGEX = "^[A-Z]{1}[a-z]+$"
DATE_REGEX = "^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$"
TIME_CONTROL_REGEX = "^blitz$|^bullet$|^quick hit$"
NUMBER_REGEX = "^[1-5]{1}$"
DB = TinyDB("chess_db.json", indent=4, sort_keys=False)


class Tournaments(Style):
    def __init__(self):
        super().__init__()

    def enter_name_t(self) -> str:
        self.console.print("-" * 5 + " Please, enter the tournament name", end=" : ", style=self.style_b)
        name_t = input().capitalize()
        try:
            if re.match(NAME_REGEX, name_t):
                return name_t
            else:
                raise ValueError
        except ValueError:
            self.console.print("Please, you must respect the regular expression for reentering a tournament name.",
                               style=self.style_r)
            return self.enter_name_t()

    def enter_location_t(self) -> str:
        self.console.print("-" * 5 + " Please, enter the tournament location", end=" : ", style=self.style_g)
        location_t = input().capitalize()
        try:
            if re.match(NAME_REGEX, location_t):
                return location_t
            else:
                raise ValueError
        except ValueError:
            self.console.print("Please, you must respect the regular expression for reentering a tournament location.",
                               style=self.style_r)
            return self.enter_location_t()

    def enter_time_control(self) -> str:
        self.console.print("-" * 5 + " Please, enter the time control (blitz, bullet or quick hit)", end=" : ",
                           style=self.style_r)
        time_control = input().lower()
        try:
            if re.match(TIME_CONTROL_REGEX, time_control):
                return time_control.capitalize()
            else:
                raise ValueError
        except ValueError:
            self.console.print("Please, you must respect the regular expression for reentering a time control.",
                               style=self.style_r)
            return self.enter_time_control()

    def enter_description(self) -> str:
        self.console.print("-" * 5 + " Please, enter the tournament description", end=" : ", style=self.style_y)
        description = input()
        try:
            if len(description) < 256:
                return description
            else:
                raise ValueError
        except ValueError:
            self.console.print("Please, you must respect the condition for reentering a tournament description.",
                               style=self.style_r)
            return self.enter_description()

    def enter_number_of_rounds(self) -> int:
        self.console.print("-" * 5 + " Please, enter the number of rounds (from 1 to 5),"
                                     " the number of rounds is 4, by default, if you press Enter", end=" : ",
                           style=self.style_b)
        number_of_rounds = input()
        try:
            if re.match(NUMBER_REGEX, number_of_rounds):
                return int(number_of_rounds)
            elif number_of_rounds == "":
                return 4
            else:
                raise ValueError
        except ValueError:
            self.console.print("Please, you must respect the number of rounds in [1, 2, 3, 4, 5] (by default = 4).",
                               style=self.style_r)
            return self.enter_number_of_rounds()

    def enter_tournament_index(self) -> int:
        number = len(DB.table("tournaments"))
        self.console.print("-" * 5 + " Please, Enter the tournament index from 1 to " + str(number), end=" : ",
                           style=self.style_g)
        try:
            tournament_index = int(input())
            if tournament_index in range(1, number + 1):
                return tournament_index
            else:
                raise ValueError
        except ValueError:
            self.console.print("Please, you must reenter a tournament index from 1 to " + str(number),
                               style=self.style_r)
            return self.enter_tournament_index()

    def enter_response(self) -> str:
        self.console.print("-" * 5 + " Would do you like to update the participants rankings ? (Yes, Y / No, N)",
                           end=" : ", style=self.style_b)
        response = input()
        try:
            if response.lower() in ["yes", "y", "no", "n"]:
                return response
            else:
                raise ValueError
        except ValueError:
            self.console.print("Please, you must enter Yes or Y for updating the participants rankings.",
                               style=self.style_r)
            return self.enter_response()

    def display_enter_tournament_data(self):
        self.console.rule("[bold red]Entering of the tournament data[/]")

    def display_start_new_tournament(self, index: int):
        self.console.rule("[bold red]Start of the new tournament index [/]" + str(index))

    def display_tournament_created(self, index: int):
        self.console.rule("[bold red]The new tournament index [/]" + str(index) +
                          "[bold red] has been created and added in database[/]")

    def display_end_tournament(self, index: int):
        self.console.rule("[bold red]End of the tournament index [/]" + str(index))

    def display_no_updating_rankings(self):
        self.console.rule("[bold red]You have not chosen to update the rankings after the end of tournament[/]")

    def display_tournament_model(self, tournament: "Tournament"):
        self.console.print(tournament, style=self.style_r)
