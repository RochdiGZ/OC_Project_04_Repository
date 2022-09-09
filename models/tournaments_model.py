from datetime import date
from numpy import random
from faker import Faker
from models.players_model import Player
from views.players_view import PView

fake = Faker(locale="fr_FR")
number_of_players = 2


class Tournament:
    rounds_t = []

    def __init__(self, date_t, name_t: str = "", location_t: str = "", description_t: str = "",
                 number_of_rounds: int = 4):
        self.name_t = name_t
        self.location_t = location_t
        self.date_t = date_t
        self.description_t = description_t
        self.number_of_rounds = number_of_rounds
        self.time_control = random.choice(["Bullet", "Blitz", "Quick Hit"])

        """List of rounds into the tournament."""
        for r in range(self.number_of_rounds):
            self.rounds_t.append("Round " + str(r+1))

        """List of players into the tournament."""
        pv = PView()
        p = Player()
        self.players_t = pv.save_players(p)

    def __str__(self):
        return f"""Tournament {self.name_t} with {self.number_of_rounds} rounds in {self.location_t} on {self.date_t}
            Description : {self.description_t}
            List of rounds : {self.rounds_t}
        """


if __name__ == "__main__":
    name_tour = input("Enter the name of tournament : ")
    location_tour = input("Enter the location of tournament : ")
    description_tour = input("Enter the description of tournament : ")
    tournament = Tournament(name_t=name_tour, location_t=location_tour, date_t=date.today(),
                            description_t=description_tour)
    print(tournament)
    print("List of players :")
    for i in range(number_of_players):
        print("Player ", i+1, ":", tournament.players_t[i])
