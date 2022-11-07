from models.match_model import Match
from models.console_style_model import Style


class Matches(Style):
    def __init__(self):
        super().__init__()

    def enter_match_result(self, match_name: str) -> int:
        print()
        try:
            self.console.print("-" * 40 + " Please, enter the " + match_name + " result (0, 1, 2)", end=" : ",
                               style=self.style_b)
            match_result = int(input())
            if match_result in [0, 1, 2]:
                return match_result
            else:
                raise ValueError
        except ValueError:
            self.console.print("Please, you must reenter an integer number (0, 1, 2) for the match result.",
                               style=self.style_r)
            return self.enter_match_result(match_name)

    def display_enter_matches_results(self):
        self.console.rule("[bold red]Entering of the matches results[/]")
        self.console.print("Match result = 0 : no winner (draw match)", "|",
                           "Match result = 1 : player1 is winner", "|",
                           "Match result = 2 : player2 is winner", style=self.style_y)

    def display_match_model(self, match: "Match"):
        print()
        if match.index % 2 == 1:
            self.console.print(match, style=self.style_y)
        else:
            self.console.print(match, style=self.style_g)
        print()
