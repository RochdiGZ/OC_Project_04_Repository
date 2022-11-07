from tinydb import TinyDB

DB = TinyDB("chess_db.json", indent=4, sort_keys=False)


class Round:
    """Define the round models."""

    def __init__(self, round_index, begin_date_time: str = "", end_date_time: str = ""):
        self.index = round_index
        self.round_name = "Round " + str(round_index)
        self.begin_date_time = begin_date_time
        self.end_date_time = end_date_time
        self.matches = []

    def __str__(self):
        if self.end_date_time == "":
            return f"The begin of {self.round_name} : {self.begin_date_time}. "
        return f"The end of {self.round_name} : {self.end_date_time}"

    def serialize_round(self) -> dict:
        return {
            "round_index": self.index,
            "round_name": self.round_name,
            "begin": self.begin_date_time,
            "end": self.end_date_time,
            "matches": self.matches
        }

    @staticmethod
    def deserialize_round(data: dict) -> "Round":
        return Round(data["round_index"], data["begin"], data["end"])
