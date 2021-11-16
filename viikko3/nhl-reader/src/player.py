class Player:
    def __init__(self, nationality, name, team, goals, assists):
        self.nationality = nationality
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.points = goals + assists

    
    def __str__(self):
        info = (
            f"{self.name:20} {self.team} "
            f"{str(self.goals):2} + {str(self.assists):2} = {str(self.points)}"
        )
        return info
