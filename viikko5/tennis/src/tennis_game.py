class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        score = ""
        temp_score = 0

        if self.player1_score == self.player2_score:
            score = self.get_even_score(self.player1_score)
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.get_four_point_score(
                self.player1_score - self.player2_score)
        else:
            score = self.get_differing_score(
                self.player1_score, self.player2_score)

        return score

    @staticmethod
    def get_even_score(on_score):
        scores = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
            3: "Forty-All"
        }

        if on_score in scores:
            return scores[on_score]

        return "Deuce"

    @staticmethod
    def get_four_point_score(minus_result):
        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    @staticmethod
    def get_differing_score(first_score, second_score):
        scores = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        return scores[first_score] + "-" + scores[second_score]
