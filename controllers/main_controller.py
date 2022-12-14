from tinydb import TinyDB
from datetime import datetime
from time import sleep
# import models
from models.match_model import Match
from models.player_model import Player
from models.report_model import Report
from models.round_model import Round
from models.tournament_model import Tournament
# import views
from views.matches_view import Matches
from views.menus_view import Menus
from views.players_view import Players
from views.reports_view import Reports
from views.rounds_view import Rounds
from views.tournaments_view import Tournaments
DB = TinyDB("chess_db.json", indent=4, sort_keys=False)
PARTICIPANTS_NUMBER = 8


class MainController:
    """Main controller."""
    all_matches = []

    def __init__(self):
        """Initialize models and views."""
        self.menus = Menus()
        self.players = Players()
        self.tournaments = Tournaments()
        self.rounds = Rounds()
        self.matches = Matches()
        self.reports = Reports()

    def create_player(self) -> "Player":
        """Enter the player data."""
        first_name = self.players.enter_first_name()
        last_name = self.players.enter_last_name()
        date_of_birth = self.players.enter_date_of_birth()
        gender = self.players.enter_gender()
        player = Player(first_name, last_name, date_of_birth, gender)
        player.ranking = self.players.enter_ranking(player.index, update=False, add=True)
        return player

    def add_player(self):
        new_player = self.create_player()
        new_player.add_player_in_db()
        self.players.display_player_created()

    def add_players(self):
        for _ in range(PARTICIPANTS_NUMBER):
            new_player = self.create_player()
            self.players.display_player_created()
            new_player.add_player_in_db()

    def create_tournament(self, player_indexes: list) -> "Tournament":
        """Enter the tournament data."""
        self.tournaments.display_enter_tournament_data()
        name_t = self.tournaments.enter_name_t()
        location_t = self.tournaments.enter_location_t()
        date_t = datetime.now().strftime("%x")
        time_control = self.tournaments.enter_time_control()
        description = self.tournaments.enter_description()
        participants_indexes = self.players.enter_indexes(player_indexes, PARTICIPANTS_NUMBER)
        rounds_number = self.tournaments.enter_number_of_rounds()
        return Tournament(date_t, participants_indexes, name_t, location_t, time_control, description, rounds_number)

    @staticmethod
    def select_tournament(tournament_index: int) -> dict:
        tournament_data = Tournament.extract_tournament_data(tournament_index)
        return tournament_data

    @staticmethod
    def get_participants_tuples(participants_data: list) -> list:
        participants_tuples = []
        for i in range(len(participants_data)):
            participants_tuples.append((participants_data[i]["ranking"], participants_data[i]["score"],
                                       participants_data[i]))
        return participants_tuples

    def start_matches_of_round(self, round_index, participants_pairs: list) -> "Round":
        round_i = Round(round_index)
        # Add the round matches
        for index, pair in enumerate(participants_pairs, 1):
            match_i = Match(index, pair[0], pair[1])
            match_i.name_m = round_i.round_name + " " + match_i.name_m
            round_i.matches.append(match_i)
        # Status display at the start of the round
        round_i.begin_date_time = datetime.now().strftime("%x %X")
        self.rounds.display_round_created(round_index)
        self.rounds.display_start_new_round(round_index)
        self.rounds.display_round_model(round_i)
        for match_i in round_i.matches:
            self.matches.display_match_model(match_i)
        sleep(2)
        self.matches.display_enter_matches_results()
        for match_i in round_i.matches:
            # Enter the match result and update the players pair sores
            match_i.result = self.matches.enter_match_result(match_i.name_m)
            match_i.player1["score"], match_i.player2["score"] = match_i.update_participant_score(match_i.result)
            # At the end of match, Updating participants scores in the table named players by players pairs
            self.players.display_player_score_updated(match_i.player1["index"])
            Player.update_player_score(match_i.player1["index"], match_i.player1["score"])
            self.players.display_player_score_updated(match_i.player2["index"])
            Player.update_player_score(match_i.player2["index"], match_i.player2["score"])
        sleep(2)
        # Status display at the end of the round
        for match_i in round_i.matches:
            self.matches.display_match_model(match_i)
        round_i.end_date_time = datetime.now().strftime("%x %X")
        # Display round matches
        round_matches = []
        for match in round_i.matches:
            round_matches.append(match.serialize_match())
        round_i.matches = round_matches
        self.rounds.display_round_model(round_i)
        self.rounds.display_end_round(round_i.index)
        return round_i

    @staticmethod
    def regenerate_participants_pairs(pair: list, next_pair: list, all_matches: list) -> (list, list):
        if pair in all_matches:
            pair1 = [pair[0], pair[1]]
            pair2 = [pair[1], pair[0]]
            pair3 = [pair[0], next_pair[0]]
            pair4 = [pair[0], next_pair[1]]
            pair5 = [pair[1], next_pair[0]]
            pair6 = [pair[1], next_pair[1]]
            if (pair1 in all_matches) and (pair3 not in all_matches and pair3[::-1] not in all_matches):
                pair[1], next_pair[0] = next_pair[0], pair[1]
            elif (pair2 in all_matches) and (pair3 not in all_matches and pair3[::-1] not in all_matches):
                pair[1], next_pair[0] = next_pair[0], pair[1]
            elif (pair1 in all_matches) and (pair4 not in all_matches and pair4[::-1] not in all_matches):
                pair[1], next_pair[1] = next_pair[1], pair[1]
            elif (pair2 in all_matches) and (pair4 not in all_matches and pair4[::-1] not in all_matches):
                pair[1], next_pair[1] = next_pair[1], pair[1]
            elif (pair1 in all_matches) and (pair5 not in all_matches and pair5[::-1] not in all_matches):
                pair[0], next_pair[0] = next_pair[0], pair[0]
            elif (pair2 in all_matches) and (pair5 not in all_matches and pair5[::-1] not in all_matches):
                pair[0], next_pair[0] = next_pair[0], pair[0]
            elif (pair1 in all_matches) and (pair6 not in all_matches and pair6[::-1] not in all_matches):
                pair[0], next_pair[1] = next_pair[1], pair[0]
            elif (pair2 in all_matches) and (pair6 not in all_matches and pair6[::-1] not in all_matches):
                pair[0], next_pair[1] = next_pair[1], pair[0]
        return pair, next_pair

    def get_new_pairs(self, pairs: list, all_matches: list):
        for k in range(len(pairs)):
            if (k < len(pairs)-1) and (pairs[k] in all_matches):
                pairs[k], pairs[k + 1] = self.regenerate_participants_pairs(pairs[k], pairs[k + 1], all_matches)
            elif (k < len(pairs)-1) and (pairs[k][::-1] in all_matches):
                pairs[k + 1], pairs[k] = self.regenerate_participants_pairs(pairs[k + 1], pairs[k], all_matches)
            elif (k == len(pairs)-1) and (pairs[k] in all_matches):
                pairs[k], pairs[0] = self.regenerate_participants_pairs(pairs[k], pairs[0], all_matches)
            elif (k == len(pairs)-1) and (pairs[k][::-1] in all_matches):
                pairs[0], pairs[k] = self.regenerate_participants_pairs(pairs[0], pairs[k], all_matches)
        if (pairs[0] in all_matches) or (pairs[0][::-1] in all_matches):
            for i in range(len(pairs)-2):
                pairs[i], pairs[i+1] = self.regenerate_participants_pairs(pairs[i], pairs[i+1], all_matches)
        return pairs

    def start_tournament(self, tournament_index: int) -> dict:
        self.tournaments.display_start_new_tournament(tournament_index)
        tournament_data = self.select_tournament(tournament_index)
        participants_indexes = tournament_data["participants"]
        participants_data = Player.extract_participants_data(participants_indexes)
        all_matches = []
        for i in range(1, tournament_data["rounds_number"]+1):
            if i == 1:
                participants_data = Report.sorted_list_by(participants_data, "ranking")
                participants_data_pairs = Player.generate_first_round_pairs(participants_data)
            else:
                participants_data = Report.sorted_list_by(participants_data, "score")
                participants_data = Report.sort_duplicated_data(participants_data)
                participants_data_pairs = Player.generate_next_round_pairs(participants_data)
                participants_data_pairs = self.get_new_pairs(participants_data_pairs, all_matches)
            # Add the round matches
            for pair in participants_data_pairs:
                all_matches.append(pair)
            # Get the round data
            round_i = self.start_matches_of_round(i, participants_data_pairs)
            # At the end of round, Updating of the tournament rounds in the tournaments table
            round_data = round_i.serialize_round()
            tournament_data["rounds"].append(round_data)
            Tournament.update_tournament(tournament_index, tournament_data["rounds"])
        return tournament_data

    def updating_after_end_tournament(self, tournament_data: dict):
        response = self.tournaments.enter_response()
        if response.lower() in ["yes", "y"]:
            participants_indexes = tournament_data["participants"]
            for index in participants_indexes:
                self.players.display_enter_player_ranking(index)
                new_ranking = self.players.enter_ranking(index, update=True, add=False)
                Player.update_player_ranking(index, new_ranking)
        else:
            self.tournaments.display_no_updating_rankings()
