import re
from tinydb import TinyDB
from models.console_style_model import Style
from models.player_model import Player
NAME_REGEX = "^[A-Z]{1}[a-z]+$"
DATE_REGEX = "^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$"
DB = TinyDB("chess_db.json", indent=4, sort_keys=False)


class Players(Style):
    def __init__(self):
        super().__init__()

    def enter_first_name(self) -> str:
        self.console.print("-" * 15 + " Please, enter the player first name", end=" : ", style=self.style_b)
        first_name = input().capitalize()
        try:
            if re.match(NAME_REGEX, first_name):
                return first_name
            else:
                raise ValueError
        except ValueError:
            self.console.print("Please, you must respect the regular expression for reentering the first name.",
                               style=self.style_r)
            return self.enter_first_name()

    def enter_last_name(self) -> str:
        self.console.print("-" * 15 + " Please, enter the player last name", end=" : ", style=self.style_g)
        last_name = input().capitalize()
        try:
            if re.match(NAME_REGEX, last_name):
                return last_name
            else:
                raise ValueError
        except ValueError:
            self.console.print("Please, you must respect the regular expression for reentering the last name.",
                               style=self.style_r)
            return self.enter_last_name()

    def enter_date_of_birth(self) -> str:
        self.console.print("-" * 15 + " Please, enter the date of birth : ", end=" : ", style=self.style_r)
        date_of_birth = input()
        try:
            if re.match(DATE_REGEX, date_of_birth):
                return date_of_birth
            else:
                raise ValueError
        except ValueError:
            self.console.print("Please, you must respect the regular expression for reentering the date of birth.",
                               style=self.style_r)
            return self.enter_date_of_birth()

    def enter_gender(self) -> str:
        self.console.print("-" * 15 + " Please, enter the gender", end=" : ", style=self.style_y)
        gender = input().upper()
        try:
            if gender in ["M", "F"]:
                return gender
            else:
                raise ValueError
        except ValueError:
            self.console.print("Please, you must reenter M or F for the gender.", style=self.style_r)
            return self.enter_gender()

    def enter_ranking(self, player_index: int, update: bool, add: bool) -> int:
        self.display_enter_player_ranking(player_index)
        number = len(DB.table("players"))
        try:
            ranking = int(input())
            if update and (ranking in range(1, number + 1)) or add and (ranking in range(1, number + 2)):
                return ranking
            else:
                raise ValueError
        except ValueError:
            if update:
                self.console.print("Please, you must reenter a ranking from 1 to " + str(number),
                                   style=self.style_r)
            self.console.print("Please, you must reenter a ranking from 1 to " + str(number+1),
                               style=self.style_r)
            return self.enter_ranking(player_index, update, add)

    def enter_player_index(self) -> int:
        number = len(DB.table("players"))
        self.console.print("-" * 15 + " Please, enter the player index from 1 to " + str(number), end=" : ",
                           style=self.style_g)
        try:
            player_index = int(input())
            if player_index in range(1, number + 1):
                return player_index
            else:
                raise ValueError
        except ValueError:
            self.console.print("Please, you must reenter a player index from 1 to " + str(number),
                               style=self.style_r)
            return self.enter_player_index()

    def enter_indexes(self, players_indexes: list, players_number: int) -> list:
        self.console.print("-" * 15 + " Please, enter " + str(players_number) + " players indexes " +
                           "in the form 1 2 3 4 5 6 7 8", end=" : ", style=self.style_b)
        try:
            indexes = list(map(int, input().split()))
            if len(indexes) != players_number:
                self.console.print(f"Please, you must reenter {players_number} players indexes.",
                                   style=self.style_r)
                return self.enter_indexes(players_indexes, players_number)
            else:
                for index in indexes:
                    if index not in players_indexes:
                        self.console.print(f"{index} is not exist as a player index in the players table.",
                                           style=self.style_y)
                        self.console.print(f"Please, you must reenter {players_number} players indexes.",
                                           style=self.style_r)
                        return self.enter_indexes(players_indexes, players_number)
        except ValueError:
            self.console.print("Please, you must respect the conditions for entering the players indexes.",
                               style=self.style_r)
            return self.enter_indexes(players_indexes, players_number)
        return indexes

    def display_enter_player_ranking(self, index: int):
        self.console.print("-" * 15 + " Please, enter the new ranking of player index " + str(index), end=" : ",
                           style=self.style_g)

    def display_generating_database(self, number: int):
        print()
        self.console.print(f"{number} players have been generated and added in the database named chess_db.json.",
                           style=self.style_b)

    def display_player_created(self):
        print()
        self.console.print("A player has been created and added in database.", style=self.style_g)

    def display_player_score_updated(self, index: int):
        self.console.print("The score of player index " + str(index) + " has been updated in the database",
                           end=".", style=self.style_g)
        print()

    def display_player_model(self, player: "Player"):
        print()
        self.console.print(player, style=self.style_g)
