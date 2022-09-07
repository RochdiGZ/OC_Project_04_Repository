from tinydb import TinyDB


class Player:
    """Define the player model."""
    
    def __init__(self, first_name: str = "", last_name: str = "", date_of_birth: str = "", gender: str = "",
                 ranking: int = 0, score: int = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
        self.score = score

    def __str__(self) -> str:
        return f"Ranking : {self.ranking}, {self.first_name} {self.last_name}, {self.gender}, {self.date_of_birth}"

    def update_ranking(self, new_ranking: int):
        """Update the player ranking."""
        self.ranking = new_ranking
        return self.ranking

    def serial_player(self) -> dict:
        """Serialize the class 'Player'."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "ranking": self.ranking,
            "score": self.score
        }

    def save_player(self, table_name: str, database: "TinyDB"):
        """Insert a record into the table 'players'."""
        database.table(table_name).insert(self.serial_player())
