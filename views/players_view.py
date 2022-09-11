from tinydb import TinyDB
from models.players_model import Player

number_of_players = 2


class PView:
    """Define the player view."""
    players = []

    @staticmethod
    def enter_data(p: "Player"):
        """Enter the data of player."""
        p.first_name = input("-" * 15 + " Enter the first name : ")
        p.last_name = input("-" * 15 + " Enter the last name : ")
        p.date_of_birth = input("-" * 15 + " Enter the date of birth : ")
        p.gender = input("-" * 15 + " Enter the gender : ")
        p.ranking = int(input("-" * 15 + " Enter the ranking : "))
        p.score = int(input("-" * 15 + " Enter the score : "))

    @staticmethod
    def serial_player(p: "Player") -> dict:
        """Serialize the class 'Player'."""
        return {
            "first_name": p.first_name,
            "last_name": p.last_name,
            "date_of_birth": p.date_of_birth,
            "gender": p.gender,
            "ranking": p.ranking,
            "score": p.score
            }

    @staticmethod
    def create_database(file_name: str) -> "TinyDB":
        """Return an instance of TinyDB to create/open the database with the json format ."""
        return TinyDB(file_name + ".json", indent=4)

    @staticmethod
    def create_table(table_name: str, database: "TinyDB") -> "TinyDB.table":
        """Create the table to insert the players' data."""
        return database.table(table_name)

    def save_players_in_list(self) -> list:
        print("-" * 5, " Enter the data players in the tournament ", "-" * 5)
        for i in range(number_of_players):
            print("-" * 10, " Enter the data player", i + 1, "-" * 10)
            p = Player()
            """Enter the player data."""
            self.enter_data(p)
            """Add a player into the list of dicts"""
            dict_player = self.serial_player(p)
            self.players.append(dict_player)
        return self.players

    def save_players_in_db(self):
        """Define an instance of the class Player."""
        players_db = self.create_database("players_db")
        players_table = self.create_table("players", players_db)
        """Remove the all records from the table"""
        players_table.truncate()
        """Save the players data into the table named 'players'."""
        dict_players = self.save_players_in_list()
        players_db.table("players").insert_multiple(dict_players)

    @staticmethod
    def output(players: list):
        print("-" * 10, " List of players in the tournament ", "-" * 10)
        for k in range(len(players)):
            print("Player", k + 1, ":", players[k])


if __name__ == "__main__":
    """Define an instance of the class Player."""
    player = Player()
    """Define an instance of the class View."""
    p_view = PView()
    p_view.save_players_in_db()
    list_of_players = p_view.save_players_in_list()
    p_view.output(list_of_players)
