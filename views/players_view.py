from tinydb import TinyDB
from models.players_model import Player

number_of_players = 2


class PView:
    """Define the player view."""

    def __init__(self):
        self.players = []

    @staticmethod
    def enter_data(p: "Player") -> dict:
        """Enter the data of player."""
        p.first_name = input("Enter the first name : ")
        p.last_name = input("Enter the last name : ")
        p.date_of_birth = input("Enter the date of birth : ")
        p.gender = input("Enter the gender : ")
        p.ranking = int(input("Enter the ranking : "))
        p.score = int(input("Enter the score : "))
        return p.serial_player()

    @staticmethod
    def create_database(file_name: str) -> "TinyDB":
        """Return an instance of TinyDB to create/open the database with the json format ."""
        return TinyDB(file_name + ".json", indent=4)

    @staticmethod
    def create_table(table_name: str, database: "TinyDB") -> "TinyDB.table":
        """Create the table to insert the players' data."""
        return database.table(table_name)

    def save_players(self, p: "Player") -> list:
        """Define an instance of the class Player."""
        players_db = self.create_database("players_db")
        players_table = self.create_table("players", players_db)
        """Remove the all records of the table"""
        players_table.truncate()
        for i in range(number_of_players):
            print("-" * 10, " Enter the data player", i + 1, "-" * 10)
            """Enter the player data."""
            dict_player = self.enter_data(p)
            """Save the player data into the table 'players'."""
            p.save_player("players", players_db)
            """Add a player into the list of dicts"""
            self.players.append(dict_player)
        return self.players

    @staticmethod
    def output(players: list):
        print("-" * 10, " List of players in the tournament ", "-" * 10)
        for i in range(number_of_players):
            print("Player", i + 1, ":", players[i])


if __name__ == "__main__":
    """Define an instance of the class Player."""
    player = Player()
    """Define an instance of the class View."""
    p_view = PView()
    list_of_players = p_view.save_players(player)
    p_view.output(list_of_players)
