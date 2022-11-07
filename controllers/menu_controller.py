from tinydb import TinyDB
# import models
from models.chess_db_model import Participant
from models.player_model import Player
from models.tournament_model import Tournament
from models.report_model import Report
# import views
from views.menus_view import Menus
from views.players_view import Players
from views.tournaments_view import Tournaments
from views.reports_view import Reports
from controllers.main_controller import MainController

DB = TinyDB("chess_db.json", indent=4, sort_keys=False)
PARTICIPANTS_NUMBER = 8


class MenuController:
    """Main controller."""
    def __init__(self):
        """Initialize models and views."""
        self.menus = Menus()
        self.players = Players()
        self.tournaments = Tournaments()
        self.reports = Reports()
        self.controllers = MainController()

    def main_menu(self):
        self.menus.display_main_menu()
        number = self.menus.choice(4)
        match number:
            case 1:
                if len(DB.table("players")) == 0:
                    # Generate and add some participants in the database named chess_db
                    self.reports.display_table_is_empty("players")
                    self.players.display_generating_database(PARTICIPANTS_NUMBER)
                    Participant.generate_add_participants(PARTICIPANTS_NUMBER)
                    self.main_menu()
                else:
                    self.access_to_players_menu()
            case 2:
                self.access_to_tournaments_menu()
            case 3:
                self.access_to_reports_menu()
            case 4:
                exit()

    def access_to_players_menu(self):
        self.menus.display_players_menu()
        choice = self.menus.choice(3)
        if choice == 1:
            # Add a player data in database
            self.controllers.add_player()
            self.access_to_players_menu()
        elif choice == 2:
            if len(DB.table("players")) == 0:
                self.reports.display_table_is_empty("players")
            else:
                # update a player ranking in database
                player_index = self.players.enter_player_index()
                new_ranking = self.players.enter_ranking()
                Player.update_player_ranking(player_index, new_ranking)
            self.access_to_players_menu()
        elif choice == 3:
            # Back to main menus.
            self.main_menu()

    def create_add_tournament_in_db(self):
        if len(DB.table("players")) == 0:
            self.reports.display_table_is_empty("players")
        elif len(DB.table("players")) < PARTICIPANTS_NUMBER:
            self.reports.display_not_enough_players()
        else:
            # Add tournament's data in database
            players_indexes = Player.extract_players_data("index")
            new_tournament = self.controllers.create_tournament(players_indexes)
            Tournament.add_tournament_in_db(new_tournament)
            tournament_data = Tournament.extract_tournament_data(new_tournament.index)
            if len(tournament_data["rounds"]) == 0:
                self.tournaments.display_tournament_created(tournament_data["index"])
                tournament_data = new_tournament.serialize_tournament()
                tournament_data = self.controllers.start_tournament(tournament_data["index"])
                self.tournaments.display_end_tournament(tournament_data["index"])
            # At the end of tournament, Updating the participants rankings
            self.controllers.updating_after_end_tournament(tournament_data)

    def select_update_tournament_in_db(self):
        if len(DB.table("players")) == 0:
            self.reports.display_table_is_empty("players")
        elif len(DB.table("players")) < PARTICIPANTS_NUMBER:
            self.reports.display_not_enough_players()
        elif len(DB.table("tournaments")) == 0:
            self.reports.display_table_is_empty("tournaments")
        else:
            # Select and start a tournament
            tournaments_indexes = Tournament.extract_tournaments_indexes()
            tournament_index = self.tournaments.enter_tournament_index(tournaments_indexes)
            tournament_data = Tournament.extract_tournament_data(tournament_index)
            if len(tournament_data["rounds"]) == 0:
                tournament_data = self.controllers.start_tournament(tournament_index)
                self.tournaments.display_end_tournament(tournament_index)
            # At the end of tournament, Updating the participants rankings
            self.controllers.updating_after_end_tournament(tournament_data)

    def access_to_tournaments_menu(self):
        self.menus.display_tournaments_menu()
        choice = self.menus.choice(3)
        if choice == 1:
            self.create_add_tournament_in_db()
        elif choice == 2:
            self.select_update_tournament_in_db()
        elif choice == 3:
            # Back to main menu.
            self.main_menu()
        # Back to tournaments menu.
        self.access_to_tournaments_menu()

    def access_to_reports_menu(self):
        self.menus.display_reports_menu()
        choice = self.menus.choice(6)
        if choice == 1 or choice == 2:
            if len(DB.table("players")) == 0:
                self.reports.display_table_is_empty("players")
            elif choice == 1:
                # Sort all players by first name
                players_list = Report.sorted_table_by(DB.table("players"), "first_name")
                # Display the sorted all players by name
                self.reports.display_players(players_list, "first_name")
            else:
                # Sort all players by first name
                players_list = Report.sorted_table_by(DB.table("players"), "ranking")
                # Display the sorted all players by ranking
                self.reports.display_players(players_list, "ranking")
        elif choice == 3:
            # Display the all tournaments
            if len(DB.table("tournaments")) == 0:
                self.reports.display_table_is_empty("tournaments")
            else:
                tournaments = Report.sorted_table_by(DB.table("tournaments"), "index")
                for tournament_dict in tournaments:
                    tournament_instance = Tournament.deserialize_tournament(tournament_dict)
                    self.tournaments.display_tournament_model(tournament_instance)
                # self.reports.display_tournaments(tournaments)
        elif choice == 4 or choice == 5:
            if len(DB.table("tournaments")) == 0:
                self.reports.display_table_is_empty("tournaments")
            else:
                tournaments_indexes = Tournament.extract_tournaments_indexes()
                tournament_index = self.tournaments.enter_tournament_index(tournaments_indexes)
                # Select a tournament
                tournament_data = self.controllers.select_tournament(tournament_index)
                participants_indexes = tournament_data["participants"]
                participants_data = Player.extract_participants_data(participants_indexes)
                if choice == 4:
                    # Sort players by name
                    participants_data = Report.sorted_list_by(participants_data, "first_name")
                    self.reports.display_players(participants_data, "first_name")
                else:
                    # Sort players by ranking
                    participants_data = Report.sorted_list_by(participants_data, "ranking")
                    self.reports.display_players(participants_data, "ranking")
                self.reports.display_rounds_matches(tournament_data["rounds"])
        elif choice == 6:
            self.main_menu()
        self.access_to_reports_menu()
