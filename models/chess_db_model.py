from tinydb import TinyDB
from faker import Faker
from models.player_model import Player

fake = Faker(locale="en_US")


class Participant(Player):
    DB = TinyDB("chess_db.json", indent=4, sort_keys=False)

    def __init__(self, first_name: str = "", last_name: str = "", date_of_birth: str = "", gender: str = "",
                 ranking: int = 1):
        super().__init__(first_name, last_name, date_of_birth, gender, ranking)

    def __str__(self) -> str:
        return f"Participant {self.index} : {self.first_name} {self.last_name}, Score : {self.score}," \
               f"Ranking : {self.ranking}"

    @staticmethod
    def generate_participant() -> "Participant":
        # Enter the player data.
        if fake.random_int(0, 1) == 0:
            gender = "M"
            first_name = fake.first_name_male()
        else:
            gender = "F"
            first_name = fake.first_name_female()
        last_name = fake.last_name()
        date_of_birth = fake.date_between("-20y", "-10y").strftime("%m/%d/%Y")
        return Participant(first_name, last_name, date_of_birth, gender)

    def add_player_in_db(self):
        self.DB.table("players").insert(self.serialize_player())

    @classmethod
    def generate_add_participants(cls, participants_number: int):
        # cls.DB.table("players").truncate()
        for i in range(participants_number):
            participant = cls.generate_participant()
            participant.ranking = i + 1
            participant.add_player_in_db()
