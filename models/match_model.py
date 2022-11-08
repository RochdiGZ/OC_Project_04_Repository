class Match:
    """Define the match model."""
    def __init__(self, match_index: int, player1: dict, player2: dict, result: int = 0):
        self.index = match_index
        self.name_m = "Match " + str(self.index)
        self.player1 = player1
        self.player2 = player2
        self.result = result
        # case 0 : no winner ; case 1 : player1 is winner ; case 2 : player2 is winner

    def __str__(self) -> str:
        player1_name = self.player1["first_name"] + " " + self.player1["last_name"]
        player1_score = self.player1["score"]
        player2_name = self.player2["first_name"] + " " + self.player2["last_name"]
        player2_score = self.player2["score"]
        return f"""{self.name_m} : ([Player index {self.player1["index"]} : {player1_name}, Score : {player1_score}]
        vs [Player index {self.player2["index"]} : {player2_name}, Score : {player2_score}])"""

    def serialize_match(self) -> dict:
        return {
            "match_index": self.index,
            "name_m": self.name_m,
            "player1": self.player1,
            "player2": self.player2,
            "result": self.result
        }

    @staticmethod
    def deserialize_match(data: dict) -> "Match":
        return Match(data["match_index"], data["name_m"], data["player1"], data["player2"])

    def update_participant_score(self, match_result: int) -> (float, float):
        match match_result:
            case 0:  # no winner (draw match)
                self.player1["score"] += 0.5
                self.player2["score"] += 0.5
            case 1:  # player 1 wins
                self.player1["score"] += float(1)
            case 2:  # player 2 wins
                self.player2["score"] += float(1)
        return self.player1["score"], self.player2["score"]

    @staticmethod
    def verify_duplicate(scores_matches: list) -> bool:
        # verify duplicate score for each match
        duplicate = False
        for score in scores_matches:
            if score[0] == score[1]:
                duplicate = True
        return duplicate

    @staticmethod
    def get_participants_scores(participants_pairs: list) -> list:
        participants_scores = []
        for pair in participants_pairs:
            for p1, p2 in zip(pair[0::2], pair[1::2]):
                participants_scores.append([p1["score"], p2["score"]])
        return participants_scores
