from tinydb import TinyDB
from models.console_style_model import Style
DB = TinyDB("chess_db.json", indent=4, sort_keys=False)


class Reports(Style):
    def __init__(self):
        super().__init__()

    def display_players(self, data: list, sort_key: str):
        if sort_key == "ranking":
            self.console.rule("[bold red]The sorted participants data by ranking[/]")
        else:
            self.console.rule("[bold red]The sorted participants data by name[/]")
        for i in range(len(data)):
            if i % 2 == 0:
                self.console.print("Ranking :", data[i]["ranking"], "#", data[i]["first_name"], data[i]["last_name"],
                                   style=self.style_b)
            else:
                self.console.print("Ranking :", data[i]["ranking"], "#", data[i]["first_name"], data[i]["last_name"],
                                   style=self.style_g)

    def display_tournaments(self, data: list):
        for tournament in data:
            self.console.print(f"""The tournament {tournament["name_t"]} was created on {tournament["date_t"]}
            in {tournament["location_t"]}""", style=self.style_b)

    def display_round_match(self, match_i: dict, style: str):
        self.console.print(match_i["name_m"], ":", match_i["player1"]["first_name"],
                           match_i["player1"]["last_name"], "vs", match_i["player2"]["first_name"],
                           match_i["player2"]["last_name"], ": Result :", match_i["result"], style=style)

    def display_rounds_matches(self, rounds_data: list):
        self.console.rule("[bold red]The rounds matches of the tournament[/]")
        for i in range(len(rounds_data)):
            self.console.rule("[bold blue]The matches of the round[/] " + str(i+1))
            round_i = rounds_data[i]
            self.console.print("The", round_i["round_name"], "started at", round_i["begin"] + ".", style=self.style_g)
            self.console.print("The", round_i["round_name"], "ended at", round_i["end"] + ".", style=self.style_r)
            matches_data = round_i["matches"]
            for k in range(len(matches_data)):
                match_k = matches_data[k]
                if k == 0:
                    self.display_round_match(match_k, self.style_b)
                elif k == 1:
                    self.display_round_match(match_k, self.style_g)
                elif k == 2:
                    self.display_round_match(match_k, self.style_r)
                else:
                    self.display_round_match(match_k, self.style_y)

    def display_table_is_empty(self, table_name: str):
        self.console.print("The " + table_name + " table is empty. There are 0 records in the table.",
                           style=self.style_g)

    def display_not_enough_players(self):
        self.console.print("There are not enough players for starting a tournament.", style=self.style_r)

    def display_data(self, data: dict):
        self.console.print(data, style=self.style_y)
