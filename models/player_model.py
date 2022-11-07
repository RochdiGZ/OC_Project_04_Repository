from tinydb import TinyDB, where

DB = TinyDB("chess_db.json", indent=4, sort_keys=False)


class Player:
    """Define the player model."""
    def __init__(self, first_name: str = "", last_name: str = "", date_of_birth: str = "", gender: str = "",
                 ranking: int = 0):
        self.index = len(DB.table("players")) + 1
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
        self.score = 0.0

    def __str__(self) -> str:
        return f"Ranking : {self.ranking}, {self.first_name} {self.last_name}, {self.gender}, {self.date_of_birth}"

    def serialize_player(self) -> dict:
        return {
            "index": self.index,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "ranking": self.ranking,
            "score": self.score
        }

    def add_player_in_db(self):
        DB.table("players").insert(self.serialize_player())

    @staticmethod
    def update_player_ranking(index: int, new_ranking: int):
        """Update the player ranking."""
        DB.table("players").update({"ranking": new_ranking}, where("index") == index)

    @staticmethod
    def update_player_score(index: int, new_score: int):
        """Update the player ranking."""
        DB.table("players").update({"score": new_score}, where("index") == index)

    @staticmethod
    def extract_players_data(data_key: str) -> list:
        """Extract from players table :
        * players indexes if data_key="index" or
        ** players rankings if data_key="ranking"."""
        players_data = []
        for i in range(len(DB.table("players"))):
            player_data = DB.table("players").all()[i][data_key]
            players_data.append(player_data)
        return players_data

    @staticmethod
    def update_participants_rankings(indexes: list, new_rankings: list):
        """Update the participants_indexes rankings."""
        for index, new_ranking in zip(indexes, new_rankings):
            DB.table("players").update({"ranking": new_ranking}, where("index") == index)

    @staticmethod
    def extract_participants_data(participants_indexes: list) -> list:
        participants_data = []
        for index in participants_indexes:
            player_data = DB.table("players").get(doc_id=index)
            participants_data.append(player_data)
        return participants_data

    @staticmethod
    def extract_participants_data_pairs(participants_indexes_pairs: list) -> list:
        participants_data_pairs = []
        for pair in participants_indexes_pairs:
            player_data1 = DB.table("players").get(doc_id=pair[0])
            player_data2 = DB.table("players").get(doc_id=pair[1])
            participants_data_pairs.append([player_data1, player_data2])
        return participants_data_pairs

    @classmethod
    def get_participants_pairs(cls, participants_data: list) -> list:
        participants_pairs = []
        for i in range(0, len(participants_data), 2):
            participants_pairs.append([participants_data[i], participants_data[i+1]])
        return participants_pairs

    @staticmethod
    def get_participants_by_key(participants_data: list, dict_key: str) -> list:
        participants_by_key = []
        for data in participants_data:
            participants_by_key.append(data[dict_key])
        return participants_by_key

    @classmethod
    def get_participants_indexes(cls, participants_data: list) -> list:
        participants_indexes = cls.get_participants_by_key(participants_data, "index")
        return participants_indexes

    @staticmethod
    def generate_first_round_pairs(participants_indexes: list) -> list:
        half = len(participants_indexes) // 2
        list1 = participants_indexes[:half]
        list2 = participants_indexes[half:]
        participants_pairs = []
        for index1, index2 in zip(list1, list2):
            participants_pairs.append([index1, index2])
        return participants_pairs

    @staticmethod
    def generate_next_round_pairs(participants_indexes: list) -> list:
        participants_pairs = []
        for p1, p2 in zip(participants_indexes[0::2], participants_indexes[1::2]):
            participants_pairs.append([p1, p2])
        return participants_pairs
