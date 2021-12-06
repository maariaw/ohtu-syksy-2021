class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score or \
           max(self.player1_score, self.player2_score) < 4:
            return self.get_lower_score(self.player1_score, self.player2_score)
        else:
            point_difference = self.player1_score - self.player2_score
            return self.get_four_point_score(point_difference)

    def get_four_point_score(self, point_difference):
        if point_difference == 1:
            score = "Advantage " + self.player1_name
        elif point_difference == -1:
            score = "Advantage " + self.player2_name
        elif point_difference >= 2:
            score = "Win for " + self.player1_name
        else:
            score = "Win for " + self.player2_name
        return score

    @staticmethod
    def get_lower_score(first_score, second_score):
        scores = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        if first_score == second_score:
            if first_score == 4:
                return "Deuce"
            else:
                return scores[first_score] + "-All"
        return scores[first_score] + "-" + scores[second_score]
