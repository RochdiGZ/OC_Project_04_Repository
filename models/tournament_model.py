from tinydb import TinyDB, where

DB = TinyDB("chess_db.json", indent=4, sort_keys=False)


class Tournament:
    def __init__(self, date_t: str, participants_indexes: list, name_t: str = "", location_t: str = "",
                 time_control: str = "", description: str = "",  rounds_number: int = 4):
        self.index = len(DB.table("tournaments")) + 1
        self.name_t = name_t
        self.location_t = location_t
        self.date_t = date_t
        self.time_control = time_control
        self.description = description
        self.participants_indexes = participants_indexes
        self.rounds_number = rounds_number
        self.rounds = []

    def __str__(self):
        return f"The Tournament {self.name_t} in {self.location_t} on {self.date_t} with {self.rounds_number} rounds"

    def serialize_tournament(self) -> dict:
        return {
            "index": self.index,
            "name_t": self.name_t,
            "location_t": self.location_t,
            "date_t": self.date_t,
            "time_control": self.time_control,
            "description": self.description,
            "participants": self.participants_indexes,
            "rounds_number": self.rounds_number,
            "rounds": self.rounds
        }

    def add_tournament_in_db(self):
        DB.table("tournaments").insert(self.serialize_tournament())

    @staticmethod
    def update_tournament(index: int, rounds: list):
        """Update the tournament data."""
        DB.table("tournaments").update({"rounds": rounds}, where("index") == index)

    def add_participants_indexes(self, participants_indexes: list) -> list:
        return self.serialize_tournament()["participants"].append(participants_indexes)

    @staticmethod
    def extract_tournaments_indexes() -> list:
        """Extract from tournaments table a tournament index."""
        tournaments_indexes = []
        for i in range(len(DB.table("tournaments"))):
            index = DB.table("tournaments").all()[i]["index"]
            tournaments_indexes.append(index)
        return tournaments_indexes

    @staticmethod
    def extract_tournament_data(tournament_index: int) -> dict:
        """Extract from tournaments table the participants indexes."""
        if len(DB.table("tournaments")) == 0:
            return {}
        return DB.table("tournaments").get(doc_id=tournament_index)

    @staticmethod
    def deserialize_tournament(tournament_data: dict) -> "Tournament":
        name_t = tournament_data["name_t"]
        location_t = tournament_data["location_t"]
        date_t = tournament_data["date_t"]
        time_control = tournament_data["time_control"]
        description = tournament_data["description"]
        participants_indexes = tournament_data["participants"]
        rounds_number = tournament_data["rounds_number"]
        return Tournament(date_t, participants_indexes, name_t, location_t, time_control, description, rounds_number)
