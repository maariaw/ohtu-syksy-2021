class Player:
    def __init__(self, name, team, games, goals, assists):
        self.name = name
        self.team = team
        self.games = games
        self.goals = goals
        self.assists = assists

    
    def __str__(self):
        info = (
            f"{self.name}, {self.team} - games: {self.games} - "
            f"goals: {self.goals} - assists: {self.assists}"
        )
        return info
